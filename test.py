from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello world'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html',name=name)

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

if __name__ == '__main__':
	app.debug=True
	with app.test_request_context():
		print (url_for('hello'))
#		print (url_for('get_profile',username='flask'))

	app.run()


