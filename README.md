# PyMusicLibrary
Idea is to create a Python based script that takes a root folder, and following simple conventions extracts artists, 
albums and songs stored inside that folder.
PyMusicLibrary provides following features:
- searching for a song
- searching for an album 
- searching for an artist
- providing list of artists
- providing list of albums
- providing list of songs
- list of albums for 1 artist
- list of songs for 1 album
- list of songs for 1 artist

## Requirements - Folder structure
File structure behind is organized in folders where the whole music library is stored in a single folder (Level 0) with
multiple sub-folders and files.
Folders are organized in levels where the root folder is level 0 and every folder inside it is considered as level 1.
Every subsequent folder increases the level by +1.
Files within a folder don't increase a level.
Only files within Level 2 are considered as actual songs.
An example of folder structure that is expected by the PyMusicLibrary
Level 0 - Music Library root folder. Contains folders whose names are considered to be artist names.
Level 1 - Artist folder. Contains folders whose names are considered to be album names. 
Level 2 -  Album folder. Contains song files and optionally folders.
Level 3 - contains some album specific files that are not songs.

## Requirements - Folder names conventions


## Requirements - Functional
Music library contains information about the artists, their albums and belonging songs.
Artists are identified by their name.
1 artist can have multiple albums where an album can have 1 or more songs.
Albums are identified by their name, and they also have a year of publishing.
