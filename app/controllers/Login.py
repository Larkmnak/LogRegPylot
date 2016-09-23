"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Login(Controller):
    def __init__(self, action):
        super(Login, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('index.html')

    def login(self):
        ErrorBool == 0
        message = ''
        print 'login'
        email = request.form['email']
        print email
        password = request.form['password']
        print password
        user_query = "SELECT email FROM users WHERE email = :email LIMIT 1"
        query_data = { 'email': email }
        user = mysql.query_db(user_query, query_data) # user will be returned in a list
        print user
        while(ErrorBool == 0):
            if not user:
                print 'email error'
                message = 'Error 86-5 EMAIL NOT FOUND: incorrect email'
                ErrorBool = 1
                break
            else:
                print "email equal"
                print user[0]['email']
            user_query = "SELECT password FROM users WHERE email = :email LIMIT 1"
            query_data = { 'email': email }
            print password
            user = mysql.query_db(user_query, query_data)
            print user
            if not user:
                print 'password error'
                message = 'Error 86-5 EMAIL NOT FOUND: incorrect password'
                ErrorBool = 1
                break
            if bcrypt.check_password_hash(user[0]['password'], password):
                print 'correct'
                print user[0]['password']
                user_query = "SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users WHERE email = :email LIMIT 1"
                query_data = { 'email': email }
                name = mysql.query_db(user_query, query_data)
                ErrorBool = 2
                break
            else:
                print 'incorrect'
                message = 'Error 86-5 EMAIL NOT FOUND: incorrect password'
                ErrorBool = 1
                break

        if ErrorBool == 1:
            flash(message)
            return redirect('/')
        else:
            flash(name[0]['full_name'])
            return redirect('success.html')

    def success():
        return self.load_view('success.html')

