#dependecia de flask 
from flask import Flask, render_template

#dependecia de los modelos
from flask_sqlalchemy import SQLAlchemy

#dependecia para las migraciones 
from flask_migrate import Migrate

#dependencia para fecha y hora
from datetime import datetime

#dependencias de wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


#crear el objeto flask
app = Flask(__name__)

#definir la "cadena de conexion" (connection )
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SECRET_KEY'] = '2687340'

#crear el objeto de modelos
db = SQLAlchemy(app)

#crear el objeto de la migracion 
migrate = Migrate(app, db)

#crear formulario de registro de productos 
class ProductosForm(FlaskForm): 
    nombre = StringField('nombre del producto')
    precio = StringField('precio del producto')
    submit = SubmitField('registrar producto')

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
    
    
#rutas:
@app.route('/productos', methods = ['GET', 'POST'])
def nuevo_producto():
    form = ProductosForm()
    if form.validate_on_submit():
#creamos un nuevo producto
        p = Producto(nombre = form.nombre.data , precio = form.precio.data)
        db.session.add(p)
        db.session.commit()
        return "producto registrado" 
    return render_template('nuevo_producto.html', form = form)
    