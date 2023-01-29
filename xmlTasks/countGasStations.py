from urllib.request import urlopen
import xmltodict
import os.path

if not os.path.exists('map2.osm'):
    http = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm').read().decode('utf-8')
    file = open('map2.osm', 'w', encoding='utf8')
    file.write(str(http))
    file.close()

fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()
parsed_xml = xmltodict.parse(xml)
count_gs = 0
for node in dict(parsed_xml)['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    count_gs += 1
        else:
            if '@k' in tags and tags['@k'] == 'amenity' and tags['@v'] == 'fuel':
                count_gs += 1
print(count_gs)
