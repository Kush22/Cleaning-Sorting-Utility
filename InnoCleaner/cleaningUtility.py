#!/usr/bin/python

# standard module imports
import os
import sys
import getpass
import zipfile
import pathlib2 as pathlib

# custom imports
import fileClassDecleration, findDuplicateFIles as findDup, cleaningTempFiles as cleanTemp, \
    fileSortingOnExtension as EfileSort


class CleaningUtility:

    def __init__(self):
        self.username = getpass.getuser()
        self.rootDirectory = '/home/' + self.username + '/'

    def populateFileList(self, scan_path, file_count):
        """
        Scan recursively from the path provided and display top_sized files there
        :param scan_path: Path from where to start scanning
        :param file_count: Number of top_sized files to be returned in the list
        :return: List containing top_sized files (indexed form 1 to file_count)
        """

        # declaring an empty list which stores the top sized files
        topSizedList = []
        sizeOfList = file_count

        for root, directories, filenames in os.walk(scan_path):
            for filename in filenames:

                # Getting the absolute path
                absFilePath = os.path.abspath(os.path.join(root, filename))

                # Getting parent directory path to be saved in object of file-structure
                parentFilePath = pathlib.Path(absFilePath).parent

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
        """
        Returns size of the file provided in path
        :param file_path: Path for which the size needs to be found
        :return: File size in MB's
        """

        try:
            fileSize = os.path.getsize(file_path)
            fileSize /= (1000 * 1000.0)
            return fileSize
        except os.error as err:
            self.sysError(err)

    def printFileList(self, file_list):
        """
        Prints the file list indexed and formatted
        :param file_list: list containing references to files
        :return: None
        """

        print("\n*****************************************************************************")
        print("\n\n%20s %24s %10s %5s %10s\n" % ("Filename", " ", "Size(MB)", " ", "Location"))
        count = 1
        for fileReference in file_list:
            print("%3d) %-40s | %-8.4f | %-50s\n" % (count, fileReference.filename, fileReference.size, fileReference.location))
            count += 1

    def deleteFile(self, file_reference):
        """
        Deletes the file specified in file_reference
        :param file_reference: pointer to fileStructure type files
        :return: size of the file deleted
        """

        filePath = str(file_reference.location) + '/' + str(file_reference.filename)
        os.remove(filePath)
        return file_reference.size

    def compressFile(self, file_reference):
        """
        Compress the file specified in file_reference
        :param file_reference: reference to a file of type fileStructure
        :return: space saved by compressing the file
        """

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
        """
        Prints messages to the console and exits
        :param message: Message to be printed to the console
        :return: None
        """

        print(message)
        exit(0)

    def checkConfirmation(self, option):
        """
        Checks whether the user has checked Yes with its multiple variations
        :param option: entered value to check for
        :return: True if yes selected else False
        """

        if option == "YES" or option == "Yes" or option == "Y" or option == "y" or option == "yes":
            return True
        else:
            return False

    def scanAndCleanSystem(self, scan_path, file_count=10,):
        """
        Scans the system from specified path and provide further functionality
        :param scan_path: path form where to start scan
        :param file_count: files to be displayed while scanning.
        :return: file list and stats on the amount of space saved
        """

        scannedFileList = self.populateFileList(scan_path, file_count)

        # printing the top sized files
        self.printFileList(scannedFileList)

        print("------------------------------------------------------------------------------------")
        optionCompressDelete = input(
            "Option Available: \n 1. Delete File(s) \n 2. Compress File(s)"
            "\n 3. Main Menu \n 4. Exit \n\n Input: ")

        if not optionCompressDelete:
            self.scanAndCleanSystem(scan_path, file_count)

        optionCompressDelete = str(optionCompressDelete)

        # Delete file
        if optionCompressDelete == "1":
            # Delete the file(s) provided and give an option to scan again

            self.printFileList(scannedFileList)
            deleteFileList = input("Enter the S.No of file(s) to be deleted (separated by space)\n Input: ")

            deleteFileList = str(deleteFileList)

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

        # Compress File
        elif optionCompressDelete == "2":
            # Compress the file(s) provided and give an option to scan again

            self.printFileList(scannedFileList)
            compressFileList = input('Enter the S.No of file(s) to be Compressed (separated by space). '
                                     'Original will be deleted)\n '
                                     'Input: ')

            compressFileList = str(compressFileList)

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

        # Main Menu
        elif optionCompressDelete == "3":
            self.main()

        # Exit
        else:
            self.sysError("Exiting the Script. ThankYou!")

        self.main()

    def main(self):
        """
        Driver function for InnoCleaner
        :return: None
        """

        # Creating a reference for the class
        obj = CleaningUtility()

        print("\n------------------------------------------------------------------------------------")
        optionFunctionality = input("Option Available: "
                                    "\n 1. Scan FileSystem to save space"
                                    "\n 2. Sort Files(Based on Extension)"
                                    "\n 3. Find Duplicate Files"
                                    "\n 4. Clean the system up (Clearing Temp Files)"
                                    "\n 5. Exit "
                                    "\n\n Input: ")
        if not optionFunctionality:
            obj.main()

        optionFunctionality = str(optionFunctionality)

        if optionFunctionality == "1":
            fileCount = input("Enter the number of files to be displayed in result (Default 10): ")
            scanPath = input("Enter the path to scan from (Press Enter to scan full path)"
                             "\nPath: ")
            print("This might take some time. Scanning...")

            if not scanPath:
                scanPath = str(self.rootDirectory)
            if not fileCount:
                fileCount = 10

            scanPath = str(scanPath)

            obj.scanAndCleanSystem(scanPath, int(fileCount))

        elif optionFunctionality == "2":
            sourceDirectory = input("Enter path for source directory: ")
            while not sourceDirectory:
                sourceDirectory = input("Enter path for source directory: ")
            sourceDirectory = str(sourceDirectory)

            destinationDirectory = input("Enter path for destination directory: ")
            while not destinationDirectory:
                destinationDirectory = input("Enter path for destination directory: ")
            destinationDirectory = str(destinationDirectory)

            EfileSort.sortOnExtension(sourceDirectory, destinationDirectory)

            print(" Files Moved from '" + sourceDirectory + "' to '"
                  + destinationDirectory + "' and sorted based on extension")

            # Again displaying the menu for further options
            self.main()

        elif optionFunctionality == "3":
            duplicateFilePath = input("Enter the path from which to find duplicate files"
                                      "(Press Enter to scan full system)"
                                      "\nInput: ")

            # If no path provided, scan from the room directory
            if not duplicateFilePath:
                duplicateFilePath = obj.rootDirectory
            duplicateFilePath = str(duplicateFilePath)

            # Check if the path exists or not
            if not os.path.exists(duplicateFilePath):
                obj.sysError("Enter valid path")

            print("Scanning for duplicate file. This might take some time...")
            sizeToBeSaved = findDup.findDuplicateFiles(duplicateFilePath)

            print("You can save " + sizeToBeSaved + " space by cleaning duplicate files")

            # Again displaying the menu for further options
            self.main()

        elif optionFunctionality == "4":

            # For deleting temp files, root permission is required
            if os.geteuid() != 0:
                obj.sysError("Root privileges needed. Run the script as SuperUser")

            confirmationForTempCleaning = input("Confirm to clean the temp files (Y/N)"
                                                "\n Input: ")
            confirmationForTempCleaning = str(confirmationForTempCleaning)

            if obj.checkConfirmation(confirmationForTempCleaning):
                sizeCleaned = cleanTemp.cleanTempFile()
                print("Temp files cleaned. Saved Space: " + sizeCleaned)
            else:
                print("Temp Files cleaning procedure aborted.")

            # Again displaying the menu for further options
            self.main()

        elif optionFunctionality == "5":
            obj.sysError("Exiting the Script. ThankYou!")

        else:
            print("Invalid Option. Enter Again\n")
            self.main()


if __name__ == '__main__':
    CleaningUtility().main()

