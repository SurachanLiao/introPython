**See the video for detailed walkthrough.** Contact me if help is needed.


# 1 Get started with Python

Before we start coding python, we need text editor that provide good

## Installing text editor: VSCode

Other text editors also work well. VSCode is recommended for beginner since it is free and widely used. 

Follow the link to [Install page for Windows and Mac](https://code.visualstudio.com/download)

## Installing Python 

The lasted version of Python is recommended. At the moment, 3.11 is the lastest.

Follow the link to [Download the lastest Python for Windows and Mac](https://www.python.org/downloads/)

## Terminal and ipython

After Python is installed, we need start the Python up! We need Terminal and ipython to run our first program.

What is Terminal?
The terminal is an interface that lets you access the command line. This is simply the browsing through computer without having an animated interface.

Common and useful comnands
- cd  : (change directory) takes a directory name as an argument, and switches into that directory.
- ls  : (list) lists all files and directories in the working directory
- pwd : (print working directory) It shows the current location or directory.
These two commands are nessesary for this lesson.

### For Windows
- Search for a program called "Terminal"
- In the command line type
  '''
  cd .\AppData\Local\Programs\Python\Python311\Scripts\
  pip3 install IPython
  ipython
  '''
- Now, we have a working Python Integrated Development Environment(IDE).
- Try simple commands.
  ```
  2+2
  2+2*(3+6)
  ```
## Running the first Python program: "Hello World!"
- Open VSCode
- On the top left, click File. Then, New Text File.
- Type 
  print("Hello World!")
- Save As the file with the name "HelloWorld.py", without the quatations. Select the location to be at Desktop.
- Reopen the "Terminal"
- In the command line type
  ```
  cd .\AppData\Local\Programs\Python\Python311\Scripts\
  ipython
  cd
  cd OneDrive/Desktop/
  run HelloWorld.py
  ```
- Hello World! should appear on the screen.
- We are successfully create and run our first program.

## Add PATH to allow using ipython at any directory
- [This link explains how to add PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)
- C:\Users\surachanliao\AppData\Local\Programs\Python\Python311\Scripts\ 
should be the location that is added to the path(replace "surachanliao" with name of the computer).

## Try the first problem sets
- Download the ls1pr1.py
- Open it in the VSCode and follow the instructions
- The sample solutions are available in ls1pr1_sol.py

[Reference to HMC CS5 course](https://www.cs.hmc.edu/twiki/bin/view/CS5/Orientation)


