from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars
import os

# Create an instance of Flask
app =Flask(__name__)



# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#app.config["MONGO_URI"] = os.environ.get('authentication')
#mongo = PyMongo(app)
# Route to render index.html template using data from Mongo

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_info= mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars_info=mongo.db.mars_info
    # Run the scrape function
    
    mars_content=scrape_mars.scrape_mars_news()
    mars_content=scrape_mars.scrape_img()
    mars_content=scrape_mars.scrape_weather()
    mars_content=scrape_mars.scrape_facts()
    mars_content=scrape_mars.scrape_hemisphere()

    # Update the Mongo database using update and upsert=True
    mars_info.update({}, mars_content, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
