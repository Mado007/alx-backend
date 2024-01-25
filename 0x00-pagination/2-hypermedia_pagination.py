#!/usr/bin/env python3
"""Define `index_range` function and `Server` class."""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of the start and end indexes
    of a list for those particular pagination parameters."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset."""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()
        total_size = len(dataset)
        max_page_num = math.ceil(total_size / page_size)
        if page < 1 or page > max_page_num:
            return []

        start, end = index_range(page, page_size)
        return dataset[start:min(end, total_size)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a dictionary of the appropriate page of the dataset."""
        data = self.get_page(page, page_size)
        max_page_num = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < max_page_num else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': max_page_num
        }
