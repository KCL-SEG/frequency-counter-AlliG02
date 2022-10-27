"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from xml.etree.ElementTree import tostring


def frequencies(items):
    frequencies = {}
    # Your code goes here

    for x in range(len(items)):
        items[x] = str(items[x])

    for i in range(len(items)):
        element = items[i]
        frequencies[element] = items.count(element)

    return frequencies