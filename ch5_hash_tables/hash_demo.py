#!/usr/bin/env python

# A hash table is a data structure that combines a hash function and an array.

# Collisions occur when a hash function assigns two keys to the same slot in the array.
# Optimal hash functions are designed to minimize collisions.

# A hash table needs a low load factor and a good hash function to reduce collisions.
# A load factor is a measure of data concentration in a hash table.
# Compute the load factor = number of items in table / the number of slots in array.
# When the load factor reache 0.7 or higher, resize the array.

# The performance of a hash table relies on a good hash function.
# Good hash functions have search/read, insert and delete complexity of O(1).
# Bad hash functions have read, insert and delete complexity of O(n).

# Hash functions excel at finding duplicates.
team = {'Sara': 'dev', 'Sid': 'devops', 'Suresh':'ux', 'Sol': 'production manager'}
name, role = 'Sampson', 'graphic designer'
def check_person(name):
    if team.get(name):
        print(f'{name} is already on the team. Duplicate detected.')
    else:
        team[name] = role
        print(f'New team member {name} as {role}.')

# Hash functions also are great for caching.
# Data that is accessed frequently is stored in a hash table.
# Caching takes strain off of web servers.
# When a user goes to a site, the cache is the first line of defense.
# If the site is not in the cache of commonly accessed pages,
# then the request is passed to the server.
cache = {}
url = 'www.banana.com'
def get_data_from_server():pass
def get_webpage(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data