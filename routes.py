from flask import Flask, render_template, request, redirect, url_for, session
from forms import SignupForm, LogInForm, ReviewForm
from models import database, User, Review

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flaskapplication'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://imudsikyzdilcq:4753bf8ab220ab96f32103ec8f86fe8aa13f60f607b7a5ce3132db10cfac5651@ec2-54-221-253-228.compute-1.amazonaws.com:5432/d1umrtn5e22sip"
database.init_app(app)
app.secret_key = "development-key"

@app.route("/")
def index():
	review_records = Review.query.all()
	return render_template("index.htm", records = review_records)
		
@app.route("/read_review/<id>")
def read(id):
	review = Review.query.filter_by(review_id = id).first()
	return render_template("read.htm", record=review)
		
@app.route("/write_review", methods=['GET','POST'])
def write_review():
	if "logged_in" in session:
		write_review_form = ReviewForm()
		if request.method == "POST" and write_review_form.validate():
			new_review= Review(session['username'], write_review_form.coffee_shop.data, write_review_form.rating.data, write_review_form.title.data, write_review_form.description.data)
			try:
				database.session.add(new_review)
				database.session.commit()
				return redirect(url_for('index'))
			except:
				database.session.rollback()
				return render_template("write_review.htm", review_form = write_review_form, message="Error: Try again")
		else:
			return render_template("write_review.htm", review_form = write_review_form)	
	else:
		return render_template("index.htm", message="You need to log in")
	
@app.route("/sign_out")
def sign_out():
	session.clear()
	return redirect(url_for('index'))

@app.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
	if "logged_in" in session:
		return redirect(url_for('index'))
		
	signUpForm = SignupForm()
	logInForm = LogInForm()
	
	if request.method == "POST" and signUpForm.validate():
		new_user = User(signUpForm.username.data, signUpForm.password.data)
		try:
			database.session.add(new_user)
			database.session.commit()
			session['username'] = new_user.username
			return redirect(url_for('index'))
		except:
			database.session.rollback()
			return render_template("signup.htm", sign_up_form=form, log_in_form = logInForm, error_message="Pick another username")
	
	elif request.method == "POST" and logInForm.validate():
		input_username = logInForm.username.data
		input_password = logInForm.password.data
		
		records = User.query.filter_by(username=input_username)
		user = records.first()
		
		if user is not None and user.check_password(input_password):
			session['username'] = input_username
			session['logged_in'] = True
			return redirect(url_for('index'))
		else:
			return render_template("signup.htm", sign_up_form=signUpForm, log_in_form = logInForm , log_in_error="Can't find your details")
		
	elif request.method == "GET" or (request.method == "POST" and signUpForm.validate() == False) or (request.method == "POST" and logInForm.validate() == False):
		return render_template("signup.htm", sign_up_form=signUpForm, log_in_form = logInForm )

if __name__ == "__main__":
	app.run(debug=True)
	

