import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# === Load pipeline model ===
model = joblib.load('fraud_model.pkl')  # This includes scaler + logistic model
selected_features = ['Time', 'Amount', 'V14', 'V17', 'V10', 'V12']  # Match your trained features
BEST_THRESHOLD = 0.5  # Default threshold for binary decision

print(f"[INFO] Model loaded with threshold = {BEST_THRESHOLD}")
print(f"[INFO] Selected features: {selected_features}")

# === Routes ===

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            input_data = []
            for feature in selected_features:
                raw_val = request.form.get(feature.lower())
                if raw_val is None or raw_val.strip() == "":
                    raise ValueError(f"Missing input for '{feature}'")
                try:
                    val = float(raw_val)
                except ValueError:
                    raise ValueError(f"Invalid number for '{feature}'")
                input_data.append(val)

            input_df = pd.DataFrame([dict(zip(selected_features, input_data))])

            # Predict using the pipeline (scaler included)
            fraud_proba = float(model.predict_proba(input_df)[0][1])
            is_fraud = int(fraud_proba > BEST_THRESHOLD)

            print(f"[DEBUG] Input: {input_data}")
            print(f"[DEBUG] Fraud Probability: {fraud_proba:.4f}")
            print(f"[DEBUG] Prediction: {is_fraud}")

            return redirect(url_for('result',
                                    prediction=is_fraud,
                                    prob=fraud_proba))

        except Exception as e:
            print(f"❌ Prediction Error: {e}")
            return render_template('predictpage.html',
                                   error=str(e),
                                   selected_features=selected_features)

    return render_template('predictpage.html', selected_features=selected_features)


@app.route('/result')
def result():
    try:
        prediction = request.args.get('prediction', type=int)
        prob = request.args.get('prob', type=float)
        prob_percent = round(prob * 100, 2) if prob is not None else 0.0

        label = "❌ Fraudulent Transaction" if prediction == 1 else "✅ Legitimate Transaction"
        confidence = "High Confidence" if prob_percent > 90 or prob_percent < 10 else "Moderate Confidence"

        return render_template('results.html',
                               prediction=prediction,
                               prob=prob_percent,
                               label=label,
                               confidence=confidence)

    except Exception as e:
        print(f"❌ Error in result route: {e}")
        return "An error occurred while processing the result."


# === Run App ===
if __name__ == '__main__':
    app.run(debug=True)
