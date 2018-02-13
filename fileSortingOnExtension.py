#!/usr/bin/env python

import os
import shutil


def findFileExtension(file_path):
    for ext in ['.tar.gz', '.tar.bz2']:
        if file_path.endswith(ext):
            # Since these has 2 dots in extension and also removing the dot
            return (file_path[:-len(ext)], file_path[-len(ext):])[1][1:]
    return os.path.splitext(file_path)[1][1:]


def sortOnExtension(sourceDirectory, destinationDirectory):

    for root, directories, filenames in os.walk(sourceDirectory):
        for filename in filenames:
            source = os.path.abspath(os.path.join(root, filename))

            fileExtension = '/' + findFileExtension(source)

            if not os.path.isdir(source):
                if not os.path.isdir(destinationDirectory + fileExtension):
                    os.makedirs(destinationDirectory + fileExtension)
                shutil.move(source, os.path.join(destinationDirectory + fileExtension, filename))


if __name__ == "__main__":
    sortOnExtension("/home/kush/Downloads/Mixed", "/home/kush/Downloads/Sorted")