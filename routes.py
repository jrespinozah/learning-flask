from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ozvqdjudguodhe:fbf6627db0142766509cebe9e5769c36555fcf245d28625cff7b3b6ba020b8fa@ec2-184-73-249-56.compute-1.amazonaws.com:5432/d2ujt1ef1oe1qt'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
	form = SignupForm()
	if request.method == 'POST':
		if form.validate() == False:
			return render_template("signup.html", form=form)
		else:
			newuser = User(form.first_name.data,form.last_name.data,form.email.data,form.password.data)
			db.session.add(newuser)
			db.session.commit()
			return "Success!"
	elif request.method == "GET":
		return render_template("signup.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)