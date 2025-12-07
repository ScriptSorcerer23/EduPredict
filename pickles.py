import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

# Load data
data = pd.read_csv('xAPI-Edu-Data.csv')

# Select relevant columns
X = data[['ParentAnsweringSurvey', 'ParentschoolSatisfaction', 'raisedhands', 'VisITedResources', 'AnnouncementsView']]
y = data['Class']

X = X.fillna('Unknown')  
y = y.fillna('Unknown')

# One-hot encoding for categorical features
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(), ['ParentAnsweringSurvey', 'ParentschoolSatisfaction'])],
    remainder='passthrough'
)

X_transformed = preprocessor.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# SMOTE for oversampling
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# ANN model pipeline
ann_model = Pipeline(steps=[('classifier', MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42))])

# Train the model
ann_model.fit(X_train_resampled, y_train_resampled)

# Save the ANN model and preprocessor using pickle
with open('ann_model.pkl', 'wb') as model_file:
    pickle.dump(ann_model, model_file)

with open('ann_preprocessor.pkl', 'wb') as preprocessor_file:
    pickle.dump(preprocessor, preprocessor_file)

print("ANN Model and Preprocessor saved successfully!")
