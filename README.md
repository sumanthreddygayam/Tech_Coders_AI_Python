# 🏠 House Price Prediction – End-to-End ML Deployment

This project is an end-to-end Machine Learning web application that predicts house prices based on user inputs.  
It demonstrates the complete ML lifecycle: model training → web application → Git collaboration → AWS EC2 deployment → CI/CD automation.

---

## 🚀 Features

- Trained Machine Learning model for house price prediction
- Flask-based web application with HTML UI
- Real-time prediction based on user inputs
- Deployed on AWS EC2
- Team collaboration using Git and GitHub
- CI/CD pipeline using GitHub Actions
- Proper handling of large ML model files

---

## 🧠 Machine Learning Model

- The model is trained using real housing data in a Jupyter Notebook.
- After training, the model is serialized using `pickle`.
- The trained model is loaded into the Flask app for inference.
- Due to GitHub’s 100 MB file size limit, the model file is **not pushed to GitHub**.

---

## 🌐 Flask Web Application

- The web application is built using Flask.
- Users provide the following inputs:
  - Square Feet
  - BHK
  - Ready-to-Move Status
  - Resale Status
  - RERA Approval
- The app processes inputs, prepares feature vectors, and predicts house prices.
- The application runs on port **5000**.

---

## ☁️ AWS EC2 Deployment

- Instance Type: Amazon Linux 2023
- Python 3 installed
- Security Group allows:
  - SSH (port 22)
  - Application access (port 5000)

### Run Application on EC2

```bash
ssh -i house-price-key.pem ec2-user@<EC2_PUBLIC_IP>

cd ~/Tech_Coders_AI_Python
pkill -f app.py
nohup python3 app/app.py > app.log 2>&1 &

Access the application in the browser:
http://54.152.179.132:5000/predict
