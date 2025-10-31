# This code imports the Flask library and some functions from it.
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf


# Create a Flask application instance
app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Required for CSRF protection
csrf = CSRFProtect(app)  # This automatically protects all POST routes

@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf())


# Global variable for site name: Used in templates to display the site name
siteName = "SHU EFSSD Module"
# Set the site name in the app context
@app.context_processor
def inject_site_name():
    return dict(siteName=siteName, p2 = "This is page 2")


# Routes
#===================
# These define which template is loaded, or action is taken, depending on the URL requested
#===================
# Home Page
@app.route('/')
def index():
    # This defines a variable 'studentName' that will be passed to the output HTML
    studentName = "SHU Student"
    # Render HTML with the name in a H1 tag
    #return render_template('index.html', title="Welcm", username = studentName)
    return render_template('index.html', title="Welcome", username=studentName)

# About Page
@app.route('/about/')
def about():
    # Render HTML with the name in a H1 tag
    return render_template('about.html', title="About EFSSD")

# Register Page
# Register Page
@app.route('/register/', methods=('GET', 'POST'))
def register():

    # If the request method is POST, process the form submission
    if request.method == 'POST':

        flash(category='success', message='The Form Was Posted Successfully!')
        return render_template('register.html', title="Register")
    
    # If the request method is GET, just render the registration form
    return render_template('register.html', title="Register")





# Run application
#=========================================================
# This code executes when the script is run directly.
if __name__ == '__main__':
    print("Starting Flask application...")
    print("Open Your Application in Your Browser: http://localhost:81")
    # The app will run on port 81, accessible from any local IP address
    app.run(host='0.0.0.0', port=81)
