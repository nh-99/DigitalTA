# DigitalTA

## Introduction
This software was developed to automate the process of grading coding homework assigments.
It will automatically feed input into a program and get the output to display to
the person in charge of grading the assignment. From there, the grader can add
a grade to the homework and the person who uploaded it can see it.

## How to use
*NOTE:* You must be running some sort of Unix system to use this software.

Download the source code and install the requirement with `pip install -r requirements.txt`.
Then, run it with `python app.py`. It will be running at [http://localhost:5000](http://localhost:5000).
You can upload homework there and visit the other routes to test the rest of the functionality.

## Future goals
Ideally, this can eventually completely automate the homework grading process,
so that as soon as a user uploads their homework they already have a grade for it.
The grade could later be manually adjusted based on the amount of work done (even
if it doesn't return the correct output), but most people would be able to get an
idea of what their grade is on a homework assignment. It would reduce a lot of
the workload of the grader.

## Todo

- [ ] Secure the application
- [ ] Add authentication and registration
- [ ] Work on user friendliness
- [ ] Add expected output to database model
- [ ] Check for expected output and give homework a grade automatically
- [ ] Make it easier to add homework checks
