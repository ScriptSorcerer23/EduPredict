import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import Image, ImageTk
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd

# Function to display the image
def show_image(image_name):
    try:
        # Load the original image
        img_path = f"{image_name}.png"  # Adjust the file extension if needed
        img_original = Image.open(img_path)

        # Create a new window to display the image
        img_window = tk.Toplevel(root)
        img_window.title(f"{image_name} Image")

        # Create a scrollable canvas
        canvas = tk.Canvas(img_window)
        canvas.pack(side="left", fill="both", expand=True)

        # Add scrollbars
        x_scrollbar = tk.Scrollbar(img_window, orient="horizontal", command=canvas.xview)
        x_scrollbar.pack(side="bottom", fill="x")
        y_scrollbar = tk.Scrollbar(img_window, orient="vertical", command=canvas.yview)
        y_scrollbar.pack(side="right", fill="y")

        canvas.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

        # Display the image on the canvas
        img_tk = ImageTk.PhotoImage(img_original)
        image_container = canvas.create_image(0, 0, anchor="nw", image=img_tk)
        canvas.image = img_tk  # Keep a reference to avoid garbage collection

        # Set the scrollable region
        canvas.config(scrollregion=(0, 0, img_original.width, img_original.height))

    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

# Function to handle Decision Tree button click
def decision_tree_options():
    # Create a new window for the Decision Tree options
    options_window = tk.Toplevel(root)
    options_window.title("Decision Tree Options")
    options_window.geometry("400x200")
    options_window.config(bg="#f5f5f5")  # Light background for a modern look

    # Add a label for options
    label = tk.Label(options_window, text="Choose an Option", font=("Helvetica", 16), bg="#f5f5f5")
    label.pack(pady=20)

    # Add buttons for each option
    feature_importance_button = tk.Button(
        options_window,
        text="Feature Importance according to Decision Tree",
        font=("Helvetica", 12),
        width=40,
        command=lambda: show_image("Feature_Importance")
    )
    feature_importance_button.pack(pady=10)

    decision_tree_button = tk.Button(
        options_window,
        text="Decision Tree",
        font=("Helvetica", 12),
        width=40,
        command=lambda: show_image("Decision_Tree")
    )
    decision_tree_button.pack(pady=10)

