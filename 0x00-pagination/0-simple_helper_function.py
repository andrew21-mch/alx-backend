#!/usr/bin/env python3
""" 
    Write a function named index_range that takes
    two integer arguments page and page_size.
"""

def index_range(page: int, page_size: int) -> tuple:
    """ create a tuple containing page and the page_size """
    return ((page - 1 ) * page_size, ((page - 1 ) * page_size) + page_size )
print(index_range(3,15))