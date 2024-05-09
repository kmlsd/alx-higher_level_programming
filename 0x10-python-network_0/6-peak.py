#!/usr/bin/python3
"""Finds peak in unsorted list of integers"""

def check_peak(_list, start_index, stop_index):
    """Recursively finds peak"""
    if stop-index - start_index < 2:
        return None
    mid = (start_index + stop_index) // 2
    if _list[mid] >= _list[mid - 1] and _list[mid] >= _list[mid + 1]:
        return _list[mid]
    return check_peak(_list, start_index, mid) and check_peak(_list, mid, stop_index)

def find_peak(list_of_integers):
    """Finds peak in unsorted list of integers"""

    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return check_peak(list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]

