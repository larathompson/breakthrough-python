import os
from flask import Flask, render_template
from seeds import blog_posts
import requests

os.environ['FLASK_DEBUG'] = '1'
os.environ['FLASK_ENV'] = 'development'

from flask import Flask, render_template
from seeds import blog_posts

from services.country_service import CountryService

app = Flask(__name__)


countries = CountryService.get_all_countries()
print(countries, " i am a list of all the countries")

spain = CountryService.get_country_by_name('spain')
print(spain, "Spain info:")

european_countries = CountryService.get_countries_for_region('europe')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/countries')
def countries():
    return render_template('countries.html', countries=countries, european_countries=european_countries)

if __name__ == '__main__':
    app.run(debug=True)