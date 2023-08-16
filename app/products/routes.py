from flask import render_template

from . import products

@products.route('/create')
def crear_product():
    return render_template('new.html')