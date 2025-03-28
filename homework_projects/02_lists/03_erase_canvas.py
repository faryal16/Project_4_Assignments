# Implement an 'eraser' on a canvas.

import tkinter as tk

# Constants
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
GRID_SIZE = 50  # Size of each cell
ERASER_SIZE = 50  # Size of eraser

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        # Draw blue grid cells
        self.cells = []
        for x in range(0, CANVAS_WIDTH, GRID_SIZE):
            for y in range(0, CANVAS_HEIGHT, GRID_SIZE):
                cell = self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="blue", outline="white")
                self.cells.append(cell)
        
        # Create an eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="black", width=2)
        
        # Bind mouse movement
        self.canvas.bind("<B1-Motion>", self.erase)

    def erase(self, event):
        """Erase cells when the eraser moves over them."""
        x1, y1, x2, y2 = self.canvas.coords(self.eraser)
        self.canvas.move(self.eraser, event.x - x1, event.y - y1)
        
        # Check collision with cells
        for cell in self.cells:
            if self.is_overlapping(cell, x1, y1, x2, y2):
                self.canvas.itemconfig(cell, fill="white")

    def is_overlapping(self, cell, x1, y1, x2, y2):
        """Check if the eraser overlaps with a cell."""
        cx1, cy1, cx2, cy2 = self.canvas.coords(cell)
        return not (x2 < cx1 or x1 > cx2 or y2 < cy1 or y1 > cy2)

# Run the application
root = tk.Tk()
root.title("Eraser Canvas")
EraserCanvas(root)
root.mainloop()
