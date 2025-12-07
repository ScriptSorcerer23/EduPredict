import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the saved Gradient Boosting model and Scaler
with open('gb_model.pkl', 'rb') as f:
    gb_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Prediction logic for the GUI
def predict():
    try:
        # Retrieve user inputs
        student_absence_days = float(absence_entry.get())
        
        # Apply condition for performance prediction based on absence days
        if 0 <= student_absence_days <= 7:
            prediction = 1  # High-performing
        else:
            prediction = 0  # Low-performing
        
        # Display result
        result_label.config(text=f"Prediction: {'High-performing (1)' if prediction == 1 else 'Low-performing (0)'}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numerical value for Student Absence Days.")

# GUI Setup
root = tk.Tk()
root.title("Performance Predictor")

# GUI Widgets
tk.Label(root, text="Enter Student Absence Days:").grid(row=0, column=0, pady=10)
absence_entry = tk.Entry(root)
absence_entry.grid(row=0, column=1, pady=10)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=1, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Prediction: ")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
