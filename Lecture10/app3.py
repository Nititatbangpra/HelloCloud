
from flask import Flask, request ,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config["SQLALCHEMY_DATABASAE_URI"] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
#Init db
db = SQLAlchemy(app)
#Init ma

ma= Marshmallow(app)

#Product class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)


    def __init__(self,name,desctiption,price,qty):
        self.name = name
        self.description = desctiption
        self.price = price
        self.qty = qty


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


product_schema = ProductSchema()
product_schema = ProductSchema(many=True)

db.create_all()


#Run Server
if __name__ == '__main__':
    app.run(debug=True)
