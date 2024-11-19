from app.routes import auth_routes, dashboard_routes, budget_routes, transaction_routes, receipt_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cis440fall24team[number]:cis440fall24team[number]@107.180.1.16:3306/cis440fall24team[number]'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(dashboard_routes.bp)
    app.register_blueprint(budget_routes.bp)
    app.register_blueprint(transaction_routes.bp)
    app.register_blueprint(receipt_routes.bp)  # Register receipt blueprint

    return app
