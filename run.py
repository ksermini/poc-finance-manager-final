from app import create_app

app = create_app()

if __name__ == "__main__":
    print("Starting the Personal Finance Manager...")
    app.run(debug=True)
