#!/usr/bin/python

import os
import hashlib


# custom imports
import fileClassDecleration


def chunkReader(file_reference, chunk_size=1024):
    """ Generator that reads the file in chunks of chunk_size"""
    while True:
        chunk = file_reference.read(chunk_size)
        if not chunk:
            return
        yield chunk


def findDuplicateFiles(path_to_find_duplicate, hash_algo=hashlib.sha1):

    # Dictionary to store unique files
    hashList = {}

    # List which stores duplicate files
    duplicateFiles = []

    for root, directories, filenames in os.walk(path_to_find_duplicate):
        for filename in filenames:

            # getting full path
            absFilePath = os.path.join(root, filename)
            hashobj = hash_algo()

            # calculating hash of the file. To check for duplicate files
            for chunk in chunkReader(open(absFilePath, 'rb')):
                hashobj.update(chunk)

            # cheating a fileID, which is based on the hash of the contents of the file and the filesize
            fileID = (hashobj.digest(), os.path.getsize(absFilePath))

            # Check if duplicate file present
            duplicateFile = hashList.get(fileID, None)
            if duplicateFile:
                print("Duplicate found: %s and %s" % (absFilePath, duplicateFile))
                duplicateFiles.append(absFilePath)
            else:
                hashList[fileID] = absFilePath


if __name__ == '__main__':
    findDuplicateFiles("/home/kush/Downloads/Sorted")