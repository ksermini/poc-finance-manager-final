# Personal Finance Manager

## Overview
The **Personal Finance Manager** is a Flask-based web application designed to help users track their finances dynamically. It allows users to:

- Set up a weekly budget based on income and expenses.
- Upload receipts and log manual transactions.
- View a real-time dashboard with spending summaries, budget status, and charts.

## Features
- **User Authentication**: Login system to manage separate accounts.
- **Dynamic Budgeting**: Weekly budget calculation based on user input.
- **Receipt Scanner**: Upload receipts to automatically log transactions using OCR.
- **Dashboard Highlights**:
  - Spending by category (chart).
  - Budget status summary (remaining vs. spent).
- **Responsive Design**: Simple and user-friendly interface.

## Directory Structure
```
/poc-finance-manager
├── run.py               # Main file to start the Flask app
├── app.py               # Backend logic and routes
├── requirements.txt      # Dependencies for the project
├── templates/           # HTML files for the frontend
│   ├── login.html       # Login page
│   ├── dashboard.html   # Dashboard
│   ├── scan_receipt.html # Receipt scanner
├── static/              # Static assets (CSS, JS)
│   ├── styles.css       # Custom styles
│   ├── chart.js         # Chart.js integration
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd poc-finance-manager
   ```

2. **Install Dependencies**:
   Make sure Python 3.8+ is installed. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Flask app by running:
   ```bash
   python run.py
   ```

4. **Access the App**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints
### User Management
- **Login**: `POST /login`  
  Authenticate users with email and password.
  
### Budget Management
- **Setup Budget**: `POST /setup-budget`  
  Body: `{"income": 5000, "expenses": 2000}`  
  Calculates and saves a weekly budget.

### Transactions
- **Scan Receipt**: `POST /scan-receipt`  
  Upload a receipt and log the transaction.

### Dashboard
- **Dashboard**: `GET /`  
  Displays spending summary and budget highlights.

## Notes
- Ensure the MySQL database is configured with the correct credentials in `app.py`.
- Replace `"your_api_key"` in the `OCR_API_KEY` variable with your OCR Space API key.

## Technologies Used
- **Backend**: Flask
- **Frontend**: HTML, CSS, Chart.js
- **Database**: MySQL
- **OCR**: OCR.Space API
