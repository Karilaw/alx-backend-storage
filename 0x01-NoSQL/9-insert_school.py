#!/usr/bin/env python3
"""
insert documents
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert
    """
    return mongo_collection.insert_one(kwargs).inserted_id
