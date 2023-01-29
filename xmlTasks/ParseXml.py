import xmltodict
from urllib.request import urlopen

http = urlopen('https://stepik.org/media/attachments/lesson/245571/map1.osm').read().decode('utf-8')
file = str(http)
fout = open('map1.osm', 'w', encoding='utf8')
fout.write(file)
fout.close()

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])
