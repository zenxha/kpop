"""Driver for Web server"""
import json
from views import app, db
with open('config.json') as file:
    config = json.load(file)


if __name__ == "__main__":
    # runs the application on the repl development server
    db.create_all()
    app.secret_key = 'heyheyhey'
    app.run(debug=True, host=config["host"], port=config["port"])