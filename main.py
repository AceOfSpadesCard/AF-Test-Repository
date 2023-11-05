# Import flask and render_template for rendering the HTML Scripts
from flask import Flask, render_template, request

# Initialize the Web Application
app = Flask(__name__)


# Create a route for the application
@app.route('/')
# Opening up the webpage by default will trigger this function and cause it to run
def index():
    return render_template('index.html')


# If the program is executed, then run this application
if __name__ == "__main__":
    # Auto refreshes the web application whenever a change is made to it
    app.debug = True
    # Runs the application
    app.run()

# By default, the application will run on port 5000 of your computer
# http://127.0.0.1:5000
