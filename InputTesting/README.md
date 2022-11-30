# Lab Activity #7 – Practicing control and exception handling

*NOTE: This lab is not a team activity an may be completed individually.*

## Goals

Practice using standard Python control statements, including the exception
handling mechanism.

### Prerequisites

This lab assumes that you have:

- read Chapters 7 and 8 in our textbook;
- basic experience with Python/IDLE and Git;
- fetched and merged the Lab07 instructions from the upstream repository.

### Skills Acquired/Reinforced Upon Completion

- Define and call functions.
- Use looping and branching control statements.
- Handle exceptions that may arise.

## Base program

In this lab, you will write a program that asks the user to enter a series
of test results, which include a student CWID number and raw test score.

- Write a function named `read_test_result` that prompts the user to enter
    a single test result and reads the input as a string (the student CWID)
    and an integer (the raw score). This function should return the ID and
    test score as a *pair*, as in `(cwid,score)`. If the user enters a blank
    line, then indicate no result by returning an empty string for the CWID
    and zero for the raw score.
- Write a `main` function that loops indefinitely, each time calling the
    `read_test_result` function to get the user input and then adding the
    returned data to a list. If the value returned by the function above
    indicates no test result, then `break` out of the loop and resume the rest
    of the main function.
- Finally, loop through your list of test results and print them to the
    screen terminal.

When you are satisfied that your program works as intended, *commit* and *push*
your work. If it does not, then try to figure out what's wrong and fix it.
Finally, continue on to the next section.

## Adding exception handling

If you test your program with invalid input, such as only one value in the
input line or a non-numeric value for the score, it will crash. Let's make
the program more robust by checking for and handling such errors.

- Add a `try`-`except` control statement to your `main` function to handle
    any `ValueError`s that may be raised by your `read_test_result` function.
    Upon a `ValueError`, print a message to the user indicating that they did
    not enter valid input. The loop should then simply continue, prompting for
    input again.

Test your program with intentionally invalid inputs to ensure that it actually
works as expected. If not, then try to figure out what's wrong and fix it. Once
you are satisfied that everything works, *commit* and *push* your changes.

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `Labs/Lab07` subfolder of your repository must contain a `control.py`
    script that meets the requirements above.
2. Your scripts must contain the name of the lab activity, your full name, and
    the date in a comment at the top.
3. Your repository's commit history must show at least three different commits
    for your `control.py` file.
4. All of the above must be pushed to GitHub so that I can see it.

Congratulations! You've completed Lab #7.

