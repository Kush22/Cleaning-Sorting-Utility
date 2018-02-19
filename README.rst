Welcome to InnoCleaner
======================

This is a Cleaning & File Sorting Utility which is developed by me as a
submission for **Innovaccer HackerCamp 18** under the assignment titled
**Infrastructure Engineering Assignment.**

The problem statement for the implemented project is: `Infrastructure
Engineering
Assignment <https://drive.google.com/file/d/1azvXBMhBmhiFRDDTR3cDegJUNTxvg3ak/view>`__

**Installation**
==========================

To install run the command:
pip install InnoCleaner

To Execute:

In **normal user mode**:
    Command: InnoCleaner
-With **super-user privileges**:
    -Command: sudo InnoCleaner

**Requirements**
==========================

- Unix Platform
- Python Installation with version >= 2.7

**Required Functionality**
==========================

-  Scan the specified path in the file system to display top 10 largest
   sized files.
-  Move the files on Desktop based on extension and save them in
   Documents folder clubbed in folders according to extension.

Now let us describe what InnoCleaner is:

InnoCleaner is a UNIX based CLI cleaner utility that gives the user a
tool to perform disk cleanup and related capabilities.

**Functionality Implemented**
=============================

-  Scan and Save Space : Given the path and number of files to list, it
   can recursively scan the path to display the largest sized
   files(Further operations include):

   -  Delete file(s):

      -  For this choose the corresponding option and specify the
         file(s) (space separated if multiple)

   -  Compressing file(s):

      -  Similar to compression, specify the file(s) (space separated if
         multiple)

   -  Stats about the amount of space saved are then displayed.

-  Sorting : Given the path of a *source* and *destination*, the files
   in *source* folder are sorted according to extension and saved
   folder-wise in the destination location

-  Duplicity : Given a path, InnoCleaner recursively scans the path for
   detecting duplicate files.

-  Cleanup : On selecting the Cleanup Option, the temp files are
   cleaned.

**Usage Guidelines**
=============================

-  After displaying the scanned files, when you choose the options to delete/compress, again the list of
   files will be displayed from which you can choose the files to perform the required action on.

-  If using python < 3, specify the path to directories and space separated options in double quotes
   e.g. ("/home/user_name/" & "1 2 3").

-  For cleaning temp files run the program in Super User mode, because normal user does not have permission
   to access /tmp folder.


**Future Improvements**
=======================

No project is complete without a list of improvements & InnoCleaner is
no exception. The list of improvements can be never ending:

-  Right now the module is tested only for UNIX environments. Test and
   make the module cross-platform compatible.

-  Separate compression algorithms work better with different types of
   files. So have a list of compression algorithms corresponding to the file
   extension and by checking the file extension, use the best possible
   to save most space.

-  Just detecting duplicate files isn't of much use. So provide option
   to clean the duplicate files too. Since a lot of files may be
   duplicated, first display only limited number of files, ask for any
   deletion and then proceed further. Also, provide an option to clean
   all duplicate files (if the user does not want to select explicitly).

-  Detection of obsolete files : Based on the modified dates, obsolete
   files may be displayed to be cleaned up or compressed.

-Contact: In case of any query you can always contact me at
kushagra.gupta@students.iiit.ac.in and I will be happy to help.

Happy Coding!

Developer **Kushagra Gupta**, IIIT Hyderabad, Bakul Nivas, Gachibowli
Hyderabad - 500032 Telangana, India
