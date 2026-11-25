# 🍽️ Zomato Restaurant Analytics — Restaurant Clustering

## Overview

Zomato Restaurant Analytics is a data analysis and machine learning project that explores restaurant characteristics, performs exploratory data analysis, conducts statistical analysis, and applies clustering algorithms to identify restaurant groups based on their attributes.

The project uses **K-Means Clustering** as the final deployment model and provides an interactive web application built with Streamlit for restaurant cluster prediction.

## 🚀 Live Application

**[Launch Zomato Restaurant Analytics](https://zomato-restaurant-analytics.onrender.com)**

Explore the deployed application and predict the cluster assigned to a restaurant based on its characteristics.

## 🎯 Project Objectives

- Explore and analyze restaurant data.
- Clean and preprocess the dataset.
- Perform exploratory data analysis (EDA).
- Analyze restaurant characteristics and patterns.
- Conduct statistical analysis to investigate relationships within the data.
- Apply and evaluate unsupervised machine learning clustering algorithms.
- Deploy the selected clustering model through an interactive web application.

## 📊 Exploratory Data Analysis

The project explores restaurant-related attributes, including:

- Approximate cost for two people.
- Average restaurant rating.
- Pictures per review.
- Number of cuisines.
- Collection status.

EDA and statistical analysis help understand the dataset's characteristics and relationships before applying clustering techniques.

## 📈 Statistical Analysis

Statistical analysis was performed to investigate restaurant characteristics and compare groups within the dataset.

The analysis includes descriptive statistics and statistical testing to explore differences in restaurant-related attributes.

## 🤖 Machine Learning

The project explores unsupervised machine learning techniques for restaurant clustering.

### Algorithms explored

- **K-Means Clustering** — selected for deployment.
- **Agglomerative Clustering** — explored and evaluated as an alternative clustering method.

### Final model

- Algorithm: K-Means Clustering
- Number of clusters: 2
- Learning type: Unsupervised Learning
- Prediction: Cluster assignment

The final model was selected following the clustering analysis and evaluation process conducted during the project.

Cluster identifiers represent groups identified by the clustering algorithm. They do not represent restaurant rankings, quality scores, or ratings.

## 🧪 Interactive Prediction Application

The Streamlit application accepts the following restaurant attributes:

| Feature | Description |
|---|---|
| Approximate Cost for Two | Estimated dining cost for two people in INR |
| Average Restaurant Rating | Average restaurant rating |
| Average Pictures per Review | Average number of pictures associated with reviews |
| Number of Cuisines | Number of cuisines offered |
| Collection Status | Restaurant collection-listing status |

The application processes the input using the saved preprocessing pipeline and trained K-Means model, then displays the predicted cluster.

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Joblib
- Streamlit
- Git
- GitHub
- Render

## 📁 Project Structure

```text
Zomato-Restaurant-Analytics/
│
├── app/
│   └── app.py
│
├── models/
│   └── zomato_kmeans_deployment.joblib
│
├── notebooks/
│   └── Zomato_Restaurant_Analytics.ipynb
│
├── requirements.txt
└── README.md
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/seshasai7d7-source/Zomato-Restaurant-Analytics.git
```

### 2. Navigate to the project directory

```bash
cd Zomato-Restaurant-Analytics
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Launch the application

```bash
python -m streamlit run app/app.py
```

The application will be available at:

http://localhost:8501

## ☁️ Deployment

The application is deployed on Render using the GitHub repository.

**Live URL:** https://zomato-restaurant-analytics.onrender.com

## ⚠️ Disclaimer

The clustering model assigns restaurants to clusters based on the learned patterns in the training data. Cluster numbers are identifiers only and should not be interpreted as rankings, ratings, or quality assessments.

## 👨‍💻 Author

**Kolla Sesha Sai**

Computer Science and Engineering — Artificial Intelligence

GitHub: [seshasai7d7-source](https://github.com/seshasai7d7-source)

---

*Built using Python, data analytics, and unsupervised machine learning.*
