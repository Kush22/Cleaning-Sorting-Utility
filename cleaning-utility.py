#!/usr/bin/python

import os
import getpass
import zipfile
from pathlib import Path


# custom imports
import fileClassDecleration


class CleaningUtility(fileClassDecleration.FileStructure):

    def __init__(self):
        self.username = getpass.getuser()
        self.rootDirectory = '/home/' + self.username + '/'

    def populateFileList(self, file_count):

        # declaring an empty list which stores the top sized files
        topSizedList = []
        sizeOfList = file_count

        for root, directories, filenames in os.walk(self.rootDirectory):
            for filename in filenames:

                # Getting the absolute path
                absFilePath = os.path.abspath(os.path.join(root, filename))

                # Getting parent directory path to be saved in object of file-structure
                parentFilePath = Path(absFilePath).parent

                try:
                    fileSize = os.path.getsize(absFilePath)
                    fileSize = fileSize/(1000*1000.0)
                except Exception as err:
                    continue

                if len(topSizedList) < sizeOfList:
                    tempFileRef = fileClassDecleration.FileStructure(filename, parentFilePath, fileSize)
                    topSizedList.append(tempFileRef)
                    topSizedList.sort(key=lambda x: x.size, reverse=True)

                elif fileSize > fileClassDecleration.FileStructure.get_size(topSizedList[-1]):
                    tempFileRef = topSizedList[-1]
                    tempFileRef.filename = filename
                    tempFileRef.location = parentFilePath
                    tempFileRef.size = fileSize
                    topSizedList.sort(key=lambda x: x.size, reverse=True)

        return topSizedList

    def getFileSize(self, file_path):
        try:
            fileSize = os.path.getsize(file_path)
            fileSize /= (1000 * 1000.0)
            return fileSize
        except Exception as err:
            return 0

    def printFileList(self, file_list):

        print("\n*****************************************************************************")
        print("\n\n%20s %24s %10s %5s %10s\n" % ("Filename", " ", "Size(MB)", " ", "Location"))
        count = 1
        for fileReference in file_list:
            print("%3d) %-40s | %-8.4f | %-50s\n" % (count, fileReference.filename, fileReference.size, fileReference.location))
            count += 1

    def deleteFile(self, file_reference):
        filePath = str(file_reference.location) + '/' + str(file_reference.filename)
        os.remove(filePath)
        return file_reference.size

    def compressFile(self, file_reference):
        filePath = str(file_reference.location) + '/' + str(file_reference.filename)

        # Making the filename of the zip file and storing in same path
        fileNameWithoutExtension = os.path.splitext(filePath)[0]
        zipFilePath = fileNameWithoutExtension + '.zip'

        # Compressing the file (Format of zip.write(path, fileName, type)
        zippedFile = zipfile.ZipFile(zipFilePath, 'w')
        zippedFile.write(filePath, os.path.basename(filePath), compress_type=zipfile.ZIP_DEFLATED)
        zippedFile.close()

        spaceSaved = file_reference.size - self.getFileSize(zipFilePath)
        return spaceSaved

    def sysError(self, message):
        print(message)
        exit(0)

    def scanAndCleanSystem(self, file_count = 10):
        scannedFileList = self.populateFileList(file_count)

        # printing the top sized files
        self.printFileList(scannedFileList)

        print("------------------------------------------------------------------------------------")
        optionCompressDelete = input(
            "Option Available: \n 1. Delete File(s) \n 2. Compress File(s) \n 3. Exit \n\n Input: ")

        if optionCompressDelete == "1":
            # Delete the file(s) provided and give an option to scan again

            self.printFileList(scannedFileList)
            deleteFileList = input("Enter the S.No of file(s) to be deleted (separated by space)\n Input: ")
            deleteFileList = deleteFileList.split(' ')

            totalSavedSpace = 0
            for file in deleteFileList:
                # Checking for index out of bound
                if int(file) > len(scannedFileList) or int(file) < 1:
                    self.sysError("Invalid Index Provided")

                localSavedSpace = self.deleteFile(scannedFileList[int(file) - 1])
                totalSavedSpace += localSavedSpace

                print("File '" + scannedFileList[int(file) - 1].filename + "' Deleted (Space Saved): " + str(
                    localSavedSpace) + " MB")

            print("\nTotal Saved Space: " + str(totalSavedSpace) + " MB")

        elif optionCompressDelete == "2":
            # Compress the file(s) provided and give an option to scan again

            self.printFileList(scannedFileList)
            compressFileList = input(
                'Enter the S.No of file(s) to be Compressed (separated by space). Original will be deleted)\n Input: ')
            compressFileList = compressFileList.split(' ')

            totalSavedSpace = 0
            for file in compressFileList:
                # Checking for index out of bound
                if int(file) > len(scannedFileList) or int(file) < 1:
                    self.sysError("Invalid Index Provided")

                # Computing the saved space
                sizeSaved = self.compressFile(scannedFileList[int(file) - 1])
                totalSavedSpace += sizeSaved

                print("File '" + scannedFileList[int(file) - 1].filename + "' Compressed (Space Saved): " + str(
                    sizeSaved) + " MB")

                # Delete the file once compressed
                self.deleteFile(scannedFileList[int(file) - 1])

            print("\nTotal Saved Space: " + str(totalSavedSpace) + " MB")

        else:
            exit(0)

        continueOption = input("\nDo you want to scan again?(Y/N)\nInput: ")
        if continueOption == "Y" or continueOption == "y" or continueOption == "Yes" or continueOption == "YES":
            self.scanAndCleanSystem(file_count)
        else:
            return


if __name__ == '__main__':
    fileCount = input("Enter the number of files to be displayed in result: ")
    obj = CleaningUtility()
    obj.scanAndCleanSystem(int(fileCount))