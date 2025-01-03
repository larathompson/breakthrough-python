# Project Setup

If you want, you can view this Readme in a nicer way by pressing Ctrl+Shift+V (or Cmd+Shift+V on macOS) to see a live preview. Otherwise, you can just read it here in your text editor.

Follow the steps below to get the project running. When it says `[project-name]` replace it with the name of the project. When it says bash, it means you should use the terminal to run the command. You do NOT need to write bash or ```.

Before you begin, ensure you have the following installed on your computer:

**Python**: You need Python 3.6 or later. You can download it from the [official Python website](https://www.python.org/downloads/). Make sure to check the box that says "Add Python to PATH" during installation.

**Git**: This is required to clone the repository. You can download it from the [official Git website](https://git-scm.com/downloads).

1. Clone repo:
   `git clone [repo-url]`

2. Navigate to the project and create a virtual environment:
   Note - a virtual environment is a way to easily setup all the dependencies for the project.

```bash
cd python-challenge
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

If the above has been successful, you should see (venv) ➜ python-challenge at the start of your terminal.

3.  This command will install all the dependencies listed in the requirements.txt file.

````bash
pip install -r requirements.txt

4. This will run the flask app. Flask is a web framework for python.
```bash
flask run

5. then visit http://localhost:5000
````

# What is the project?

This is a simple web app that has various pages. It has a welcome page, a blog page and a countries page that allows you to view information about countries. It uses the [REST Countries API](https://restcountries.com/) to get the data. During the project, you can edit both the backend and frontend code and make changes to the app.

# What do the different files do?

- `app.py` is the main file that runs the Flask app. It initializes the application and starts the server.
- `routes.py` is the file that defines the routes. Routes are the different URLs that the app can handle, and they determine what content is displayed when a user visits a specific URL.
- `requirements.txt` is the file that lists the dependencies. These are the external libraries and packages that the project needs to function correctly. You can install them using `pip install -r requirements.txt`.
- `templates` is the folder that contains the HTML templates. These templates define the structure of the web pages.
- `static` is the folder that contains the static files. This is where the CSS, JavaScript, and image files are stored. These files help style the web pages and add interactivity.
- `seeds.py` contains sample data for the blog posts. You can add new blog posts, update existing ones, or add more fields like the author or the number of views.
- `country_service.py` is responsible for interacting with the REST Countries API. It fetches data about countries, which is then used to display information on the countries page of the web app.

# How does the code flow?

1. **Starting the Application**:

   - The application begins with `app.py`, which initializes the Flask app and starts the server. This file sets up the environment for the web application to run.

2. **Handling Requests**:

   - When a user visits a URL, `routes.py` determines which function should handle the request. Each route corresponds to a specific URL and is linked to a function that processes the request and returns a response.

3. **Fetching Data**:

   - If the request involves displaying country information, `country_service.py` is used to fetch data from the REST Countries API. This data is then processed and sent back to the user.

4. **Rendering Web Pages**:

   - The HTML templates in the `templates` folder are used to render the web pages. These templates are filled with data and sent to the user's browser to display the content.

5. **Styling and Interactivity**:

   - The `static` folder contains CSS and JavaScript files that style the web pages and add interactivity, such as animations or dynamic content updates.

6. **Managing Dependencies**:

   - The `requirements.txt` file lists all the external libraries needed for the project. These are installed in the virtual environment to ensure the app runs smoothly.

7. **Sample Data**:
   - `seeds.py` provides sample data for blog posts, which can be displayed on the blog page. This file can be modified to add or update blog content.

This flow should help you understand how different parts of the codebase interact to create a functioning web application. If you have any specific questions or need further details, feel free to ask!

# Tasks

Take a look through the code and see if you can understand how it works. Then, try to complete some of the tasks below. Also feel free to make any other changes you would like!

## Home page

1. Can you edit the text on the homepage?
2. Can you add an image to the homepage?
3. Can you change the colour of the font?

## Blog page

1. Can you add a new blog post?
2. Can you edit the text of an existing blog post?
3. Can you add an image to a blog post?
4. Can you add a new field to the blog post?

## Countries page

1. Can you change the layout of the countries page? Look at the blog page for an example.
2. Can you add a new language field to the countries page?
3. Can you filter for another region apart from Europe?

## General

1. Can you add a new page?
   1. Can you add a new page to the navigation bar?
   2. Can you add a new route to the app?
   3. Can you add a new template to the templates folder?
2. Can you some styles to the layout which show on all pages?

# Tools to help

- [REST Countries API](https://restcountries.com/). This is the API that we are using. You can call diffferent endpoints to get different data about countries.
- Keep checking the terminal and the UI to check that your app is working as expected.
- Ways to get help:
  - ask other people in the group
  - google
  - ChatGPT
  - follow through other code examples
