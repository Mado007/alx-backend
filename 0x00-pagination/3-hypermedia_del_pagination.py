#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return dictionary of appropriate page."""
        indexed_dataset = self.indexed_dataset()
        total_size = len(indexed_dataset)
        assert 0 <= index and index < total_size
        actual_size = 0
        data = []
        start = index
        while index < total_size and actual_size < page_size:
            if indexed_dataset.get(index) is not None:
                data.append(indexed_dataset.get(index))
                actual_size += 1
            index += 1

        return {
            'index': start,
            'data': data,
            'page_size': actual_size,
            'next_index': index
        }
