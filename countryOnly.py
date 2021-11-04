import csv

# 把各國空氣品質的檔案中挑選TW(台灣)挑選出來

f = open('./raw_data/waqi-covid19-airqualitydata-2020.csv', encoding='utf-8')
f2 = open('./filtered/taiwan_air_quality_2020.csv', 'w', encoding='utf-8', newline='')

header = ['日期', '國家', '城市', '項目', '次數', 'min', 'max', 'median', 'variance']
csv.writer(f2).writerow(header)

rows = csv.reader(f)
count = 1
for row in rows:
    if count >= 6:
        if row[1] == 'TW':
            csv.writer(f2).writerow(row)
    count += 1

f.close()
f2.close()

# 從台灣空氣品質資料中挑出台北市

f = open('./filtered/空氣品質/taiwan_air_quality_2020.csv', encoding='utf-8')
f2 = open('./filtered/空氣品質/taipei_air_quality_2020.csv', 'w', encoding='utf-8', newline='')

csv.writer(f2).writerow(header)
rows = csv.reader(f)
for row in rows:
    if row[2] == 'Taipei':
        csv.writer(f2).writerow(row)

f.close()
f2.close()