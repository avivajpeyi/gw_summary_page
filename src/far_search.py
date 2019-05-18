#!/usr/bin/env python3
from ligo.gracedb.rest import GraceDb

client = GraceDb()

# Retrieve an iterator for events matching a query.
events = client.events("gstlal ER5 far < 1.0e-4")

# For each event in the search results, add the graceid
# and chirp mass to a dictionary.
results = {}
for event in events:
    graceid = event["graceid"]
    mchirp = event["extra_attributes"]["CoincInspiral"]["mchirp"]
    results.update({graceid: mchirp})


# For each super event in the search results, add the superevent_id
# and chirp mass to a dictionary.
superevents = client.superevents("gstlal ER5 far < 1.0e-4")
s_results = {}
for superevent in superevents:
    superevent_id = superevent["superevent_id"]
    mchirp = superevent["extra_attributes"]["CoincInspiral"]["mchirp"]
    s_results.update({superevent_id: mchirp})
