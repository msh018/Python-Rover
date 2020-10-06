import os
import Rover
import Window
import tkinter as tk
from PIL import Image, ImageTk
def main():
    """
    path = os.getcwd()
    f = open(path + "\\Text\\instructions.txt", 'r')
    instructionSet = f.read()
    f.close()
    instructionSet = instructionSet.replace(" ", "")
    instructionSet = instructionSet.splitlines()
    #set up rover object with class attributes from file
    rover = Rover.Rover(int(instructionSet[1][0]), int(instructionSet[1][1]), instructionSet[1][2], [int(instructionSet[0][0]), int(instructionSet[0][1])])
    #split apart instructions and prepare them for further rover runs, remove the play area bounds
    instructionSet.pop(0)
    #set arrays for origins and movement sets and populate them for further runs
    origins = []
    movementSets = []
    for i in range(0, len(instructionSet)):
        if i%2 == 1:
            movementSets.append(instructionSet[i])
        else:
            origins.append(instructionSet[i])

    #iterate over movement sets and run rover tests
    for i in range(0, len(movementSets)):
        #at the beginning of each run set the new origin location for new test
        rover.setX(int(origins[i][0]))
        rover.setY(int(origins[i][1]))
        rover.setOrientation(origins[i][2])
        #run new instruction set
        rover.parseInstructions(movementSets[i])
        #after instructions are exhausted, write the final position to file
        rover.writePositionToFile()
    """
    root = tk.Tk()
    window = Window.Window(root)
    window.getWindow().mainloop()



if __name__ == "__main__":
    main()


"""
read in instructions
create rover object
read instructions to rover and allow it to run through them
print final position to file
iterate and run through further tests
print further tests to file
"""