from app import db
from datetime import datetime 

#crear los modelos 
class Cliente(db.Model):
    
    #definir los atributos 
    __tablename__= "clientes"
    id = db.Column(db.Integer , primary_key = True )
    username = db.Column(db.String(120), nullable = True)
    pasword = db.Column(db.String(128), nullable = True)
    Email = db.Column(db.String(128), nullable = True)
    
    #relaciones SQL alchemy
    ventas = db.relationship('Venta', backref = "cliente", lazy = "dynamic")

class Producto(db.Model):
    
    #definir los atributos
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))

class Venta(db.Model):
    
    #definir los atributos 
    __tablename__ = "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    
    #clave foranea:
    cliente_id = db.Column(db.Integer , db.ForeignKey('clientes.id'))
    
class Detalle(db.Model):
    
    #definir los atributos
    __tablename__ = "detalles"
    id = db.Column(db.Integer, primary_key = True)
    cantidad = db.Column(db.Integer)
    
    #clave foranea
    producto_id = db.Column(db.Integer , db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer , db.ForeignKey('ventas.id'))