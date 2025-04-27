import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def create_canvas(canvas):
    cells = []
    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        row_cells = []
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            cell = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
            row_cells.append(cell)
        cells.append(row_cells)
    return cells

def erase_cells(event):
    x, y = event.x, event.y
    row = y // CELL_SIZE
    col = x // CELL_SIZE

    if 0 <= row < len(cells) and 0 <= col < len(cells[0]):
     canvas.itemconfig(cells[row][col], fill="white") 

def main():
    global canvas, cells
    root = tk.Tk()
    root.title("Erase Canvas")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.bind("<B1-Motion>", erase_cells)  # Bind left mouse button drag to erase_cells function
    canvas.pack()

    cells = create_canvas(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()

    