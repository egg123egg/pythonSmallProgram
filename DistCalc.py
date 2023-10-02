#calculate distance from velocity and time.
import tkinter as tk
from tkinter import Entry, Label, Button

# Create the main application window
app = tk.Tk()
app.title("Distance Calculator")

# Create and configure GUI elements
label1 = Label(app, text="Speed of motorbike(km/hr)")
entry1 = Entry(app)
label2 = Label(app, text="Time taken (hr,min,sec)")
entry2 = Entry(app)
entry3 = Entry(app)
entry4 = Entry(app)
result_label = Label(app, text="Result:")

# Function to calculate the distance
def calculate_distance():
    try:
        v1= int(entry1.get())
        t2= int(entry2.get())
        t3= int(entry3.get())
        t4= int(entry4.get())
        t5= float((t2)+(t3/60)+(t4/3600))
        distance = v1* t5
        result_label.config(text=f"Distance: {distance:.3f}")
    except ValueError:
        result_label.config(text="Invalid input")
        
calculate_button = Button(app, text="Calculate:km", command=calculate_distance)

# Place GUI elements in the window
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
entry3.pack()
entry4.pack()
calculate_button.pack()
result_label.pack()

# Start the main event loop
app.mainloop()
