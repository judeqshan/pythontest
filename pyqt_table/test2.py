import tkinter as tk
from tkintertable.Tables import TableCanvas

# Create the main window
root = tk.Tk()
root.title('Tkinter Table Example')

# Create a table using TableCanvas
table = TableCanvas(root)

# Define the table's headers and data
data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [4.5, 6.7, 8.9]}
table.createTable(data, cellwidth=100, cellbackgr='lightblue')

# Pack the table
table.show()

# Run the main loop
root.mainloop()