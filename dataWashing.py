import csv

# 把taipeiCovid.csv裡面的資料按照不同區寫成區名.csv
# 資料為各區時間軸上的確診人數

f = open('./raw_data/taipeiCovid.csv', encoding='utf-8')
f2 = open('./filtered/台北確診人數/分區/全區.csv', 'w', encoding='utf-8', newline='')
f3 = open('./filtered/台北確診人數/分區/萬華區.csv', 'w', encoding='utf-8', newline='')
f4 = open('./filtered/台北確診人數/分區/士林區.csv', 'w', encoding='utf-8', newline='')
f5 = open('./filtered/台北確診人數/分區/文山區.csv', 'w', encoding='utf-8', newline='')
f6 = open('./filtered/台北確診人數/分區/大同區.csv', 'w', encoding='utf-8', newline='')
f7 = open('./filtered/台北確診人數/分區/安區.csv', 'w', encoding='utf-8', newline='')
f8 = open('./filtered/台北確診人數/分區/信義區.csv', 'w', encoding='utf-8', newline='')
f9 = open('./filtered/台北確診人數/分區/中山區.csv', 'w', encoding='utf-8', newline='')
f10 = open('./filtered/台北確診人數/分區/中正區.csv', 'w', encoding='utf-8', newline='')
f11 = open('./filtered/台北確診人數/分區/北投區.csv', 'w', encoding='utf-8', newline='')
f12 = open('./filtered/台北確診人數/分區/內湖區.csv', 'w', encoding='utf-8', newline='')
f13 = open('./filtered/台北確診人數/分區/松山區.csv', 'w', encoding='utf-8', newline='')

header = ['id', '個案研判日', '個案公布日', '縣市', '區域', '新增確診人數', '累計確診人數', '七天移動平均新增確診']
csv.writer(f2).writerow(header)
csv.writer(f3).writerow(header)
csv.writer(f4).writerow(header)
csv.writer(f5).writerow(header)
csv.writer(f6).writerow(header)
csv.writer(f7).writerow(header)
csv.writer(f8).writerow(header)
csv.writer(f9).writerow(header)
csv.writer(f10).writerow(header)
csv.writer(f11).writerow(header)
csv.writer(f12).writerow(header)
csv.writer(f13).writerow(header)

rows = csv.reader(f, delimiter=",")

for row in rows:
    if row[4] == "全區":
        csv.writer(f2).writerow(row)
    if row[4] == "萬華區":
        csv.writer(f3).writerow(row)
    if row[4] == "士林區":
        csv.writer(f4).writerow(row)
    if row[4] == "文山區":
        csv.writer(f5).writerow(row)
    if row[4] == "大同區":
        csv.writer(f6).writerow(row)
    if row[4] == "大安區":
        csv.writer(f7).writerow(row)
    if row[4] == "信義區":
        csv.writer(f8).writerow(row)
    if row[4] == "中山區":
        csv.writer(f9).writerow(row)
    if row[4] == "中正區":
        csv.writer(f10).writerow(row)
    if row[4] == "北投區":
        csv.writer(f11).writerow(row)
    if row[4] == "內湖區":
        csv.writer(f12).writerow(row)
    if row[4] == "松山區":
        csv.writer(f13).writerow(row)
    

f.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()
f13.close()