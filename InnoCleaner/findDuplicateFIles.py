#!/usr/bin/python

import os
import hashlib


# custom imports


def chunkReader(file_reference, chunk_size=1024):
    """
    A generator that reads a file chunk by chunk
    :param file_reference: Reference to the file object
    :param chunk_size: The size of chunk that needs to be read
    :return: The chunk of the file read
    """
    while True:
        chunk = file_reference.read(chunk_size)
        if not chunk:
            return
        yield chunk


def findDuplicateFiles(path_to_find_duplicate, hash_algo=hashlib.sha1):
    """
    Finds the duplicate files from the provided path. This is done by calculating hash of the files
    storing in a dictionary. If any file have the same hash -> duplicate file
    :param path_to_find_duplicate: Specified the root path from where to search for duplicate files
    :param hash_algo: Specifies the hash algo. Default is SHA1
    :return: Prints the path to duplicate and original file from the path_to_find_duplicate
    """

    # Dictionary to store unique files
    hashList = {}

    # List which stores duplicate files
    duplicateFiles = []
    totalSize = 0

    for root, directories, filenames in os.walk(path_to_find_duplicate):
        for filename in filenames:

            # getting full path
            absFilePath = os.path.join(root, filename)

            # Check if (valid) file exists
            if not os.path.isfile(absFilePath):
                continue

            # Checking for file_permission
            accessPerm = os.access(absFilePath, os.R_OK)
            if not accessPerm:
                continue

            hashobj = hash_algo()

            # calculating hash of the file. To check for duplicate files
            try:
                for chunk in chunkReader(open(absFilePath, 'rb')):
                    hashobj.update(chunk)
            except IOError as _:
                continue

            # creating a fileID, which is based on the hash of the contents of the file and the filesize
            fileID = (hashobj.digest(), os.path.getsize(absFilePath))

            # Check if duplicate file present
            duplicateFile = hashList.get(fileID, None)
            if duplicateFile:
                print("Duplicate found: %s and %s" % (absFilePath, duplicateFile))
                totalSize += os.path.getsize(duplicateFile)
                duplicateFiles.append(absFilePath)
            else:
                hashList[fileID] = absFilePath

    return totalSize


if __name__ == '__main__':
    findDuplicateFiles("/home/kush/Downloads/Sorted")