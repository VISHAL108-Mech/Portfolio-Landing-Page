# Personal Name Card

A simple one-page personal website built with Flask. It shows my photo, name, role and links to my GitHub and LinkedIn profiles on a clean card.

I built it to get started with Flask: serving a page from Python, using templates, and working with static files like CSS and images. The design comes from a free HTML5 UP template, which I customized with my own details.

<img width="400" height="400" alt="Screenshot 2026-10-22 212142" src="https://github.com/user-attachments/assets/4cce1df8-ba9e-4e17-bb63-af25452c6904" />

## What it includes

- A profile photo, my name and my role
- Icon links to GitHub and LinkedIn
- A responsive layout that works on both desktop and mobile
- A short footer with the copyright and the template credit

## Built with

- Python 3
- Flask
- HTML and CSS (HTML5 UP template)

## Project structure

```
Name Card/
├── server.py            # Flask app
├── templates/
│   └── index.html       # the page itself
├── static/
│   ├── assets/          # CSS and fonts from the template
│   └── images/
│       └── vishal.png   # profile photo
└── README.md
```

Flask looks for HTML files in a folder called `templates` and for CSS, images and scripts in a folder called `static`, so the files need to be arranged like this.

## Setup

Install Flask:

```bash
pip install flask
```

Run the app:

```bash
python server.py
```

Then open `http://127.0.0.1:5000` in your browser.

## How it works

The whole app is one small file. It creates a Flask app and has a single route for the homepage, which renders `index.html`.

```python
from flask import Flask, render_template

server = Flask(__name__)


@server.route("/")
def home():
    """Render the homepage for the personal portfolio/name card."""
    return render_template("index.html")


if __name__ == "__main__":
    server.run(debug=True)
```

Debug mode is on, so the server reloads on its own whenever I change the code. That is handy while developing, but it should be turned off if the site is ever deployed.

The template loads its styles from the `static` folder and fills the card with my details:

```html
<header>
    <span class="avatar"><img src="static/images/vishal.png" alt="vishal_image"/></span>
    <h1>Vishal Yadav</h1>
    <p>Python Developer</p>
</header>

<footer>
    <ul class="icons">
        <li><a href="https://github.com/VISHAL108-Mech" class="fa-github">GitHub</a></li>
        <li><a href="https://www.linkedin.com/in/vishal-yadav-2a91a7428/" class="fa-linkedin">LinkedIn</a></li>
    </ul>
</footer>
```

## What I learned

- Setting up a basic Flask app and a route
- How Flask uses the `templates` and `static` folders
- Editing an existing HTML template to make it my own
- Running a development server with debug mode

## Things to improve

This is a learning project, so there are rough edges.

- Load the CSS and images with Flask's `url_for('static', ...)` instead of hardcoded paths
- Add an email link (there is a commented-out Gmail icon in the template)
- Add sections for my projects and skills, or link to the project READMEs
- Deploy it (PythonAnywhere, Render or similar) and add the live link here

## Credits

Design by [HTML5 UP](https://html5up.net).

## Author

**VISHAL YADAV**
- GitHub: [@VISHAL108-Mech](https://github.com/VISHAL108-Mech)
- LinkedIn: [vishal-yadav-2a91a7428](https://www.linkedin.com/in/vishal-yadav-2a91a7428)
- Email: [vy4122000@gmail.com](mailto:vy4122000@gmail.com)
