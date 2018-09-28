from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def index():
    return render_template('user_signup.html',title='User Signup')

@app.route('/welcome', methods=['POST']) 
def signup():
    name = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    if password != confirm:
        return redirect('/') 
    else:
        return render_template('welcome.html', name=name) 
          


           

app.run()    