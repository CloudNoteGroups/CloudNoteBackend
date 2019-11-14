from application.api.model.models import db
import sys
from application import app
from flask_cors import *
if __name__ == '__main__':

    db.init_app(app)
    if 'install' in sys.argv:
        with app.app_context():
            db.create_all()
    CORS(app, supports_credentials=True)
    app.run(port=app.config['PORT'])
