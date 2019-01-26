from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

database = SQLAlchemy()

class User(database.Model):
	__tablename__ = "users"
	username = database.Column(database.String(255), primary_key = True)
	password = database.Column(database.String(255))
	
	def __init__(self, username, given_password):
		self.username = username
		self.password = self.make_password_hash(given_password)
		
	def make_password_hash(self, given_password):
		return generate_password_hash(given_password)
	
	def check_password(self, given_password):
		return check_password_hash(self.password, given_password)


class Review(database.Model):
	review_ID = database.Column(database.Integer, primary_key=True)
	username = database.Column(database.String(255))
	coffee_shop = database.Column(database.String(255))
	rating = database.Column(database.Integer)
	title = database.Column(database.String(255))
	description = database.Column(database.Text)

	def __init__(self, username, coffee_shop, rating, title, description):
		self.username = username
		self.coffee_shop = coffee_shop.Title
		self.rating = rating
		self.title = title.Title
		self.description = description

	 
	


