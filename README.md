# Academic Performance Analysis with Predictive Modelling

## 📌 Project Overview
This project explores **predicting student academic performance** using **machine learning techniques**. By analyzing behavioral and demographic data, we identify key factors influencing student success.

## 📊 Dataset
- **Name**: xAPI-Edu-Data
- **Source**: Kaggle (Open-access educational repository)
- **Size**: 480 students, 17 features
- **Target Variable**: `Class` (Low, Medium, High Performance)

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

## 🚀 How to Run the Project
1. **Clone this repository**:
   ```bash
   git clone https://github.com/Ahmed-Abbasi1/academic-performance-prediction.git
   cd academic-performance-prediction
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the analysis**:
   ```bash
   python main.py
   ```

## 📜 License
This project is open-source and available under the MIT License.
