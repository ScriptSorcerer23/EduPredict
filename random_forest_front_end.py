import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the saved Random Forest model and scaler
with open('random_forest_model.pkl', 'rb') as model_file:
    rf_classifier = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Prediction logic for the GUI
def predict():
    try:
        # Ensure numerical values are entered
        raisedhands = int(raisedhands_entry.get())
        visited_resources = int(visited_resources_entry.get())
        announcements_view = int(announcements_view_entry.get())

        # Apply the condition that all inputs must be between 0 and 7
        if (0 <= raisedhands <= 7 and 0 <= visited_resources <= 7 and 0 <= announcements_view <= 7):
            result_label.config(text="Prediction: High-performing (1)")
            return
        
        # Prepare input data
        input_data = np.array([[raisedhands, visited_resources, announcements_view]])

        # Preprocessing: Standardizing numerical features
        input_data[:, :] = scaler.transform(input_data.astype(float))

        # Make prediction using the trained Random Forest model
        prediction = rf_classifier.predict(input_data)[0]

        # Display result
        result_label.config(text=f"Prediction: {'High-performing (1)' if prediction == 1 else 'Low-performing (0)'}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

# GUI Setup
root = tk.Tk()
root.title("Random Forest Performance Prediction")

# GUI Widgets for Numerical Inputs
tk.Label(root, text="Enter Raised Hands:").grid(row=0, column=0, pady=10)
raisedhands_entry = tk.Entry(root)
raisedhands_entry.grid(row=0, column=1)

tk.Label(root, text="Enter Visited Resources:").grid(row=1, column=0, pady=10)
visited_resources_entry = tk.Entry(root)
visited_resources_entry.grid(row=1, column=1)

tk.Label(root, text="Enter Announcements View:").grid(row=2, column=0, pady=10)
announcements_view_entry = tk.Entry(root)
announcements_view_entry.grid(row=2, column=1)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Prediction: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()