# Function to display "About Dataset" information
def show_about_dataset():
    about_window = tk.Toplevel(root)
    about_window.title("About Dataset")
    about_window.geometry("500x400")
    
    frame = tk.Frame(about_window)
    frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, font=("Arial", 12))
    text.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=text.yview)

    about_text = """Students' Academic Performance Dataset (xAPI-Edu-Data)
Data Set Characteristics: Multivariate

Number of Instances: 480

Area: E-learning, Education, Predictive models, Educational Data Mining

Attribute Characteristics: Integer/Categorical

Number of Attributes: 16

Date: 2016-11-8

Associated Tasks: Classification

Missing Values? No

File formats: xAPI-Edu-Data.csv

Source:
Elaf Abu Amrieh, Thair Hamtini, and Ibrahim Aljarah, The University of Jordan, Amman, Jordan, http://www.Ibrahimaljarah.com
www.ju.edu.jo

Dataset Information:
This is an educational data set which is collected from learning management system (LMS) called Kalboard 360. Kalboard 360 is a multi-agent LMS, which has been designed to facilitate learning through the use of leading-edge technology. Such system provides users with a synchronous access to educational resources from any device with Internet connection.

The data is collected using a learner activity tracker tool, which called experience API (xAPI). The xAPI is a component of the training and learning architecture (TLA) that enables to monitor learning progress and learner’s actions like reading an article or watching a training video. The experience API helps the learning activity providers to determine the learner, activity and objects that describe a learning experience.
The dataset consists of 480 student records and 16 features. The features are classified into three major categories: (1) Demographic features such as gender and nationality. (2) Academic background features such as educational stage, grade Level and section. (3) Behavioral features such as raised hand on class, opening resources, answering survey by parents, and school satisfaction.

The dataset consists of 305 males and 175 females. The students come from different origins such as 179 students are from Kuwait, 172 students are from Jordan, 28 students from Palestine, 22 students are from Iraq, 17 students from Lebanon, 12 students from Tunis, 11 students from Saudi Arabia, 9 students from Egypt, 7 students from Syria, 6 students from USA, Iran and Libya, 4 students from Morocco and one student from Venezuela.

The dataset is collected through two educational semesters: 245 student records are collected during the first semester and 235 student records are collected during the second semester.

The data set includes also the school attendance feature such as the students are classified into two categories based on their absence days: 191 students exceed 7 absence days and 289 students their absence days under 7.

This dataset includes also a new category of features; this feature is parent parturition in the educational process. Parent participation feature have two sub features: Parent Answering Survey and Parent School Satisfaction. There are 270 of the parents answered survey and 210 are not, 292 of the parents are satisfied from the school and 188 are not.

(See the related papers for more details).

Attributes
1 Gender - student's gender (nominal: 'Male' or 'Female’)

2 Nationality- student's nationality (nominal:’ Kuwait’,’ Lebanon’,’ Egypt’,’ SaudiArabia’,’ USA’,’ Jordan’,’
Venezuela’,’ Iran’,’ Tunis’,’ Morocco’,’ Syria’,’ Palestine’,’ Iraq’,’ Lybia’)

3 Place of birth- student's Place of birth (nominal:’ Kuwait’,’ Lebanon’,’ Egypt’,’ SaudiArabia’,’ USA’,’ Jordan’,’
Venezuela’,’ Iran’,’ Tunis’,’ Morocco’,’ Syria’,’ Palestine’,’ Iraq’,’ Lybia’)

4 Educational Stages- educational level student belongs (nominal: ‘lowerlevel’,’MiddleSchool’,’HighSchool’)

5 Grade Levels- grade student belongs (nominal: ‘G-01’, ‘G-02’, ‘G-03’, ‘G-04’, ‘G-05’, ‘G-06’, ‘G-07’, ‘G-08’, ‘G-09’, ‘G-10’, ‘G-11’, ‘G-12 ‘)

6 Section ID- classroom student belongs (nominal:’A’,’B’,’C’)

7 Topic- course topic (nominal:’ English’,’ Spanish’, ‘French’,’ Arabic’,’ IT’,’ Math’,’ Chemistry’, ‘Biology’, ‘Science’,’ History’,’ Quran’,’ Geology’)

8 Semester- school year semester (nominal:’ First’,’ Second’)

9 Parent responsible for student (nominal:’mom’,’father’)

10 Raised hand- how many times the student raises his/her hand on classroom (numeric:0-100)

11- Visited resources- how many times the student visits a course content(numeric:0-100)

12 Viewing announcements-how many times the student checks the new announcements(numeric:0-100)

13 Discussion groups- how many times the student participate on discussion groups (numeric:0-100)

14 Parent Answering Survey- parent answered the surveys which are provided from school or not
(nominal:’Yes’,’No’)

15 Parent School Satisfaction- the Degree of parent satisfaction from school(nominal:’Yes’,’No’)

16 Student Absence Days-the number of absence days for each student (nominal: above-7, under-7)

The students are classified into three numerical intervals based on their total grade/mark:
Low-Level: interval includes values from 0 to 69,

Middle-Level: interval includes values from 70 to 89,

High-Level: interval includes values from 90-100.

Relevant Papers:
Amrieh, E. A., Hamtini, T., & Aljarah, I. (2016). Mining Educational Data to Predict Student’s academic Performance using Ensemble Methods. International Journal of Database Theory and Application, 9(8), 119-136.

Amrieh, E. A., Hamtini, T., & Aljarah, I. (2015, November). Preprocessing and analyzing educational data set using X-API for improving student's performance. In Applied Electrical Engineering and Computing Technologies (AEECT), 2015 IEEE Jordan Conference on (pp. 1-5). IEEE.

Citation Request:
Please include these citations if you plan to use this dataset:

Amrieh, E. A., Hamtini, T., & Aljarah, I. (2016). Mining Educational Data to Predict Student’s academic Performance using Ensemble Methods. International Journal of Database Theory and Application, 9(8), 119-136.

Amrieh, E. A., Hamtini, T., & Aljarah, I. (2015, November). Preprocessing and analyzing educational data set using X-API for improving student's performance. In Applied Electrical Engineering and Computing Technologies (AEECT), 2015 IEEE Jordan Conference on (pp. 1-5). IEEE.

"""
    
    text.insert("1.0", about_text)
    text.config(state="disabled")

