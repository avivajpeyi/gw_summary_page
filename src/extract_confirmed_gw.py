#!/usr/bin/env python3
"""
Confirmed GW

Prefix
The prefix is determined by the superevent’s “status” (is it marked as a “confirmed GW” or not) and its category. A superevent’s category will never change, but its status can, resulting in a prefix change. When this happens, the superevent will be accessible (via URLs, the API, searches, etc.) by both its old and new IDs.

|  Category  | Not a confirmed GW | Confirmed GW |
|:----------:|:------------------:|:------------:|
| Production |          S         |      GW      |
|    Test    |         TS         |      TGW     |
|     MDC    |         MS         |      MGW     |

"""


from ligo.gracedb.rest import GraceDb

GRACE_ID_KEY = "graceid"


def count_iterable(i):
    return sum(1 for _ in i)


def get_data(query: str):
    grace_client = GraceDb()
    events = grace_client.events("gid: GW150914")
    events = grace_client.events("GW150914")
    events = grace_client.events("is_gw: True")
    events = grace_client.events("is_gw")

    print(count_iterable(events))

    results = {}
    for event in events:
        grace_id = event.get(GRACE_ID_KEY)
        results.update({grace_id: event})

    return results


def main():
    get_data(query='instruments = "H1,L1,V1" & far < 1e-7')


if __name__ == "__main__":
    main()

client = GraceDb()
