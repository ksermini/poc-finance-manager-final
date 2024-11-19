from flask import Blueprint, render_template, session, redirect, url_for
from app.services.budget_service import calculate_dashboard_data

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    data = calculate_dashboard_data(user_id)
    return render_template('dashboard.html', dashboard_data=data)
