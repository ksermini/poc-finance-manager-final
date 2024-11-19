from sqlalchemy import create_engine
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'

db_config = {
    'host': '107.180.1.16',
    'user': 'cis440fall24team2',
    'password': 'cis440fall24team2',
    'database': 'cis440fall24team2',
    'port': 3306
}
engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

transactions_df = pd.DataFrame(columns=["user_id", "amount", "category", "currency", "transaction_date"])
budgets_df = pd.DataFrame(columns=["user_id", "income", "expenses", "weekly_budget"])

OCR_API_KEY = "your_api_key"
OCR_URL = "https://api.ocr.space/parse/image"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with engine.connect() as conn:
            result = conn.execute(f"SELECT * FROM users WHERE email='{email}' AND password='{password}'").fetchone()
            if result:
                session['user_id'] = result['id']
                return redirect(url_for('dashboard'))
            else:
                return "Invalid credentials. Try again.", 401
    return render_template('login.html')

@app.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    transactions = pd.read_sql(f"SELECT * FROM transactions WHERE user_id={user_id}", engine)
    budget = pd.read_sql(f"SELECT * FROM budgets WHERE user_id={user_id}", engine)

    total_spending = transactions['amount'].sum() if not transactions.empty else 0
    weekly_budget = budget['weekly_budget'].iloc[0] if not budget.empty else 0
    remaining_budget = weekly_budget - total_spending

    dashboard_data = {
        "total_spending": total_spending,
        "weekly_budget": weekly_budget,
        "remaining_budget": remaining_budget
    }

    return render_template('dashboard.html', dashboard_data=dashboard_data)

@app.route('/setup-budget', methods=['POST'])
def setup_budget():
    global budgets_df
    user_id = session['user_id']
    data = request.json
    income = data.get('income', 0)
    expenses = data.get('expenses', 0)

    weekly_budget = (income - expenses) / 4
    new_budget = pd.DataFrame([{"user_id": user_id, "income": income, "expenses": expenses, "weekly_budget": weekly_budget}])

    budgets_df = pd.concat([budgets_df, new_budget], ignore_index=True)
    budgets_df.to_sql(name='budgets', con=engine, if_exists='append', index=False)

    return jsonify({"message": "Budget setup complete", "weekly_budget": weekly_budget})

@app.route('/scan-receipt', methods=['GET', 'POST'])
def scan_receipt():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files['receipt']
        if file:
            file_path = f"uploads/{file.filename}"
            file.save(file_path)

            with open(file_path, 'rb') as f:
                response = requests.post(OCR_URL, files={"file": f}, data={"apikey": OCR_API_KEY})
            
            if response.status_code == 200:
                ocr_data = response.json()
                extracted_data = {
                    "user_id": session['user_id'],
                    "amount": 50,
                    "category": "Food",
                    "currency": "USD",
                    "transaction_date": "2024-11-18"
                }
                transactions_df = pd.concat([transactions_df, pd.DataFrame([extracted_data])], ignore_index=True)
                transactions_df.to_sql(name='transactions', con=engine, if_exists='append', index=False)

                return jsonify({"message": "Receipt processed successfully", "data": extracted_data})
    return render_template('scan_receipt.html')
