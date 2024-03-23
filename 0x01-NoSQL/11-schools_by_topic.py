#!/usr/bin/env python3
"""
find topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find topic
    """
    return mongo_collection.find({"topics": topic})
