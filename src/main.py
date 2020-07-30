#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script to run a few Python3 basic functions, only to check whether pylint is working or not.

Since this is only a basic script to check wheter pylint is running well or not, documentation may
not be very detailed.
"""


from datetime import datetime

import functions

def main():
    """
    main() function, just to call a few basic functions.
    """

    print("Basic software to test pylint.\n")

    condition = False
    while not condition:
        if not condition:
            print("Testing if/else inside a loop!\n")

            condition = True

        else:
            print("Should never reach here!\n")

    today = datetime.today().strftime("%d/%m/%Y")
    print("Today is: {:s}\n".format(today))

    result = "This string was written by the main()!\n"
    result = functions.test_print()
    print(result)


if __name__ == "__main__":
    main()
