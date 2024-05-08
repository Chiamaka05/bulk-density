from tkinter import *


# Using tkinter for the GUI phase because it is easy.

def bulk_density():
    try:
        mass = int(mass_input.get())
        volume = int(volume_input.get())
        if volume <= 0:
            raise ValueError("Volume must be a positive number")
        calculate_bulk_density = mass / volume
        result_label.config(text=f"{calculate_bulk_density}")
    except ValueError:
        print("Error: Please enter valid numerical values for mass and volume.")


window = Tk()
window.title("BULK DENSITY CALCULATOR")
window.config(padx=20, pady=20, background="dark gray")
window.minsize(width=500, height=300)

mass_input = Entry(width=12)
# This program calculates the bulk density of a material. To calculate the bulk density of any material, input the necessary values"
mass_input.grid(column=2, row=0)

mass_label = Label(text="Enter the value in kg: ", font=("Helvetica", 12))
mass_label.grid(column=1, row=0, padx=15, pady=15)

volume_input = Entry(width=12)
volume_input.grid(column=2, row=1)

volume_label = Label(text="Enter the value in m3: ", font=("Helvetica", 12))
volume_label.grid(column=1, row=1, padx=15, pady=15)

result_label = Label(text="0", font=("Helvetica", 12))
result_label.grid(column=2, row=3, padx=15, pady=15)

convert_label = Label(text="kg/m3", font=("Helvetica", 12))
convert_label.grid(column=4, row=3, padx=15, pady=15)

calculate_button = Button(text="Calculate", command=bulk_density, bg="gray", fg="black")
calculate_button.grid(column=1, row=4)

window.mainloop()
