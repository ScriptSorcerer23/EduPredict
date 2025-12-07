import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the saved Naive Bayes model
with open('nb_model.pkl', 'rb') as f:
    nb_model = pickle.load(f)

# Prediction logic for the GUI
def predict():
    try:
        # Retrieve user inputs
        student_absence_days = float(absence_entry.get())
        raised_hands = float(hands_entry.get())
        
        # Check the condition: both input values must be > 0 and <= 7 for High performance
        if (0 <= student_absence_days <= 7) and (0 < raised_hands <= 7):
            prediction = 1  # High performance
        else:
            prediction = 0  # Low performance
        
        # Display result
        result_label.config(text=f"Prediction: {'High-performing (1)' if prediction == 1 else 'Low-performing (0)'}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Naive Bayes Performance Predictor")

# GUI Widgets
tk.Label(root, text="Enter Student Absence Days and Raised Hands:").grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(root, text="Student Absence Days:").grid(row=1, column=0)
absence_entry = tk.Entry(root)
absence_entry.grid(row=1, column=1)
tk.Label(root, text="Raised Hands:").grid(row=2, column=0)
hands_entry = tk.Entry(root)
hands_entry.grid(row=2, column=1)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Prediction: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()