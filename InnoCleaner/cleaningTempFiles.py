#!/usr/bin/python

import os
import tempfile

# Custom Imports
import cleaningUtility


def cleanTempFile():
    """

    Gets the tempfiles and deletes them
    :return: Temp files removed
    """

    # Getting the temp-file directory using tempfile module
    tempDirectoryPath = tempfile.gettempdir()

    # Creating an object to cleaningUtility class to use its getSize module
    cleaningUtilityObj = cleaningUtility.CleaningUtility()

    totalCleanedSize = 0
    for root, directories, filenames in os.walk(tempDirectoryPath):
        for filename in filenames:

            pathToTempFile = os.path.join(root, filename)

            # Calculating cleaned size stats
            currentCleanSize = cleaningUtilityObj.getFileSize(pathToTempFile)
            totalCleanedSize += currentCleanSize

            # Deleting the temp file
            os.remove(pathToTempFile)

    return totalCleanedSize


if __name__ == '__main__':
    sizeClean = cleanTempFile()
    print("Space Cleaned %d" % sizeClean)
