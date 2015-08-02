from flask import Flask,url_for,render_template

app = Flask(__name__)
app.debug = True


@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):

	return render_template('hello.html',name=name)#'hello world'

@app.route('/profile/<username>')
def get_profile(username):
	return 'profile : ' + username

@app.route('/profile/',methods=['POST','GET'])
def profile(username=None):
	error =None
	if reuqest.method == 'POST':
		username = request.form['username']
		email = reuqest.form['email']
		if not username and not email:
			return add_profile(reuqest.form)
	else:
		error = "Invalid username or emial"

	return render_template('profile.html',error=error)

if __name__ == '__main__':
	with app.test_request_context():
		print(url_for('hello'))
		print (url_for('get_profile',username='flask'))

	app.run()
