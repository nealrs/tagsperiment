import argparse
import requests
import re
from tagdb import *

parser = argparse.ArgumentParser(description='Analyze Devpost project and suggest tech & api tags.')
parser.add_argument('project', metavar='p', type=str, help='a Devpost URL slug (e.g. sincerely)')

args = parser.parse_args()
project = args.project

## GET PROJECT DATA
api = "https://iii3mdppm7.execute-api.us-east-1.amazonaws.com/prod/ProjectEndpoint/"
text = ""
etags = [];

r = requests.get(api+project)
if r.status_code is 200:
    text = text + r.json()['title'] + "\n"
    text = text + r.json()['tagline'] + "\n"
    text = text + r.json()['description_text'] + "\n"
    for x in r.json()['collaborators']:
        text = text + x['contribution'] + "\n"
    for x in r.json()['built_with']:
        etags.append(str(x['name']))

print "Project title, tagline, description, and contributions: \n" + text + "\n"
print "Existing tags: "
print str(etags) + "\n"

## EXTRACT TAGS
stags = [];
for t in db:
    reg = t['phrase'] + r'\b';
    if re.search(reg, text, re.IGNORECASE):
        stags.append(str(t['tag']))
stags = list(set(stags))

print "Suggested tags: \n"
print stags
