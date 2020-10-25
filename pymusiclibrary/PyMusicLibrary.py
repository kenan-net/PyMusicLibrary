#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
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
        if os.path.isdir(startingFolder+"\\"+item):
            folders.append(item)
    return folders


def get_files(startingFolder: str) -> List:
    """
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


def get_artists(startingFolder: str) -> List:
    """
    Creates the list of artists available following the convention:
    name of every folder inside the startingFolder is an artist name
    every folder inside the artistFolder is album name
    every file (ending with mp3) inside the album folderor artist folder is song by that artist.
    Example:
    MyMusic
        ArtistName
            song.mp3
            AlbumName
                song1.mp3
                song2.mp3
    :param str startingFolder: path to a root folder from where the search starts
    :return: list of artists
    :rtype: List
    """
    artists = []
    artists = get_folders(startingFolder)
    return artists


def get_albums(startingFolder: str) -> List:
    """
    Creates the list of albums from a single artist following the convention:
    name of every folder inside the startingFolder is an album name
    Example:
        ArtistName
            Album 1
                song1.mp3
                song2.mp3
            Album 2
                song1.mp3
                song2.mp3
    :param str startingFolder: path to a root folder from where the search starts
    :return: list of albums or empty list
    :rtype: List
    """
    albums = []
    albums = get_folders(startingFolder)
    return albums


def get_songs(startingFolder: str) -> List:
    """
    Creates list of songs contained inside one folder.
    :param str startingFolder: path to a root folder from where the search starts
    :return: list of songs
    :rtype: List
    """
    songs = []
    songs = get_files(startingFolder)
    return songs


def get_album_year(albumName: str) -> int:
    """
    Takes 1 argument, and that is album name as a string. Parses this string looking for numbers as this could be the
    album year.
    In order to recognize numbers as album year, following conventions must be followed:
    - album year must be at the beginning or at the end of the given string
    - there must be a total of 4 digits consecutively in given string
    - the number could not be lower than 1900 or greater than (current year + 1)
    Example of album names with album year:
    - Some album [2002]
    - [2002] Some 1 album
    - 2002 Some album
    - Some album 2002
    Example of album names with incorrect album years:
    - Some album [20025]
    - [2002] Some album [2002]
    - Some album [2002]
    - Some [2002] album
    :param albumName: album name that possibly contains numbers
    :return: album year if found, or -1 if album year could not be found
    :rtype: int
    """
    # TODO "Some [2002] album" - this would be recognized as correct year but it should not!
    numbers = ""
    numbersFound = False
    charactersProcessed = 0
    for character in albumName:
        charactersProcessed += 1
        if character.isdigit():
            numbersFound = True
            numbers += character
        else:
            if numbersFound and len(numbers) < 4:
                numbersFound = False
                # print("restarting numbers string")
                numbers = ""

    if len(numbers) == 0 or len(numbers) > 4:
        return -1

    if numbers.isdigit():
        albumYear = int(numbers)
        if albumYear < 1920 or albumYear > (datetime.datetime.now().year + 1):
            albumYear = -1
    else:
        albumYear = -1
    return albumYear
