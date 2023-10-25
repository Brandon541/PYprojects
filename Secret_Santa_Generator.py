#!/bin/python3
#10OCT2023 @2130
#Secret_Santa_Generator.py

## INSTRUCTIONS ##
''' Each individual should add their name into the script one at a time, when everyone 
    has entered their names into the script click the finish button which will output 
    the files into the directory this scripted is located in. email the files to each 
    person the file is titled for.
    
    If you have any comments or questions please reach out! '''

import tkinter as tk
import random

 # Constructor method is called when an object of the class is created.
 # It initializes the attributes and creates the GUI components.

class SecretSantaGenerator:  #SecretSantaGenerator class, passing the main window as a parameter.
    def __init__(self, master):
        self.master = master # self.master: A reference to the main window of the GUI application.
        self.names = []  #self.names: A list to store the names entered by the users.
        self.master.configure(bg="#ff6666")  
        self.master.title("🎅 Secret Santa Generator 🎁") #self.result_label: A label to display messages about the Secret Santa generation process.
        self.result_label = tk.Label(master, text="", font=("Comic Sans MS", 16, "bold"), bg="#ff6666", fg="#ffffff") 
        self.result_label.pack(pady=20) 
        self.entry_label = tk.Label(master, text="Enter your name:", font=("Comic Sans MS", 14), bg="#ff6666", fg="#ffffff")  #self.entry_label: A label prompting users to enter their names.
        self.entry_label.pack()
        self.name_entry = tk.Entry(master, font=("Comic Sans MS", 14))  #self.name_entry: An entry widget where users can input their names.
        self.name_entry.pack(pady=10)  #self.add_button: A button to add a name to the list.
        self.add_button = tk.Button(master, text="Add Name", command=self.add_name, font=("Comic Sans MS", 14, "bold"), bg="#ffcc00")  #self.add_button: A button to add a name to the list.
        self.add_button.pack(pady=10)
        self.finish_button = tk.Button(master, text="Finish", command=self.generate_secret_santa, font=("Comic Sans MS", 14, "bold"), bg="#ff3333")  #self.finish_button: A button to generate Secret Santa assignments.
        self.finish_button.pack(pady=20)


# This method is called when the "Add Name" button is clicked.
# It retrieves the name entered by the user and adds it to the list of names.
    def add_name(self):
        name = self.name_entry.get()
        if name:
            self.names.append(name)
            self.name_entry.delete(0, tk.END)


# This method is called when the "Finish" button is clicked.
# It checks if there are at least two names, shuffles the list, generates Secret Santa pairs,
# creates text files for each pair, and updates the result_label with the outcome.
    def generate_secret_santa(self):
        if len(self.names) < 2:
            self.result_label.config(text="Please enter at least two names!", fg="red")
        else:
            random.shuffle(self.names)
            pairs = list(zip(self.names, self.names[1:] + [self.names[0]]))
            for pair in pairs:
                sender, recipient = pair
                file_name = f"{sender}_SecretSanta.txt"
                with open(file_name, "w") as file:
                    file.write(f"Dear {sender},\n\nYour Secret Santa recipient is: {recipient}\n\nMerry Christmas!")
            self.result_label.config(text="🎁Secret Santa assignments generated and saved to text files!🎅", fg="#00ff00")

root = tk.Tk()  #tk.Tk(): Creates the main window of the application.
app = SecretSantaGenerator(root) '''app = SecretSantaGenerator(root): Creates an instance of the SecretSantaGenerator class, passing the main window as a parameter. '''
root.mainloop()  '''root.mainloop(): Starts the main event loop of the application, which listens for user interactions.'''
