#!/usr/bin/env python3


"""This script is for pagenization of the data"""


def index_range(page: int, page_size: int) -> tuple:
    """AI is creating summary for index_range

    Args:
        page (int): [number of page]
        page_size (int): [number of page_size]

    Returns:
        tuple: [a tuple of two integers indicating the start and end index
        of the range]
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
