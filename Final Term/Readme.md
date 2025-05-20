# 💼 Salary Prediction using Naïve Bayes Classifier


This project uses a real-world salary dataset to perform data preprocessing, visualization, classification, and evaluation using a **Naïve Bayes Classifier**. It is implemented using Python and Google Colab.

---

## 📚 Table of Contents

- [Google Drive Mounting](#google-drive-mounting)
- [Libraries Used](#libraries-used)
- [Tasks Overview](#tasks-overview)
- [Results](#results)
- [Conclusion](#conclusion)

---

## 🔗 Google Drive Mounting

To load the dataset, Google Drive is mounted using the following command:

```python
from google.colab import drive
drive.mount('/content/drive')
````

```
📦 Libraries Used
pandas and numpy for data manipulation

matplotlib and seaborn for visualization

sklearn for machine learning preprocessing, modeling, and evaluation


✅ Tasks Overview

📝 Task 1: Load the Dataset

The dataset salaries1.csv is loaded from Google Drive using Pandas.

🧹 Task 2: Data Cleaning
Checked and filled missing values (salary column filled with mean)

Removed duplicate rows

📊 Task 3: Frequency Distribution Visualization
Created multiple bar plots using matplotlib.pyplot.subplot() to visualize distributions of categorical and numerical features like:

work_year, experience_level, employment_type, job_title, salary_currency, etc.

📉 Task 4: Relationship with Salary
Plotted average salary versus features like:

work_year, experience_level, employment_type, job_title, and remote_ratio

⚙️ Task 5: Feature Scaling
Used StandardScaler for numerical features

Used OneHotEncoder for categorical features

Combined using ColumnTransformer in a Pipeline

✂️ Task 6: Train-Test Split
Split the dataset using:

train_test_split(..., random_state=321)
🤖 Task 7: Naïve Bayes Model
Trained a GaussianNB model using the scaled training data.

🔍 Task 8: Confusion Matrix
Computed and printed the confusion matrix for predictions on the test set. (Can also be visualized using seaborn.heatmap())

📈 Task 9: Accuracy Scores
Calculated training and test set accuracy

Compared the scores to assess model performance

🔁 Task 10: 10-Fold Cross-Validation
Performed cross-validation with cv=10 and reported:

Individual fold accuracies

Mean accuracy

📊 Results Summary
Train Accuracy: Displayed in output

Test Accuracy: Displayed in output

Cross-Validation Mean Accuracy: Displayed in output

🧠 Conclusion
Naïve Bayes is simple and fast but may not be ideal for regression-like salary prediction (continuous target).

Future models can use classification-friendly targets or switch to regression models like LinearRegression, RandomForestRegressor, etc.

Proper preprocessing and understanding feature relationships significantly improve predictive modeling.

````
## Author

Nasimul Arafin Rounok
