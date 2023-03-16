# Aliasing

## The concepts covered in this lab include:

1. Object-Oriented Programming in Python.
2. Class creation and initialization.
3. Data attributes and instance methods.
4. Using lists, sets, and dictionaries in Python.
5. String representation of objects.

## Brief summary

This lab covers the concept of creating classes and working with objects in Python to form and schedule clubs for students in ASUO (The Associated Students of the University of Oregon). The lab includes creating three classes: `Student`, `Club`, and `ASUO`, and implementing various methods for scheduling meetings and finding common time slots for clubs. The lab also covers the concept of type checking and type hints in Python, and the use of dictionaries and sets in Python.

## Plan for the lab

1. Create a class `Student` that has a constructor which takes in a `name` and `interests` list as arguments. It also has two instance variables: `freetimes` (a set of available time slots for the student) and `meetings` (a list of time slots for all the meetings that a student has scheduled). Implement a method `schedule_meeting()` to scedule a meeting for a student given a time slot.
2. Create a class `Club` that has a constructor which takes in the name of the club as an argument. It has two instance variables: `members` (a list of members of the club) and `meeting_time` (a meeting time so that all members can attend). Implement functions `join()` to add a student to the member list, `find_common_time()` to find the common time slot for all members from their freetimes to attend, and `schedule()` to schedule the club meeting for all of its members.
3. Create a class `ASUO` that has a constructor with two instance variables: `students` (a list of students) and `clubs` (a list of clubs). Implement functions `enroll()` to add a student to the list of students, `form_clubs()` to form clubs, and `schedule_clubs()` to schedule clubs. Implement a function `print_club_schedule()` to print out the schedule of each club.
4. Add test code to create an instance of the ASUO class, enroll some students, form and schedule clubs, and print out the club schedule.

Look in doc/HOWTO.md for detailed directions.
