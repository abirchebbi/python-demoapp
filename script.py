import xmltodict, json;
with open('test-results.xml', 'r') as myfile:
    obj = xmltodict.parse(myfile.read())
f=open('results.json', 'w')
f.write(json.dumps(obj))

