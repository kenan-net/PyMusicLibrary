#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
from pymusiclibrary import PyMusicLibrary


@pytest.fixture
def create_test_env():
    """

    :return:
    """
    # Create dummy folder structure
    cwd = os.getcwd()
    os.makedirs(cwd + "\\Music\\Artist1\Album1", exist_ok=True)
    os.makedirs(cwd + "\\Music\\Artist1\Album2", exist_ok=True)
    os.makedirs(cwd + "\\Music\\Artist1\Album3", exist_ok=True)

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


def test_get_albums_1(create_test_env):
    """

    :return:
    """
    myMusicLibrary = PyMusicLibrary.PyMusicLibrary(os.getcwd() + "\\Music\\")
    albums = myMusicLibrary.get_albums("Artist1")
    assert len(albums) == 3, "There are 3 albums of Artist 1"
