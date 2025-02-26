# 🔍 Fraud Detection Machine Learning Project

This project focuses on building a machine learning model to detect fraudulent transactions. The process involves data preprocessing, exploratory data analysis (EDA), model training, and deployment in a containerized environment.

---

## 🏆 Problem Description

Financial fraud detection is a critical challenge in modern finance and e-commerce. The dataset used in this project is synthetic and includes a variety of transactional patterns that mimic real-world scenarios. Features such as transaction amount, geographic location, card type, and device type were analyzed to predict whether a transaction is fraudulent.

---
## 🏗️ Architecture Overview
![Architecture diagram](https://github.com/Naga-Manohar-Y/ML_ZoomCamp/blob/main/07_midterm_project/FD_architecture.png)
---
## 📌 Project Workflow

### 1️⃣ **Exploratory Data Analysis (EDA)** 📊
   - Understand the dataset's structure, distribution, and key characteristics.
   - Visualize patterns and correlations among features such as transaction amounts and frequencies.
   - Identify potential anomalies in the data that could signal fraudulent activity.

### 2️⃣ **Model Training** 🤖
   - Various machine learning models were tested and evaluated using metrics like precision, recall, and F1 score.
   - **XGBoost** was selected as the best-performing model based on its high accuracy and precision in detecting fraudulent transactions.
   - The trained model is saved in a binary file named `XGBoost_model.bin`.

### 3️⃣ **Exporting Notebook to Script** 📜
   - The main code from the Jupyter Notebook was exported to Python scripts (`train.py` and `predict.py`) for streamlined execution and deployment.

### 4️⃣ **Model Deployment** 🚀
   - A Flask web application is implemented to provide an API endpoint for predicting fraud based on transaction details.
   - The Flask app is containerized using Docker for consistent and scalable deployment.

### 5️⃣ **Reproducibility** 🔄
   - Reproducibility is ensured by using clear scripts (`train.py` and `predict.py`), specifying dependencies in `Pipfile`, and documenting each step.

---

## 🛠️ Dependency and Environment Management

- **Pipfile** and **Pipfile.lock** are used to define and lock the Python dependencies for the project.
- **Key Dependencies**:
   ✅ scikit-learn 
   ✅ XGBoost 
   ✅ Flask 
   ✅ pandas 
   ✅ numpy 

---

## 🐳 Containerization

- A **Dockerfile** is provided for containerizing the application. The Docker container includes the following:
  - Installation of required dependencies using `pipenv`.
  - Configuration of the Flask app for serving predictions.
  - Exposing port `9696` for the web service.

---

## 🏃 How to Run It

### Prerequisites
- Python 3.12+
- Docker (for containerized deployment)

### Steps to Run Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Naga-Manohar-Y/ML_ZoomCamp/tree/main
   cd 07_midterm_project
   ```
2. **Install Dependencies**:

```bash
pip install pipenv
pipenv install
```
This will create a virtual environment and install all required dependencies for the project.
3. **Train the Model**:

```bash
python train.py
```
This script will train the model using the training dataset, and save the model to a binary file (XGBoost_model.bin) which can then be used for predictions.
4. **Build the Docker Image**:

After ensuring that the project files are in place, build the Docker image by running the following command in the project directory:
```bash
docker build -t fraud-detection:latest .
```
5. **Run the Docker Container**:

Once the Docker image is built, you can run the container:
```bash
docker run -p 9696:9696 fraud-detection:latest
This will run the application inside a Docker container and map port 9696 from the container to your local machine.
```