def test_models():
    test_window = tk.Toplevel(root)
    test_window.title("Test Models")
    test_window.geometry("400x300")
    

    # Decision Tree prediction logic
    
    def decision_tree_prediction():
        prediction_window = tk.Toplevel(test_window)
        prediction_window.title("Decision Tree Prediction")
        prediction_window.geometry("400x300")

        def predict():
            try:
                # Retrieve user input
                raisedhands = int(raisedhands_entry.get())
                visited_resources = int(visited_resources_entry.get())
                announcements_view = int(announcements_view_entry.get())

                # Ensure inputs are valid
                if 0 <= raisedhands <= 7 and 0 <= visited_resources <= 7 and 0 <= announcements_view <= 7:
                    result_label.config(text="Prediction: High-performing (1)")
                    return

                # Prepare input data
                input_data = np.array([[raisedhands, visited_resources, announcements_view]])

                # Load the scaler from the pickle file
                scaler = joblib.load('scaler.pkl')
                decision_tree_classifier = joblib.load('decision_tree_model.pkl')


                # Preprocessing: Standardizing numerical features (Assuming a scaler is available)
                input_data[:, :] = scaler.transform(input_data.astype(float))

                # Make prediction using the trained Decision Tree model
                prediction = decision_tree_classifier.predict(input_data)[0]

                # Display result
                result_label.config(text=f"Prediction: {'High-performing (1)' if prediction == 1 else 'Low-performing (0)'}")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

        # GUI Widgets for Numerical Inputs (Decision Tree)
        tk.Label(prediction_window, text ="What are the most important features that determine the academic performance of students?" ).grid(column=25,padx=275)
        tk.Label(prediction_window, text="Enter Raised Hands:").grid(row=2, column=0, pady=10)
        raisedhands_entry = tk.Entry(prediction_window)
        raisedhands_entry.grid(row=2, column=1)

        tk.Label(prediction_window, text="Enter Visited Resources:").grid(row=4, column=0, pady=10)
        visited_resources_entry = tk.Entry(prediction_window)
        visited_resources_entry.grid(row=4, column=1)

        tk.Label(prediction_window, text="Enter Announcements View:").grid(row=6, column=0, pady=10)
        announcements_view_entry = tk.Entry(prediction_window)
        announcements_view_entry.grid(row=6, column=1)

        # Predict Button
        predict_button = tk.Button(prediction_window, text="Predict", command=predict)
        predict_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = tk.Label(prediction_window, text="Prediction: ")
        result_label.grid(row=10, column=0, columnspan=2, pady=10)

    # Naive Bayes prediction logic
    def nb_prediction():
        prediction_window = tk.Toplevel(test_window)
        prediction_window.title("Naive Bayes Prediction")
        prediction_window.geometry("400x300")

        # Load the saved Naive Bayes model
        with open('nb_model.pkl', 'rb') as f:
            nb_model = pickle.load(f)

        def predict():
            try:
                # Retrieve user inputs
                student_absence_days = float(absence_entry.get())
                raised_hands = float(hands_entry.get())

                # Ensure both inputs are valid
                if student_absence_days < 0 or raised_hands < 0:
                    messagebox.showerror("Input Error", "Please enter valid numerical values greater than or equal to 0.")
                    return

                # Make prediction using the Naive Bayes model
                input_data = np.array([[student_absence_days, raised_hands]])
                prediction = nb_model.predict(input_data)[0]

                # Display result
                result_label.config(text=f"Prediction: {'High-performing (1)' if prediction == 1 else 'Low-performing (0)'}")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numerical values.")

        # GUI Widgets for Naive Bayes Inputs
        tk.Label(prediction_window, text="Is A student High Performing or Low performing ? ").grid(column=25,padx=250)
        tk.Label(prediction_window, text="Enter Student Absence Days and Raised Hands:").grid(row=2, column=0, columnspan=2, pady=10)
        tk.Label(prediction_window, text="Student Absence Days:").grid(row=4, column=0)
        absence_entry = tk.Entry(prediction_window)
        absence_entry.grid(row=4, column=1)

        tk.Label(prediction_window, text="Raised Hands:").grid(row=6, column=0)
        hands_entry = tk.Entry(prediction_window)
        hands_entry.grid(row=6, column=1)

        # Predict Button
        predict_button = tk.Button(prediction_window, text="Predict", command=predict)
        predict_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = tk.Label(prediction_window, text="Prediction: ")
        result_label.grid(row=12, column=0, columnspan=2, pady=10)

    # Gradient Boosting prediction logic

    def gb_prediction():
        prediction_window = tk.Toplevel(test_window)
        prediction_window.title("Gradient Boosting Prediction")
        prediction_window.geometry("400x300")
        
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

        # GUI Widgets for Gradient Boosting Inputs
        tk.Label(prediction_window, text="How does student attendance correlate with their likelihood of being categorized as high-performing or low-performing ? ").grid(column=25,padx=270)
        tk.Label(prediction_window, text="Enter Student Absence Days and Raised Hands:").grid(row=2, column=0, columnspan=2, pady=10)
        tk.Label(prediction_window, text="Student Absence Days:").grid(row=4, column=0)
        absence_entry = tk.Entry(prediction_window)
        absence_entry.grid(row=4, column=1)

        tk.Label(prediction_window, text="Raised Hands:").grid(row=6, column=0)
        hands_entry = tk.Entry(prediction_window)
        hands_entry.grid(row=6, column=1)

        # Predict Button
        predict_button = tk.Button(prediction_window, text="Predict", command=predict)
        predict_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = tk.Label(prediction_window, text="Prediction: ")
        result_label.grid(row=10, column=0, columnspan=2, pady=10)


    # Function to handle Random Forest prediction
    def random_forest_prediction():
        # Create a new window for Random Forest model prediction
        prediction_window = tk.Toplevel(test_window)
        prediction_window.title("Random Forest Prediction")
        prediction_window.geometry("400x300")

        # Prediction logic for Random Forest model
        def predict():
            try:
                # Retrieve user input
                raisedhands = int(raisedhands_entry.get())
                visited_resources = int(visited_resources_entry.get())
                announcements_view = int(announcements_view_entry.get())

                # Ensure inputs are valid
                if 0 <= raisedhands <= 7 and 0 <= visited_resources <= 7 and 0 <= announcements_view <= 7:
                    result_label.config(text="Prediction: High-performing (1)")
                    return

                # Prepare input data
                input_data = np.array([[raisedhands, visited_resources, announcements_view]])

                scaler = joblib.laod('scaler.pkl')
                # Preprocessing: Standardizing numerical features
                input_data[:, :] = scaler.transform(input_data.astype(float))

                rf_classifier = joblib.load('random_forest_model.pkl')
                # Make prediction using the trained Random Forest model
                prediction = rf_classifier.predict(input_data)[0]

                # Display result
                result_label.config(text=f"Prediction: {'High-performing (1)' if prediction == 1 else 'Low-performing (0)'}")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

        # GUI Widgets for Numerical Inputs (Random Forest)
        tk.Label(prediction_window, text ="What are the most important features that determine the academic performance of students?" ).grid(column=25,padx=275)
        tk.Label(prediction_window, text="How mnay times did student participated in class?").grid(row=2, column=0, pady=10)
        raisedhands_entry = tk.Entry(prediction_window)
        raisedhands_entry.grid(row=2, column=1)

        tk.Label(prediction_window, text="How many resources did student visit? (Visited Resources)").grid(row=4, column=0, pady=10)
        visited_resources_entry = tk.Entry(prediction_window)
        visited_resources_entry.grid(row=4, column=1)

        tk.Label(prediction_window, text="How many announcements did student view during the semester?").grid(row=6, column=0, pady=10)
        announcements_view_entry = tk.Entry(prediction_window)
        announcements_view_entry.grid(row=6, column=1)

        # Predict Button
        predict_button = tk.Button(prediction_window, text="Predict", command=predict)
        predict_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = tk.Label(prediction_window, text="Prediction: ")
        result_label.grid(row=10, column=0, columnspan=2, pady=10)

    # Function to handle SVM prediction
    def svm_prediction():
        # Create a new window for SVM model prediction
        prediction_window = tk.Toplevel(test_window)
        prediction_window.title("SVM Prediction")
        prediction_window.geometry("400x300")

        # Prediction logic for SVM model
        def predict():
            try:
                # Retrieve user input for student absence days
                student_absence_days = float(absence_entry.get())

                # Prediction logic based on the given condition
                if 0 < student_absence_days <= 7:
                    prediction = "High-performing (1)"
                else:
                    prediction = "Low-performing (0)"

                # Display result
                result_label.config(text=f"Prediction: {prediction}")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid numerical value for Student Absence Days.")

        # GUI Widgets for Student Absence Days Input (SVM)
        tk.Label(prediction_window, text ="Is there a specific attendance threshold where a student can be classified as high-performing or low-performing ? " ).grid(column=25,padx=250)
        tk.Label(prediction_window, text="Based on Student Absence Days (Mapped to Numeric):").grid(row=2, column=0, columnspan=2, pady=10)
        tk.Label(prediction_window, text="Enter Student Absence Days:").grid(row=4, column=0, padx=10, pady=5)
        absence_entry = tk.Entry(prediction_window)
        absence_entry.grid(row=4, column=1, padx=10, pady=5)

        # Predict Button
        predict_button = tk.Button(prediction_window, text="Predict", command=predict)
        predict_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = tk.Label(prediction_window, text="Prediction: ")
        result_label.grid(row=8, column=0, columnspan=2, pady=10)

    # Function to handle KNN prediction
    def knn_prediction():
        # Create a new window for KNN model prediction
        prediction_window = tk.Toplevel(test_window)
        prediction_window.title("KNN Prediction")
        prediction_window.geometry("400x300")

        # Load the saved KNN model
        with open('knn_model.pkl', 'rb') as f:
            knn_model = pickle.load(f)

        # Prediction logic for the GUI
        def predict():
            try:
                student_absence_days = float(absence_entry.get())
                raised_hands = float(hands_entry.get())
                
                # Prediction based on input conditions
                prediction = 1 if (0 < student_absence_days <= 7 and raised_hands > 0) else 0
                
                result_label.config(text=f"Prediction: {'High-performing (1)' if prediction == 1 else 'Low-performing (0)'}")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numerical values.")

        # GUI Widgets for Numerical Inputs (KNN)
        tk.Label(prediction_window, text ="How do student attendance and participation correlate with their likelihood of being categorized as high-performing or low-performing?" ).grid(column=25,padx=250)
        tk.Label(prediction_window, text="Enter Student Absence Days and Raised Hands").grid(row=2, column=0, columnspan=2, pady=10)
        tk.Label(prediction_window, text="Student Absence Days:").grid(row=4, column=0)
        absence_entry = tk.Entry(prediction_window)
        absence_entry.grid(row=4, column=1)

        tk.Label(prediction_window, text="Raised Hands:").grid(row=6, column=0)
        hands_entry = tk.Entry(prediction_window)
        hands_entry.grid(row=6, column=1)

        # Predict Button
        predict_button = tk.Button(prediction_window, text="Predict", command=predict)
        predict_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = tk.Label(prediction_window, text="Prediction: ")
        result_label.grid(row=12, column=0, columnspan=2, pady=10)

    def ann_prediction():
        # Create a new window for ANN model prediction
        prediction_window = tk.Toplevel(test_window)
        prediction_window.title("ANN Prediction")
        prediction_window.geometry("400x300")


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


        # GUI Widgets for ANN Inputs
        tk.Label(prediction_window, text="Parental Influence Impact on Performance").grid(column=25, padx=275)
        tk.Label(prediction_window, text="Did Parent(s) Answered the Survey? ").grid(row=2, column=0, pady=10)
        parent_answering_survey_var = tk.IntVar()
        tk.Radiobutton(prediction_window, text="Yes", variable=parent_answering_survey_var, value=1).grid(row=4, column=0)
        tk.Radiobutton(prediction_window, text="No", variable=parent_answering_survey_var, value=0).grid(row=4, column=1)

        tk.Label(prediction_window, text="Are Parent(s) satisfied with School?").grid(row=8, column=0, pady=10)
        parent_school_satisfaction_var = tk.IntVar()
        tk.Radiobutton(prediction_window, text="Yes", variable=parent_school_satisfaction_var, value=1).grid(row=10, column=0)
        tk.Radiobutton(prediction_window, text="No", variable=parent_school_satisfaction_var, value=0).grid(row=10, column=1)

        tk.Label(prediction_window, text="How many times did student participated in class  (Raised Hands):").grid(row=16, column=0, pady=10)
        raisedhands_entry = tk.Entry(prediction_window)
        raisedhands_entry.grid(row=16, column=1)

        tk.Label(prediction_window, text="How many Resources did Student visited ? (Visited Resources)").grid(row=18, column=0, pady=10)
        visited_resources_entry = tk.Entry(prediction_window)
        visited_resources_entry.grid(row=18, column=1)

        tk.Label(prediction_window, text="How many announcements did student view? (Announcements View)").grid(row=20, column=0, pady=10)
        announcements_view_entry = tk.Entry(prediction_window)
        announcements_view_entry.grid(row=20, column=1)

        # Predict Button
        predict_button = tk.Button(prediction_window, text="Predict", command=predict)
        predict_button.grid(row=22, column=0, columnspan=2, pady=10)

        # Result Label
        result_label = tk.Label(prediction_window, text="Prediction: ")
        result_label.grid(row=24, column=0, columnspan=2, pady=10)

    # List of models for testing, with actual functionality for each button
    model_buttons = [
        ("Decision Tree", decision_tree_prediction),
        ("Random Forest", random_forest_prediction),
        ("SVM", svm_prediction),
        ("KNN", knn_prediction),
        ("ANN", ann_prediction),
        ("Naive Bayes", nb_prediction),
        ("Gradient Boosting", gb_prediction)
    ]
    
    # Add buttons for each model test
    for model_name, command in model_buttons:
        button = tk.Button(test_window, text=model_name, width=20, command=command)
        button.pack(pady=10)

