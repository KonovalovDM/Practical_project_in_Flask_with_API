from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'calendar.db'

    with app.app_context():
        from .database import init_db
        init_db()

    from .views import calendar_bp
    app.register_blueprint(calendar_bp, url_prefix='/api/v1/calendar')

    return app