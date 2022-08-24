#import json
#import re
#
#with open("./conditions.json") as f:
#    CONDITIONS = json.load(f)
#    f.close()
#
#list_prereqs = re.findall("[A-Z][A-Z][A-Z][A-Z]\d\d\d\d", CONDITIONS.get('COMP1531'))
#print(list_prereqs)

print(False and False or True)
print(False and (False or True))