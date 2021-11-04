import json
import csv

with open('./raw_data/taipeiCovid.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

f = open('./raw_data/taipeiCovid.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(f)
count = 0
for row in data:
    if count == 0:
        header = row.keys()
        csv_writer.writerow(header)
        count += 1
    else:
        csv_writer.writerow(row.values())
    # tmp = row
    # print(tmp)

f.close()
        