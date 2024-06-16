#!/usr/bin/env python3
""" Module """


def insert_school(mongo_collection, **kwargs):
    """
    Creates a new document with the key-value pairs in kwargs.

    Returns:
        The _id of the created document.
    """
    document = {}
    for key, value in kwargs.items():
        document[key] = value

    return mongo_collection.insert_one(document).inserted_id
