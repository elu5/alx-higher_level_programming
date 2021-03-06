#!/usr/bin/python3

"""
This file contains a function
that creates an object from a "JSON FILE"
"""
import json

def load_from_json_file(filename):
    """
     creates object from json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
        f.close()
