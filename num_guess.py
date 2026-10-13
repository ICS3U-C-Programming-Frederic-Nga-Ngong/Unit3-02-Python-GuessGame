#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 2008 18
# Write what this program does.


def main():
    from Constant import CORRECT_ANSWER

    # Get the number from the user
    number = float(input("Enter a number between 0 and 9"))

    # Choosing whether the number is correct or wrong
    if number != CORRECT_ANSWER:

        # Telling the user its answer is not correct
        print("The answer is wrong")

    if number == CORRECT_ANSWER:
        print("the answer is correct")


if __name__ == "__main__":

    main()
