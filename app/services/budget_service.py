from app.models.budget_model import Budget
from app.models.transaction_model import Transaction

def calculate_dashboard_data(user_id):
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    budget = Budget.query.filter_by(user_id=user_id).first()

    total_spending = sum(t.amount for t in transactions)
    remaining_budget = budget.weekly_budget - total_spending if budget else 0

    return {
        "total_spending": total_spending,
        "weekly_budget": budget.weekly_budget if budget else 0,
        "remaining_budget": remaining_budget
    }
