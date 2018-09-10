# coding: utf-8

import sys, json
from collections import Counter
from natasha import SimpleNamesExtractor

lines = sys.argv[1].split(",")
extractor = SimpleNamesExtractor()
names = Counter()
surnames = Counter()
for line in lines:
    matches = extractor(line)
    if matches.__len__() == 0:
        continue
    match = matches[0]
    if match.fact.first is not None:
        names[match.fact.first] +=1
    if match.fact.last is not None:
        surnames[match.fact.last] +=1

data = {
    'names': {},
    'surnames': {}
}
for (name, count) in names.most_common(2):
    if count < 2 or name.__len__() < 3:
        continue
    data['names'][name] = count

for (surname, count) in surnames.most_common(2):
    if count < 2 or surname.__len__() < 3:
        continue
    data['surnames'][surname] = count

print(json.dumps(data))