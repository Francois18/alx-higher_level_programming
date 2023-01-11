#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json

def to_json(obj: object) -> str:
 """Return the JSON representation of a string object."""
    return json.dumps(obj, default=str)
