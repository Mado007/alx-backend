#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('../2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()

my_cache.put("E", "Battery")    # discard d
my_cache.print_cache()  # a b c e

my_cache.put("C", "Street")
my_cache.print_cache()  # a b c:street e

my_cache.put("F", "Mission")   # discard e
my_cache.print_cache()    # a b c f

my_cache.put("G", "San Francisco")    # discard f
my_cache.print_cache()    # a b c f
