"""Driver for Web server"""

from views import app

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='0.0.0.0', port='5000')