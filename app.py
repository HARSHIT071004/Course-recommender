
from flask import Flask, render_template, request, jsonify
from model import CourseRecommender
import os

app = Flask(__name__)
CSV_PATH = os.path.join(os.path.dirname(__file__), 'data', 'courses.csv')
recommender = CourseRecommender(CSV_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/courses')
def get_courses():
    return jsonify({'courses': recommender.get_courses()})

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    course_name = data.get('course_name', '')
    recs = recommender.recommend(course_name)
    return jsonify({'recommendations': recs})

if __name__ == '__main__':
    app.run(debug=True)
