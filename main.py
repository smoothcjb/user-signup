from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def index():
    return render_template('user_signup.html',title='User Signup', username_error='',password_error='',confirm_error='',email_error='', username='', email='')

@app.route('/signup', methods=['POST']) 
def signup():
    name = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']
    username_error = ''
    password_error = ''
    confirm_error = ''
    email_error = '' 
    

    if len(name) > 20 or " " in name:    
        username_error = 'Username cannot contain a space or exceed 20 characters.'
        return render_template('user_signup.html',title='User Signup',username_error=username_error,password_error='',confirm_error='',email_error='',username=name,)
    elif len(password) > 20 or " " in password:
        password_error = 'Password cannot contain a space or exceed 20 characters.'
        return render_template('user_signup.html',title='User Signup', username_error='',password_error=password_error,confirm_error='',email_error='')
    elif password != confirm:    
        confirm_error= 'Passwords do not match.'
        return render_template('user_signup.html',title='User Signup', username_error='',password_error='',confirm_error=confirm_error,email_error='',email=email,username=name)
    elif email == '':
        return redirect('/welcome?username={0}'.format(name))   
    elif "@" not in email and "." not in email:
        email_error = "Enter a valid email address."
        return render_template('user_signup.html',title='User Signup', username_error='',password_error='',confirm_error='',email_error=email_error,username=name,email=email)
    elif len(email) > 20 or " " in email:
        email_error = 'Email address cannot contain a space or exceed 20 characters.'
        return render_template('user_signup.html',title='User Signup', username_error='',password_error='',confirm_error='',email_error=email_error,username=name,email=email)         
    else:
        return redirect('/welcome?username={0}'.format(name)) 

@app.route('/welcome')
def welcome():
    name = request.args.get('username')
    return render_template('welcome.html',name=name)        



app.run()    