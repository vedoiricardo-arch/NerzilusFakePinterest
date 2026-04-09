from Nerzilus import database, app
from Nerzilus.models import Usuario, Foto

with app.app_context():
    database.create_all()

