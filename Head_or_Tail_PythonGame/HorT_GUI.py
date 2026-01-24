#import tkinter as tk

# 1. Create the main application window
#root = tk.Tk()
#root.title("Simple GUI")  # Set the window title
#root.geometry("300x150")  # Set the initial window size (width x height)

# 2. Add a Label widget
# The first argument is the parent window (root), the second is the text to display
#label = tk.Label(root, text="Hello, World!", font=("Helvetica", 16))

# 3. Arrange the label using a geometry manager (pack in this case)
#label.pack(pady=50) # pady adds vertical padding so it's centered

# 4. Enter the main event loop
#root.mainloop()


#two type of organisation
#.grid(): Organizes widgets in a table-like structure using row and column numbers (e.g., button.grid(row=0, column=1)).
#.place(): Uses absolute coordinates (x and y) for exact pixel-perfect positioning (e.g., button.place(x=50, y=100)).


import tkinter as tk


def LetsPlay():
    # 1. Clear all current widgets from the window
    for widget in root.winfo_children():
        widget.destroy()

    # 2. Add the new "play" label at the top
    play_label = tk.Label(root, text="play", font=("Arial", 24, "bold"))
    play_label.pack(side=tk.TOP, pady=20)

# Create the main window
root = tk.Tk()
root.title("Text Updater")
root.geometry("500x300")

# 1. The original "Hello World" label
hello_label = tk.Label(root, text="This is a game of head's and Tail", font=("Arial", 16))
hello_label.pack(pady=40)
#hello_label.place(x=50, y=50)

# 2. Add the prompt label
prompt_label = tk.Label(root, text="Do you want to play Yes or No?")
prompt_label.pack(pady=20)

# 3. Add the Entry text box for user input
#entry = tk.Entry(root)
#entry.pack(pady=5)

# 4. Add the button to trigger the update
# The 'command' links the button to the update_text function
# 1. Create a Frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# 2. Pack buttons into the Frame using side=tk.LEFT
Yes_button = tk.Button(button_frame, text="Yes", width=10, command=LetsPlay)
Yes_button.pack(side=tk.LEFT, padx=5)
#Yes_button.pack(pady=10)
#Yes_button.grid(row=1, column=0, padx=5)

No_button = tk.Button(button_frame, text="No", width=10, command=root.destroy)
No_button.pack(side=tk.LEFT, padx=5)
#No_button.pack(pady=10)
#No_button.grid(row=1, column=1, padx=5)

root.mainloop()

