#!/usr/bin/env python3
from ligo.gracedb.rest import GraceDb, HTTPError

client = GraceDb()

try:
    r = client.ping()
except HTTPError as e:
    print(e.message)

print("Response code: {}".format(r.status))
print("Response content: {}".format(r.json()))
