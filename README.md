# 💳 Credit Card Fraud Detection Web App

An interactive and user-friendly Flask-based web application that uses a machine learning model to predict fraudulent credit card transactions in real time using just 6 simple features. This project is built to demonstrate practical machine learning deployment and frontend-backend integration.

---

## 🚀 Live Demo

🟢 **Live on Render**: [https://creditcardfrauddetection-a6gy.onrender.com/]

---

## 📌 Key Features

- ✅ Fraud detection using Logistic Regression with SMOTE for imbalance handling
- ✅ Lightweight 6-feature input: `Time`, `Amount`, `V14`, `V17`, `V10`, `V12`
- ✅ Built-in preprocessing and scaling (via pipeline)
- ✅ Beautiful, responsive frontend (HTML/CSS + animations)
- ✅ Render deployment-ready (free hosting)
- ✅ Metrics include precision, recall, F1, and ROC AUC

---

## 🧠 Technologies Used

| Tech             | Purpose                       |
|------------------|-------------------------------|
| Flask            | Web application backend       |
| HTML/CSS         | Frontend interface            |
| scikit-learn     | Model training & evaluation   |
| imbalanced-learn | SMOTE oversampling            |
| pandas/numpy     | Data handling                 |
| joblib           | Model serialization           |
| gunicorn         | WSGI server for deployment    |

---

## 📁 Project Structure

```
credit_card_fraud_detection/
├── app.py                  # Flask backend
├── fraud_model.pkl         # Trained model (pipeline: scaler + classifier)
├── requirements.txt        # Dependencies for deployment
├── Procfile                # Render startup config
├── templates/              # HTML templates
│   ├── index.html
│   ├── predictpage.html
│   └── results.html
└── static/ (optional)      # For CSS or JS if extended
```

---

## 🏗️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/imrishu18/CreditCardFraudDetection.git
cd CreditCardFraudDetection
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000/

```

---

## 🧪 Model Overview

| Metric     | Value   |
|------------|---------|
| Accuracy   | 98%     |
| Recall     | 86%     |
| Precision  | 9%      |
| F1-Score   | 0.16    |
| ROC AUC    | 0.99    |

✅ The model prioritizes **recall** to avoid missing fraudulent transactions, even at the cost of some false positives — a trade-off suitable for fraud detection.

---

## 📊 How It Works

- User inputs 6 transaction features
- Model predicts fraud probability
- Result page displays:
  - Fraud vs Legit label
  - Confidence percentage
  - Risk message (High/Moderate)

---

## 🧹 Notes

- Dataset (`creditcard.csv`) is too large for GitHub (143MB) and is **excluded**
- Only the trained model `.pkl` is stored
- If retraining is needed, download dataset from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)

---

## 🌐 Deployment (Render)

1. Push to GitHub
2. Connect repo to Render
3. Add:
   - `Procfile`: `web: gunicorn app:app`
   - `requirements.txt`
4. Deploy with **Python environment**

---

## 🔗 Project Links

- 📓 **Google Colab Notebook**: [Run the Model on Google Colab](https://colab.research.google.com/drive/1ibs8pfJF6mm_iSzIzstnMq8TagEk5ZEL?usp=sharing)

---

## 👨‍💻 Author

**Rishu Raj**  
🔗 [GitHub](https://github.com/imrishu18)  
💼 [LinkedIn][Coming soon...](https://www.linkedin.com/in/your-link)

---

## 📜 License

This project is open-source and free to use under the MIT License.
