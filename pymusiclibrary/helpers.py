#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import List


def get_folders(startingFolder: str) -> List:
    """
    Generic function that lists a folder and creates a list of sub-folders found in starting folder.
    It takes only first level from starting point. Does not go any deeper inside the folder structure.
    :param str startingFolder: starting point for search (not returned in list of results)
    :return: list of folder names or empty list if there are no folders inside starting folder.
    :rtype: List
    """
    folders = []
    if (not os.path.exists(startingFolder)) or (not os.path.isdir(startingFolder)):
        return folders

    for item in os.listdir(startingFolder):
        if os.path.isdir(startingFolder + "\\" + item):
            folders.append(item)
    return folders


def get_files(startingFolder: str) -> List:
    """
    # TODO make this as a generator function
    Generic function that lists a folder and creates a list of files contained in that folder.
    It lists only files contained in the starting folder and does not look for files inside sub-folders of starting
    folder.
    :param str startingFolder: starting point
    :return: list of file names (with extension) or empty list if there are no files inside starting folder.
    :rtype: List
    """
    files = []
    if (not os.path.exists(startingFolder)) or (not os.path.isdir(startingFolder)):
        return files
    for item in os.listdir(startingFolder):
        if os.path.isfile(startingFolder + "\\" + item):
            files.append(item)
    return files
