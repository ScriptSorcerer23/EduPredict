# EduPredict: Academic Performance Analysis with Predictive Modelling

## 📌 Project Overview
This project explores **predicting student academic performance** using **machine learning techniques**. By analyzing behavioral and demographic data (e.g., gender, guardian relation, attendance), we identify key factors influencing student success. It includes a **desktop app** for interactive predictions.

Demo: https://igit.me/EduPredict

## 📊 Dataset
- **Name**: xAPI-Edu-Data
- **Source**: Kaggle (Open-access educational repository)
- **Size**: 480 students, 17 features
- **Target Variable**: `Class` (Low, Medium, High Performance)
- **Key Features**: Demographics (gender, nationality, relation to guardian—Mother vs. Father), behavioral (raised hands, resource visits, announcements, discussions, parental surveys, absences).

## 🛠 Data Preprocessing
- **Data Cleaning**: Handled missing values, standardized numerical features
- **Feature Engineering**: Encoded categorical data
- **No Dimensionality Reduction**: All 17 features retained for interpretability

## 🤖 Machine Learning Models Used
We applied **seven classification algorithms**:

| Model                     | Purpose |
|---------------------------|---------|
| 📌 **Decision Tree**       | Interpretability & feature importance |
| 🌳 **Random Forest**       | Improved accuracy & robustness |
| 📈 **Support Vector Machine (SVM)** | Identified attendance threshold |
| 📍 **K-Nearest Neighbors (KNN)** | Analyzed attendance & participation impact |
| 📊 **Naïve Bayes**        | Probabilistic classification |
| 🚀 **Gradient Boosting**   | High accuracy & feature importance |
| 🧠 **Artificial Neural Network (ANN)** | Studied parental influence |

## 🔍 Key Insights
✅ **Attendance Matters**: Students with **>7 absences** are likely **low-performing**.  
✅ **Participation Helps**: More class participation (raised hands) → Higher performance.  
✅ **Parental Involvement is Crucial**: Students whose parents **answered school surveys** performed better.  
✅ **Demographics**: Explored gender and guardian relation (Mother vs. Father) impacts via statistical tests and visualizations.

## 🚀 How to Run the Project
1. **Clone this repository**:
   ```bash
   git clone https://github.com/ScriptSorcerer23/EduPredict.git
   cd EduPredict
   ```
2. **Install dependencies** (create `requirements.txt` if needed):
   ```bash
   pip install pandas numpy scikit-learn seaborn matplotlib tkinter imbalanced-learn
   ```
3. **Run the analysis** (Jupyter Notebook):
   ```bash
   jupyter notebook Academic_Performance_Project.ipynb
   ```
4. **Run the Desktop App** (e.g., for ANN predictions):
   ```bash
   python ann_front_end.py
   ```
   - Use individual front-end scripts (e.g., `decision_tree_front_end.py`) for model-specific GUIs.

## 📁 Project Structure
- `Academic_Performance_Project.ipynb`: Main analysis notebook with EDA, modeling, and visualizations.
- `*_front_end.py`: Desktop GUI scripts for each model.
- `*.pkl`: Trained models, preprocessors, and scalers.
- `xAPI-Edu-Data.csv`: Dataset.
- `Data_Mining_Project_Presentation.pptx`: Project slides.
- `*.png`: Model diagrams and plots.

## 📜 License
This project is open-source. Feel free to contribute or adapt!
This project is open-source and available under the MIT License.
