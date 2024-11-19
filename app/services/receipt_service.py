import requests
from app.models.database import db
from app.models.transaction_model import Transaction
from datetime import datetime

OCR_API_KEY = "your_api_key"
OCR_URL = "https://api.ocr.space/parse/image"

def process_receipt(file, user_id):
    """
    Processes an uploaded receipt and logs a transaction.
    
    Parameters:
    - file: The uploaded receipt file.
    - user_id: ID of the user uploading the receipt.
    
    Returns:
    - dict: Contains the result of the operation or an error message.
    """
    try:
        # Save the file temporarily
        file_path = f"uploads/{file.filename}"
        file.save(file_path)

        # Call OCR API
        with open(file_path, 'rb') as f:
            response = requests.post(
                OCR_URL,
                files={"file": f},
                data={"apikey": OCR_API_KEY}
            )

        if response.status_code != 200:
            return {"error": "Failed to process the receipt with OCR"}

        # Mock data extraction (replace with actual OCR data processing logic)
        ocr_data = response.json()
        extracted_data = {
            "amount": 50.0,  # Replace with logic to extract amount
            "category": "Food",  # Replace with logic to extract category
            "currency": "USD",
            "transaction_date": datetime.now()  # Use current timestamp for simplicity
        }

        # Log the transaction in the database
        new_transaction = Transaction(
            user_id=user_id,
            amount=extracted_data["amount"],
            category=extracted_data["category"],
            currency=extracted_data["currency"],
            transaction_date=extracted_data["transaction_date"]
        )
        db.session.add(new_transaction)
        db.session.commit()

        return {"data": extracted_data}
    except Exception as e:
        return {"error": str(e)}
