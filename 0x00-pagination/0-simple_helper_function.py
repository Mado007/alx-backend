#!/usr/bin/env python3
"""Define `index_range` function."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of the start and end indexes
    of a list for those particular pagination parameters."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
