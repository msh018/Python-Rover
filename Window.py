import tkinter as tk
from PIL import Image, ImageTk
import Rover
import time

class Window:
    def __init__(self, window):
        self.window = window
        self.boundX = 0
        self.boundY = 0
        self.roverImg = 0
        self.startFrame()

    def getWindow(self):
        return self.window
    
    def setWindow(self, window):
        self.window = window

    def getBoundX(self):
        return self.boundX

    def setBoundX(self, newX):
        self.boundX = int(newX)
    
    def getBoundY(self):
        return self.boundY

    def setBoundY(self, newY):
        self.boundY = int(newY)

    def startFrame(self):
        boundXVar = tk.StringVar()
        boundYVar = tk.StringVar()

        tk.Label(self.window, text="Welcome to Rover Explorer!", padx=10, pady=10).grid(row=0, columnspan=4)
        tk.Label(self.window, text= "Input map boundaries: ", pady=10).grid(row=1)
        tk.Label(self.window, text="x").grid(row=1, column=2)
        boundX = tk.Entry(self.window, width=5, textvariable = boundXVar)
        boundY = tk.Entry(self.window, width=5, textvariable = boundYVar)
        boundX.grid(row=1, column=1)
        boundY.grid(row=1, column=3)

        def submitCallback():
            self.setBoundX(boundXVar.get())
            self.setBoundY(boundYVar.get())
            self.gridFrame()

        nextButton = tk.Button(text="Submit", command=submitCallback, padx=10, pady=10)
        nextButton.grid(row=2, column=3)
    
    def gridFrame(self):
        xStartPosVar = tk.StringVar()
        yStartPosVar = tk.StringVar()
        instructionsVar = tk.StringVar()
        directionVar = tk.StringVar()

        #gridFrame = tk.Tk()
        gridFrame = tk.Toplevel(self.window)
        roverImg = ImageTk.PhotoImage(Image.open("rover(100x100).jpg"))
        self.roverImg = roverImg
        self.setWindow(gridFrame)

        #canvas def
        c = tk.Canvas(self.window, height=(self.getBoundY()*100), width=(self.getBoundX()*100), bg='white')
        c.grid(row=0, column=0, columnspan=4)
        self.createGrid(c)

        #row 1 col 0 label 
        tk.Label(self.window, text="Start Position").grid(row=1, column=0, columnspan=2)

        #row 2 col 0 frame with pos input
        startInputFrame = tk.Frame(self.window)
        startInputFrame.grid(row=2, column=0, columnspan=2)

        tk.Label(startInputFrame, text="X:", pady=10).pack(side='left')
        xStartPosEntry = tk.Entry(startInputFrame, width=5, textvariable = xStartPosVar)
        xStartPosEntry.pack(side='left')
 
        tk.Label(startInputFrame, text="Y:").pack(side='left')
        yStartPosEntry = tk.Entry(startInputFrame, width=5, textvariable = yStartPosVar)
        yStartPosEntry.pack(side='left')

        tk.Label(startInputFrame, text="Heading:").pack(side='left')
        directionEntry = tk.Entry(startInputFrame, width=5, textvariable = directionVar)
        directionEntry.pack(side='left')

        #row 1 col 2 instruction label
        tk.Label(self.window, text="Instructions").grid(row=1, column=2)

        #row 2 col 2 instructions entry
        instructionsEntry = tk.Entry(self.window, width=10, textvariable = instructionsVar)
        instructionsEntry.grid(row=2, column=2)

        def runCallback():
            xStart = int(xStartPosEntry.get())
            yStart = int(yStartPosEntry.get())
            dirStart = directionEntry.get()
            instructions = instructionsEntry.get()
            self.runTest(xStart, yStart, dirStart, instructions, c)

        #row 1 col 3 run button
        runButton = tk.Button(self.window, text="Run!", command=runCallback, padx=10, pady=10)
        runButton.grid(row=1, column=3, rowspan=2)

    def runTest(self, xStart, yStart, dirStart, instructions, canvas):
        rover = Rover.Rover(xStart, yStart, dirStart, [self.getBoundX(), self.getBoundY()])
        imgID = canvas.create_image((xStart-1)*100, (yStart-1)*100, image=self.roverImg, anchor='nw')
        self.window.update()
        for i in instructions:
            time.sleep(1)
            rover.parseInstruciton(i)
            newX = rover.getX()
            newY = rover.getY()
            xDelta = ((newX-1)*100) - canvas.coords(imgID)[0]
            yDelta = ((newY-1)*100) - canvas.coords(imgID)[1]
            print("xD: " + str(xDelta) + " yD: " + str(yDelta))
            canvas.move(imgID, xDelta, yDelta)
            self.window.update()
        


    def createGrid(self, canvas):
        rows = self.getBoundX()
        columns = self.getBoundY()
        canvas.delete('grid_line')

        for i in range(0, (rows*100), 100):
            canvas.create_line([(i,0),(i,(rows*100))], tag='grid_line')
        
        for i in range(0, (columns*100), 100):
            canvas.create_line([(0,i),((columns*100),i)], tag='grid_line')

    

        
    