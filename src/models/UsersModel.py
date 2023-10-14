from . import db, app
from flask_migrate import Migrate

migrate = Migrate()
migrate.init_app(app, db)

class Users(db.Model):
            
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), nullable=False)
    nombre_completo = db.Column(db.String(150), nullable=False)
    correo = db.Column(db.String(80), nullable=False)
    
    def __str__(self):
        return f'ID: {self.id_usuario}, Usuario: {self.usuario}, Nombre: {self.nombre_completo}, Correo: {self.correo}'
        
    def __repr__(self):
        return f'{self.full_name}'