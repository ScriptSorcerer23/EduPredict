import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np



# Load the saved ANN model
with open('ann_model.pkl', 'rb') as f:
    ann_model = pickle.load(f)



# Prediction logic for the GUI
def predict():
    try:
        # Retrieve user inputs
        parent_answering_survey = parent_answering_survey_var.get()
        parent_school_satisfaction = parent_school_satisfaction_var.get()

        # Ensure both radio buttons are selected
        if not parent_answering_survey or not parent_school_satisfaction:
            messagebox.showerror("Input Error", "Please select all options.")
            return

        raisedhands = int(raisedhands_entry.get())
        visited_resources = int(visited_resources_entry.get())
        announcements_view = int(announcements_view_entry.get())

        # Calculate total impact
        total_impact = raisedhands + visited_resources + announcements_view

        # Determine the impact based on the sum of inputs
        if total_impact <= 50:
            impact_message = "The impact of parents answering survey is low on student performance."
        elif total_impact <= 100:
            impact_message = "The impact of parents answering survey is medium on student performance."
        else:
            impact_message = "The impact of parents answering survey is high on student performance."

        # Display result
        result_label.config(text=impact_message)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

# GUI Setup
root = tk.Tk()
root.title("Performance Prediction")

# GUI Widgets for Radio Buttons
tk.Label(root, text="Select Parent Answering Survey:").grid(row=0, column=0, pady=10)
parent_answering_survey_var = tk.StringVar(value=' ')  # Set default value as empty
tk.Radiobutton(root, text="Yes", variable=parent_answering_survey_var, value='Yes').grid(row=0, column=1)
tk.Radiobutton(root, text="No", variable=parent_answering_survey_var, value='No').grid(row=0, column=2)

tk.Label(root, text="Select Parent School Satisfaction:").grid(row=1, column=0, pady=10)
parent_school_satisfaction_var = tk.StringVar(value=' ')  # Set default value as empty
tk.Radiobutton(root, text="Good", variable=parent_school_satisfaction_var, value='Good').grid(row=1, column=1)
tk.Radiobutton(root, text="Bad", variable=parent_school_satisfaction_var, value='Bad').grid(row=1, column=2)

# GUI Widgets for Numerical Inputs
tk.Label(root, text="Enter Raised Hands:").grid(row=2, column=0, pady=10)
raisedhands_entry = tk.Entry(root)
raisedhands_entry.grid(row=2, column=1)

tk.Label(root, text="Enter Visited Resources:").grid(row=3, column=0, pady=10)
visited_resources_entry = tk.Entry(root)
visited_resources_entry.grid(row=3, column=1)

tk.Label(root, text="Enter Announcements View:").grid(row=4, column=0, pady=10)
announcements_view_entry = tk.Entry(root)
announcements_view_entry.grid(row=4, column=1)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=5, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Prediction: ")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()