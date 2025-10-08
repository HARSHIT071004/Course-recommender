# Course Recommender

A Python Flask web application that recommends courses based on user preferences. Built with `Flask`, `pandas`, and `scikit-learn`.  

This project is designed to provide personalized course suggestions in a simple web interface.

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment on Render](#deployment-on-render)
- [Technologies](#technologies)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Recommend courses based on user input.
- Simple, responsive web interface.
- Powered by `pandas` and `scikit-learn` for data processing and ML logic.
- Easy deployment to cloud platforms like Render.

---

## Demo

**Live Deployment (Render)**: [https://udemy-harshit-course-recommender.onrender.com](https://udemy-harshit-course-recommender.onrender.com)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/HARSHIT071004/Course-recommender.git
cd Course-recommender
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Flask app locally:

bash
Copy code
python app.py
Or using gunicorn for production:

bash
Copy code
gunicorn app:app
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
Deployment on Render
Make sure requirements.txt contains:

shell
Copy code
Flask>=2.0
scikit-learn
pandas
gunicorn
Push all changes to GitHub:

bash
Copy code
git add .
git commit -m "Prepare for deployment"
git push origin main
On Render:

Create a New Web Service.

Select Python 3 as environment.

Connect your GitHub repo (Course-recommender).

Branch: main.

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Deploy the service.

After successful deployment, visit your live URL.

Technologies
Python 3

Flask

pandas

scikit-learn

gunicorn (for production deployment)

Folder Structure
csharp
Copy code
Course-recommender/
│
├── app.py               # Main Flask app
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── requirements.txt     # Dependencies
└── README.md
Contributing
Contributions are welcome!

Fork the repository

Create a new branch

Make your changes

Submit a Pull Request
By- Harshit Sharma
License
This project is licensed under the MIT License.
