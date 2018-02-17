#!/usr/bin/env python

import os
import shutil


def findFileExtension(file_path):
    """
    Find the extension of the file
    :param file_path: path to the file given as file_path
    :return: Extension of file provided as file_path
    """

    for ext in ['.tar.gz', '.tar.bz2']:
        if file_path.endswith(ext):
            # Since these has 2 dots in extension and also removing the dot
            return (file_path[:-len(ext)], file_path[-len(ext):])[1][1:]
    return os.path.splitext(file_path)[1][1:]


def sortOnExtension(sourceDirectory, destinationDirectory):
    """
    Segregate files based on extension
    :param sourceDirectory: path containing the mixed files, whose files needs to be sorted
    :param destinationDirectory: destination where the sorted files need to be moved
    :return: Moves the files form the source directory to destination directory & sorts according to the extension
    """

    # If '/' provided at the end, remove that because later concatenating it
    if sourceDirectory[-1] == "/":
        sourceDirectory = sourceDirectory[:-1]

    for filename in os.listdir(sourceDirectory):

        # Making the path for the file (os.sep is '/' for Unix)
        source = sourceDirectory + os.sep + filename

        fileExtension = os.sep + findFileExtension(source)

        if not os.path.isdir(source):

            # Check if the directory already exists
            if not os.path.isdir(destinationDirectory + fileExtension):
                os.makedirs(destinationDirectory + fileExtension)

            # If file with the same name already exists, notify user (can be asked for confirmation too)
            if os.path.exists(destinationDirectory + fileExtension + os.sep + filename):
                print("File '" + filename + "' already exists at '" + destinationDirectory + "' It will be replaced")

            # Moving the files form the source to the destination
            shutil.move(source, os.path.join(destinationDirectory + fileExtension, filename))


if __name__ == "__main__":
    sortOnExtension("/home/kush/Downloads/Mixed", "/home/kush/Downloads/Sorted")