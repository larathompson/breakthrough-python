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

spain = CountryService.get_country_by_name('spain')
# print(spain, "Spain info:")

germany = CountryService.get_country_by_name('germany')
# print(germany, "Germany info:")

countriesList = spain + germany



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/countries')
def countries():
    print(type(countries)) 
    return render_template('countries.html', countries=countriesList)

if __name__ == '__main__':
    app.run(debug=True)