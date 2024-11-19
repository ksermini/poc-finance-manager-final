from app import app

if __name__ == "__main__":
    # Start the Flask app
    print("Starting the Personal Finance Manager...")
    print("Available Routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.methods} -> {rule}")
    app.run(debug=True)
