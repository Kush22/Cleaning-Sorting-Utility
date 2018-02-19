#!/usr/bin/python

import os
import tempfile

# Custom Imports
import cleaningUtility


def cleanTempFile():
    """

    Gets the tempfiles and deletes them
    :return: Temp files removed and amount of space saved
    """

    # Getting the temp-file directory using tempfile module
    tempDirectoryPath = tempfile.gettempdir()

    # Creating an object to cleaningUtility class to use its getSize module
    cleaningUtilityObj = cleaningUtility.CleaningUtility()

    totalCleanedSize = 0

    # for each file in the temp directory
    for root, directories, filenames in os.walk(tempDirectoryPath):
        for filename in filenames:

            try:
                pathToTempFile = os.path.join(root, filename)

                # Check if valid file
                if not os.path.isfile(pathToTempFile):
                    continue

                # Calculating cleaned size stats
                currentCleanSize = cleaningUtilityObj.getFileSize(pathToTempFile)
                totalCleanedSize += currentCleanSize

                # Deleting the temp file
                os.remove(pathToTempFile)
            except IOError as _:
                continue

    # Return the amount of space that can be saved
    return totalCleanedSize


if __name__ == '__main__':
    sizeClean = cleanTempFile()
    print("Space Cleaned %d" % sizeClean)
