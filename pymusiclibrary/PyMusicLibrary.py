#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
from . import helpers
from typing import List


class PyMusicLibrary:
    """
    This class provides methods to create a simple but usable music library.

    Attributes
    ----------
    root
        Path to starting folder where all the music is stored.

    Methods
    -------
    __init__(self, startingFolder: str)
        Class initializer.
    get_artist
        Provides a list of artists that can be found in the starting folder.
    get_albums
        Provides a list of albums that can be found in the folder of 1 artist.
    get_songs
        Provides a list of songs that can be found in the folder of 1 album or 1 artist.
    """

    def __init__(self, startingFolder: str):
        """
        Class initializer.

        :param str startingFolder: path to a folder where all the music (artists/albums/songs) is stored.
        """
        # Todo : add tests here if the path exists, if the path is folder etc. If basic conditions are not met, it must
        #  fail!
        self._initialized = False
        if (not os.path.exists(startingFolder)) or (not os.path.isdir(startingFolder)):
            print("Init failed! Path does not exist or it is not a folder!")
            self.root = startingFolder = None
        else:
            self.root = startingFolder
            self._initialized = True
        self._artists = None

    def get_artists(self) -> List:
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
        if not self._initialized:
            print("Get artists: not init")
            return artists
        self._artists = helpers.get_folders(self.root)
        print("Get artists: {0}".format(len(self._artists)))
        return self._artists

    def get_albums(self, artistName: str) -> List:
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
        :param str artistName: name of the artist (folder name) for whom we want to get the albums.
        :return: list of albums or empty list
        :rtype: List
        """
        albums = []
        print("Get Albums started")
        if not self._initialized:
            print("not initialized")
            return albums
        if self._artists is None:
            print("No artists!")
            return albums
        print("Artists in library: {0}".format(len(self._artists)))
        if artistName not in self._artists:
            print("Artist not found")
            return albums
        albums = helpers.get_folders(self.root + "\\" + artistName)
        return albums

    def get_songs(self, startingFolder: str) -> List:
        """
        Creates list of songs contained inside one folder.
        :param str startingFolder: path to a root folder from where the search starts
        :return: list of songs
        :rtype: List
        """
        songs = []
        if not self._initialized:
            return songs
        songs = helpers.get_files(startingFolder)
        return songs

    @staticmethod
    def get_album_year(self, albumName: str) -> int:
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
