#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
from pymusiclibrary import getArtistsAlbumsSongs


@pytest.fixture
def create_test_env():
    """

    :return:
    """
    # Create dummy folder structure
    cwd = os.getcwd()
    os.makedirs(cwd + "\\Music\\Artist1", exist_ok=True)
    os.makedirs(cwd + "\\Music\\Artist2", exist_ok=True)
    os.makedirs(cwd + "\\Music\\Artist3", exist_ok=True)

    # Create dummy file.
    if not os.path.exists(cwd + "\\dummy_file.txt"):
        try:
            f = open("dummy_file.txt", "a+")
        except OSError:
            print("Could not create dummy file.")
            return False
        f.write("Dummy File content")
        f.close()
    else:
        return True


def test_get_artists_1():
    """
    Tests if the check for artists in non existing folder returns 0 artists.
    :return: None
    """
    artists = getArtistsAlbumsSongs.get_artists("C:\\DummyTestFolder")
    assert len(artists) == 0, "Folder does not exist!"


def test_get_artists_2(create_test_env):
    """
    Tests if the check for artists returns a list with 0 artists when a path to a file is given and not a path to a
    folder.
    :return: None
    """
    artists = getArtistsAlbumsSongs.get_artists(os.getcwd() + "\\dummy_file.txt\\")
    assert len(artists) == 0, "Path to file was given, not to a folder!"


def test_get_artists_3(create_test_env):
    """
    Tests if the check for artists in existing folder that has sub-folders (artists) returns not zero.
    :return: None
    """
    artists = getArtistsAlbumsSongs.get_artists(os.getcwd() + "\\Music")
    assert len(artists) != 0, "Folder is not empty!"


def test_get_artists_4(create_test_env):
    """
    Tests if the check for artists in existing folder that has 3 sub-folders (artists) returns exactly 3 artists.
    :return:
    """
    artists = getArtistsAlbumsSongs.get_artists(os.getcwd() + "\\Music")
    assert len(artists) == 3, "3 artists exists!"


def test_get_artists_5(create_test_env):
    """
    Tests if the check for artists in existing folder that has no sub-folders (artists) returns exactly 0 artists.
    :return:
    """
    artists = getArtistsAlbumsSongs.get_artists(os.getcwd() + "\\Music\\Artist1")
    assert len(artists) == 0, "0 artists exists!"
