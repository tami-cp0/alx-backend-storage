#!/usr/bin/env python3
"""
Script  that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == '__main__':
    """Prints the log stats in nginx collection"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    # number of logs
    count = logs.count_documents({})

    get = logs.count_documents({"method": "GET"})
    post = logs.count_documents({"method": "POST"})
    put = logs.count_documents({"method": "PUT"})
    patch = logs.count_documents({"method": "PATCH"})
    delete = logs.count_documents({"method": "DELETE"})

    doc = logs.count_documents({"method": "GET", "path": "/status"})

    print(
        f"{count} logs\n"
        "Methods:\n"
        f"\t method GET: {get}\n"
        f"\t method POST: {post}\n"
        f"\t method PUT: {put}\n"
        f"\t method PATCH: {patch}\n"
        f"\t method DELETE: {delete}\n"
        f"{doc} status check"
    )
