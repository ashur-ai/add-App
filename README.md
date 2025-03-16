# add-App
This is a simple python application to add two numbers
# Streamlit Addition App

This is a simple **Streamlit** application that allows users to add two numbers. The app is deployed on **Streamlit Community Cloud** and follows a **CI/CD pipeline** using GitHub.

## Features
- Accepts two numerical inputs.
- Displays the sum of the numbers.
- Hosted on **Streamlit Community Cloud**.

## Setup Instructions

### **1. Install Dependencies**
Ensure you have **Git**, **VS Code**, and **Python** installed.

### **2. Clone the Repository**
```bash
git clone https://github.com/ashur-ai/add-App.git
cd add-App
```

### **3. Create a Virtual Environment**
```bash
conda create --name myenv python=3.9
conda activate myenv
```

### **4. Install Requirements**
```bash
pip install -r requirements.txt
```

### **5. Run the Streamlit App**
```bash
streamlit run app.py
```

## **Git Workflow**
When making changes, follow these Git commands:

```bash
git add .
git commit -m "Updated the application"
git push origin main
```

## **CI/CD Integration**
This project is integrated with **Streamlit Community Cloud**. Once changes are pushed to GitHub, the app is automatically updated.

### **Deployment Steps:**
1. Create an account on **Streamlit Community Cloud**.
2. Connect the repository.
3. Deploy the app.

Now, every time you modify the code and push changes using Git, the application will update automatically.

## **Contributing**
Feel free to contribute by opening issues or submitting pull requests.


how to make changes
go to open file then documents open add-app in vs code
then make changes

## **Author**
Ashur Addanki (@ashur-ai)

