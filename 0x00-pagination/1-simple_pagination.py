#!/usr/bin/env python3
"""This module contains the function index_range"""

import csv
import math
from os import X_OK
from typing import List, Tuple, Dict


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


class Server:
    """Server class to paginate a database of popular baby names"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Init method for server class"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE, "r") as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This function get the page with the pagination"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        page_range = index_range(page, page_size)
        if page_range[0] >= len(dataset):
            return []
        return dataset[page_range[0]:page_range[1]]