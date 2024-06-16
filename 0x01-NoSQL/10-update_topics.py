#!/usr/bin/env python3
""" Module """
from typing import List


def update_topics(mongo_collection, name: str, topics: List[int]) -> None:
    """
    Updates the query object gotten using name
    and sets a topic
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
