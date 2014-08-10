# -*- coding: utf-8 -*-

import json, sys

def ascii(s):
    return ''.join([c for c in s if (ord(c) < 128 and c != ',')])

if len(sys.argv) < 2:
    print "usage: python ingress.py [input json file]"
    sys.exit()
text = open(sys.argv[-1]).read()
data = json.loads(text)


for timestamps in data["result"]["map"].keys():
    for portal in data["result"]["map"][timestamps]["gameEntities"]:
        info = portal[2]
        try:
            temp = info["points"]
            continue # ignore the fields
        except:
            pass

        # ignore the links
        if(info["type"] != "portal"): continue

        # title, lat, lng = info["title"].encode('utf-8'), info["latE6"], info["lngE6"]
        title, lat, lng = ascii(info["title"].strip()), info["latE6"], info["lngE6"]
        print (title+",").ljust(55)+(str(lat)+",").ljust(10)+(str(lng)+",").ljust(10)+"  0, False"
