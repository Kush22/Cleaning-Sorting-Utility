#!/usr/bin/python

import sys

# Custom Imports
from InnoCleaner import cleaningUtility as cleanUtil


def main():
    """
    Entry Point to InnoCleaner Application
    :return: None
    """
    if sys.version_info < (3, 0):
        sys.exit("Sorry, Python < 3 not supported for now")
    cleanUtil.CleaningUtility().main()
