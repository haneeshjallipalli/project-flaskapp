#import flask

from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the home route
@app.route("/bilal")
def home():
    return "<h1>Welcome to My Flask App! BILAL </h1><p>This is a simple Flask application.</p>"

@app.route("/haneesh")
def functionality():
    return "<h1>Welcome to the functionality</h1>"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)