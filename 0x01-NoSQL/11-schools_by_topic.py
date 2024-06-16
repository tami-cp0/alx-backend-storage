#!/usr/bin/env python3
""" Module """


def schools_by_topic(mongo_collection, topic):
    """
    Finds all documents where 'topics' contains the specified topic

    Returns:
        A list of schools containing that topic.
    """
    schools = mongo_collection.find({'topics': topic})

    return list(schools)
