"""Driver for Web server"""
from flask import Flask
from views import app

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=False,host='127.0.0.1',port='5000')
