#!/usr/bin/env python

import codecs
import cStringIO
import csv
import json

# Script to convert the data.json file, scraped using the Scrapy spider
# from the EU Whoiswho website, to a CSV stored in data.csv

# Write CSV with correct encoding
# Taken from: https://docs.python.org/2/library/csv.html#examples
class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

# Load the data from data.json
with open('data.json') as IN:
    data = json.load(IN)

# Open data.csv and write the converted data to it
with open('data.csv', 'w') as OUT:
    wr = UnicodeWriter(OUT, quoting=csv.QUOTE_ALL, lineterminator='\n')
    wr.writerow(
        [
            'hierarchy',
            'title',
            'name',
            'email',
            'telephone',
            'fax',
            'url',
            'source'
        ]
    )

    all_csv_data = []
    for item in data:
        csv_data = []
        # Separate items in the hierarchy list with a '|' in order to
        # make a single string which we can place in 1 CSV cell
        csv_data.append(' | '.join(item['hierarchy']))
        if item['title']:
            csv_data.append(item['title'])
        else:
            csv_data.append('')
        if item['name']:
            csv_data.append(item['name'])
        else:
            csv_data.append('')
        if item['email']:
            csv_data.append(item['email'])
        else:
            csv_data.append('')
        # Combined multiple telephone numbers with a comma
        if item['telephone']:
            csv_data.append(', '.join(item['telephone']))
        else:
            csv_data.append('')
        if item['fax']:
            csv_data.append(item['fax'])
        else:
            csv_data.append('')
        if item['url']:
            csv_data.append(item['url'])
        else:
            csv_data.append('')
        if item['source']:
            csv_data.append(item['source'])
        else:
            csv_data.append('')

        all_csv_data.append(csv_data)

    wr.writerows(sorted(all_csv_data))
