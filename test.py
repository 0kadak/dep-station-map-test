"""
this programs aims at learning how overpass api works. the complete version is on index.html
"""

import urllib.parse
import urllib.request
import json

police='''
[out:json];
node['amenity'='police']['addr:city'='札幌市'];
out body;
'''
firestation='''
[out:json];
node['amenity'='fire_station']['addr:city'='札幌市'];
out body;
'''

def getOSM_namecoordinates(OSMQL:str):
    url = 'https://z.overpass-api.de/api/interpreter?data='
    e = urllib.parse.quote(OSMQL)
    url += e
    with urllib.request.urlopen(url) as r:
        response = r.read() # type:bytes

    resjson = json.loads(response)
    elements = resjson['elements']
    osmList = list()
    for element in elements:
        name = element['tags']['name:ja']
        coordinates = (element['lat'], element['lon'])
        osmList.append(name + '\t' + str(coordinates)+'\n')
    return osmList

with open('./output.txt', 'w') as f:
    f.writelines(getOSM_namecoordinates(firestation))
    f.writelines(getOSM_namecoordinates(police))