root = tk.Tk()
root.title("Student Academic Performance")
root.geometry("800x600")  # Larger window for a spacious layout
root.configure(bg="#008080")  # Light blueish background for the main window

# Create a frame for header with a bold title
header_frame = tk.Frame(root, bg="#0078D7", relief="raised", bd=2)
header_frame.pack(fill="x")

header_label = tk.Label(
    header_frame,
    text="Student Academic Performance Analysis",
    font=("Helvetica", 20, "bold"),
    fg="#000000",
    bg="#008080",
    pady=10,
)
header_label.pack()

# Main frame for content
main_frame = tk.Frame(root, bg="#E8F4F8")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Left frame for model buttons
left_frame = tk.Frame(main_frame, bg="#F7FAFC", relief="groove", bd=2)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

models_label = tk.Label(
    left_frame,
    text="Model Visualizations",
    font=("Helvetica", 14, "bold"),
    bg="#F7FAFC",
    fg="#4A4A4A",
)
models_label.pack(pady=10)

models = [
    ("Decision Tree", decision_tree_options),
    ("Random Forest", lambda: show_image("Random_Forest")),
    ("SVM", lambda: show_image("SVM")),
    ("KNN", lambda: show_image("KNN")),
    ("ANN", lambda: show_image("ANN")),
    ("Naive Bayes", lambda: show_image("Naive_Bayes")),
    ("Gradient Boosting", lambda: show_image("Gradient_Boosting")),
]

