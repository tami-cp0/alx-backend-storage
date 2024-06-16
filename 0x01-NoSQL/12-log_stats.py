#!/usr/bin/env python3
"""
Script  that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
logs = client.logs.nginx

# number of logs
count = logs.count_documents({})

get = len([log for log in logs.find({"method": "GET"})])
post = len([log for log in logs.find({"method": "POST"})])
put = len([log for log in logs.find({"method": "PUT"})])
patch = len([log for log in logs.find({"method": "PATCH"})])
delete = len([log for log in logs.find({"method": "DELETE"})])

doc = len([log for log in logs.find({"method": "GET", "path": "/status"})])

print(
    f"{count}\n"
    "Methods:\n"
    f"\t method GET: {get}\n"
    f"\t method POST: {post}\n"
    f"\t method PUT: {put}\n"
    f"\t method PATCH: {patch}\n"
    f"\t method DELETE: {delete}\n"
    f"{doc} status check"
)
