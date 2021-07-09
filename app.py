from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create flask instance
app = Flask(__name__)

# Establish Mongo Connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/scraper_mars")


# Route to render the index.html
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_database = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", scrape_mars=mars_database)


# function scraping
@app.route("/scrape")
def scrape():

    # Run the scraper function
    mars_function= scrape_mars.scrape()

    # Update the Mongo database and upsert=True
    mongo.db.collection.update({}, mars_function, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)