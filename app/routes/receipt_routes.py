from flask import Blueprint, request, jsonify, session, render_template
from app.services.receipt_service import process_receipt

bp = Blueprint('receipt', __name__, url_prefix='/receipt')

@bp.route('/scan', methods=['GET', 'POST'])
def scan_receipt():
    """
    Handles receipt uploads.
    GET: Render the receipt upload page.
    POST: Process the uploaded receipt and log the transaction.
    """
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        file = request.files['receipt']
        if file:
            result = process_receipt(file, session['user_id'])
            if result.get("error"):
                return jsonify({"error": result["error"]}), 400
            return jsonify({"message": "Receipt processed successfully", "data": result["data"]})
        return jsonify({"error": "No file uploaded"}), 400

    return render_template('scan_receipt.html')
