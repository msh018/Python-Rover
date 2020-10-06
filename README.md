# Python-Rover

This repository is generic python practice to demonstrate my abilities as a software engineer in the python language.
The goal of the system is to simulate the movement of a 'rover' on a 2d platform with set boundaries. The allowed inputs are:
  L: rotate 90 deg counterclockwise
  R: rotate 90 deg clockwise
  M: move 1 tile forward according to the current rover heading
The base version of this system used text files to give map boundaries, origin (start) position, and the given instructions.
The ouput location and heading was written to a separate file

After completing the base version I wanted to improve my GUI abilities in order to practice further and iterate upon what I already made.
This GUI was made using Python's Tkinter library and allows the user to input custom boundaries and draws the grid the rover will be moving on.
The movement of the rover is simulated moving across the grid.

This file took roughly 10 hours of work to fully produce as a minimum viable product. Several things need improvement in order to be considered a release and I will comment on them here:
  Input sterilization: the gui inputs run on good faith of the user to not input incorrect information. In order to focus on the larger goals I opted to leave this till later
  Commenting: The first part of the program is well documented but the gui and its associated updates need to be explained 
  Readability: I need to refactor a good deal of the GUI code to improve ones ability to follow it. In the attempt to get it running I took shortcuts that are not acceptable
  
I hope this program shows you some of my abilities and the quality and quantity of work I can produce in a short period of time

- Matthew Harmon 2020
