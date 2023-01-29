from urllib.request import urlopen
import xmltodict

http = urlopen('https://stepik.org/media/attachments/lesson/245678/map1.osm').read().decode('utf-8')
fout = open('map1.osm', 'w', encoding='utf8')
fout.write(str(http))
fout.close()

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()
count_total = 0
count_tag = 0
parsedXml = xmltodict.parse(xml)
for node in dict(parsedXml)['osm']['node']:
    count_total += 1
    if 'tag' in node:
        count_tag += 1
print(count_tag, count_total - count_tag)