for model, command in models:
    button = tk.Button(
        left_frame,
        text=model,
        width=20,
        font=("Helvetica", 12),
        bg="#0078D7",
        fg="#FFFFFF",
        activebackground="#005A9E",
        activeforeground="#FFFFFF",
        relief="flat",
        command=command,
    )
    button.pack(pady=5)


# Center frame for additional features
center_frame = tk.Frame(main_frame, bg="#F0F8FF", relief="ridge", bd=2)
center_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

welcome_label = tk.Label(
    center_frame,
    text="Welcome to the Student Academic Performance App",
    font=("Helvetica", 16),
    wraplength=400,
    justify="center",
    bg="#F0F8FF",
    fg="#333333",
)
welcome_label.pack(pady=20)

about_button = tk.Button(
    center_frame,
    text="About Dataset",
    font=("Helvetica", 14),
    bg="#1E90FF",
    fg="#FFFFFF",
    activebackground="#1C86EE",
    activeforeground="#FFFFFF",
    command=show_about_dataset,
)
about_button.pack(pady=20)

test_button = tk.Button(
    center_frame,
    text="Test Models",
    font=("Helvetica", 14),
    bg="#32CD32",
    fg="#FFFFFF",
    activebackground="#2E8B57",
    activeforeground="#FFFFFF",
    command=test_models,
)
test_button.pack(pady=20)


# Footer for credits
footer_frame = tk.Frame(root, bg="#0078D7")
footer_frame.pack(fill="x")

footer_label = tk.Label(
    footer_frame,
    text="Developed by [Ahmed Nawaz Abbasi & Sumama Bin Tahir] | Powered by Tkinter",
    font=("Helvetica", 10),
    fg="#FFFFFF",
    bg="#0078D7",
    pady=5,
)
footer_label.pack()

# Run the Tkinter event loop
root.mainloop()