import os
import BidirectionalStepIterator
import InvalidInstructionException
class Rover:
    """ Rover class contains the necessary definitions for positioning and orientation of the object. It handles all of its own movement and error handling

    Attributes
        x -- x position of the rover on x,y coordinate grid
        y -- y position of the rover on x,y coordinate grid
        orientation -- current orientation of the rover using one of the four cardinal directions
        mapBounds -- [int, int] array bounding the movable coordinates of the rover
        directions -- allowable orientations of the rover, currently four cardinal directions
    
    Methods
        getX -- returns current x position
        getY -- returns current y position
        setX -- sets rovers x position
        setY -- sets rovers y position
        getMapBoundX -- returns x map max boundary value
        getMapBoundY -- returns y map max boundary value
        getOrientation -- returns current rover orientation
        setOrientation -- sets rovers orientation
        updatePosition -- updates rovers x,y coordinates based on positive or negative input values for x and y, throws IndexError for passing out of map boundaries
        writePositionToFile -- writes the x, y, and orientation value to output text file
        writeErrorPositionToFile -- writes the error message to the output text file
        parseInstructions -- handles the parsing of instructions from test file and calls all utility methods to update the necessary class attributes to their correct values, throws InvalidInstructionException when invalid instructions are provided to the rover
    """
    def __init__(self, x, y, orientation, mapBounds):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.mapBounds = mapBounds
        self.directions = ['N', 'E', 'S', 'W']


    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def getMapBoundX(self):
        return self.mapBounds[0]
    
    def getMapBoundY(self):
        return self.mapBounds[1]

    def getOrientation(self):
        return self.orientation

    def setOrientation(self, newOrientation):
        self.orientation = newOrientation

    def updatePosition(self, xUpdate, yUpdate):
        if (self.getX() + xUpdate) > self.getMapBoundX() or (self.getY() + yUpdate) > self.getMapBoundY() :
            raise IndexError('The rover has fallen off the plateu!')
        else: 
            self.setX(self.getX() + xUpdate)
            self.setY(self.getY() + yUpdate)

    def writePositionToFile(self):
        path = os.getcwd()
        f = open(path + "\\Text\\results.txt", "a")
        f.write(str(self.getX()) + " " + str(self.getY()) + " " + self.getOrientation() + "\n")
        f.close()

    def writeErrorPositionToFile(self, message):
        path = os.getcwd()
        f = open(path + "\\Text\\results.txt", "a")
        f.write(message)
        f.close()

    def parseInstructions(self, instructionArray):
        directionIterator = BidirectionalStepIterator.BidirectionalStepIterator(self.directions)
        for instruction in instructionArray:
            if instruction == 'M':
                try: 
                    if self.getOrientation() == 'N':
                        self.updatePosition(0,1)
                    elif self.getOrientation() == 'E':
                        self.updatePosition(1,0)
                    elif self.getOrientation() == 'S':
                        self.updatePosition(0,-1)
                    elif self.getOrientation() == 'W':
                        self.updatePosition(-1,0)
                except InvalidInstructionException.InvalidInstructionException(self.getOrientation, "Invalid orientation provided from orientation list, valid operators are N E S W"): 
                    self.writeErrorPositionToFile("Invalid orientation provided from orientation list, valid operators are N E S W")
            elif instruction == 'L':
                self.setOrientation(directionIterator.prev(self.directions.index(self.getOrientation())))
            elif instruction == 'R':
                try:
                    self.setOrientation(directionIterator.next(self.directions.index(self.getOrientation())))
                except InvalidInstructionException.InvalidInstructionException(instruction, "Invalid instruction provided from instructions list, valid operators are L R and M"):
                    self.writeErrorPositionToFile("Invalid instruction provided from instructions list, valid operators are L R and M")
    
    def parseInstruciton(self, instruction):
        directionIterator = BidirectionalStepIterator.BidirectionalStepIterator(self.directions)
        if instruction == 'M':
            try: 
                if self.getOrientation() == 'N':
                    self.updatePosition(0,1)
                elif self.getOrientation() == 'E':
                    self.updatePosition(1,0)
                elif self.getOrientation() == 'S':
                    self.updatePosition(0,-1)
                elif self.getOrientation() == 'W':
                    self.updatePosition(-1,0)
            except InvalidInstructionException.InvalidInstructionException(self.getOrientation, "Invalid orientation provided from orientation list, valid operators are N E S W"): 
                self.writeErrorPositionToFile("Invalid orientation provided from orientation list, valid operators are N E S W")
        elif instruction == 'L':
            self.setOrientation(directionIterator.prev(self.directions.index(self.getOrientation())))
        elif instruction == 'R':
            try:
                self.setOrientation(directionIterator.next(self.directions.index(self.getOrientation())))
            except InvalidInstructionException.InvalidInstructionException(instruction, "Invalid instruction provided from instructions list, valid operators are L R and M"):
                self.writeErrorPositionToFile("Invalid instruction provided from instructions list, valid operators are L R and M")