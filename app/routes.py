from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    languages = [
        {
            'id': 1,
            'lang_name': 'Python',
            'difficulty': '2',
            'common_uses': ['Data Science', 'Finance', 'Web Applications'],
            'image': 'app/static/images/python.png'
        },
        {
            'id': 2,
            'lang_name': 'JavaScript',
            'difficulty': '2',
            'common_uses': ['Web Applications'],
            'image': 'app/static/images/javascript.png'

        },
        {
            'id': 3,
            'lang_name': 'Java',
            'difficulty': '4',
            'common_uses': ['Enterprise Applications', 'Web Applications'],
            'image': 'app/static/images/java.jpg'
        },
        {
            'id': 4,
            'lang_name': 'Swift',
            'difficulty': '3',
            'common_uses': ['Mobile Applications'],
            'image': 'app/static/images/swift.png'
        },
        {
            'id': 5,
            'lang_name': 'ReactJS',
            'difficulty': '3',
            'common_uses': ['Mobile Applications', 'Web Applications'],
            'image': 'app/static/images/react.png'
        },
        {
            'id': 6,
            'lang_name': 'Android',
            'difficulty': '4',
            'common_uses': ['Mobile Applications'],
            'image': 'app/static/images/android.png'
        }
    ]
    return render_template('index.html', title='Language Quick Reference Guide', languages=languages)

