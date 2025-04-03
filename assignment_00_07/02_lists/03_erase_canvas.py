import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x, mouse_y = canvas.winfo_pointerxy()
    
    # Calculate the bounding box of the eraser
    left_x = mouse_x - ERASER_SIZE // 2
    top_y = mouse_y - ERASER_SIZE // 2
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find all cells that overlap with the eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For everything that overlaps with our eraser, change its color to white
    for overlapping_object in overlapping_objects:
        canvas.itemconfig(overlapping_object, fill='white')

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Create the grid of blue cells
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    cells = []
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')
            cells.append(cell)

    # Create the eraser
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')
    
    def move_eraser(event):
        # Move the eraser to the mouse pointer position
        canvas.coords(eraser, event.x - ERASER_SIZE // 2, event.y - ERASER_SIZE // 2,
                      event.x + ERASER_SIZE // 2, event.y + ERASER_SIZE // 2)
        # Erase cells in contact with the eraser
        erase_objects(canvas, eraser)

    # Bind the mouse motion to move the eraser
    canvas.bind('<Motion>', move_eraser)

    root.mainloop()

if __name__ == '__main__':
    main()
