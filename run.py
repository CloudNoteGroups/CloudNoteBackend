from application.api.model.models import db
import sys
from application import app

if __name__ == '__main__':

    db.init_app(app)
    if 'install' in sys.argv:
        with app.app_context():
            db.create_all()

    app.run(port=app.config['PORT'])