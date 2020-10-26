#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pymusiclibrary import PyMusicLibrary


def test_init_01():
    """

    :return:
    """
    myMusicLibrary = PyMusicLibrary.PyMusicLibrary("C:\\DummyTestFolder")
    artists = myMusicLibrary.get_artists()
    assert len(artists) == 0, "Folder does not exist!"


def test_init_02():
    """

    :return:
    """
    myMusicLibrary = PyMusicLibrary.PyMusicLibrary(os.getcwd() + "\\dummy_file.txt\\")
    artists = myMusicLibrary.get_artists()
    assert len(artists) == 0, "Folder does not exist!"
