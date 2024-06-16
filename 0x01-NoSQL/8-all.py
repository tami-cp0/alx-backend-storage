#!/usr/bin/env python3
""" Module """


def list_all(mongo_collection):
    """
    Returns:
        A list of all documents in the mongo_collection,
        An empty list if no documents are found in mongo_colection
    """
    if not mongo_collection.find():
        return []

    collection = [document for document in mongo_collection.find()]
    return collection
