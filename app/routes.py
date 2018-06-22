from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    languages = [
        {
            'lang_name': 'Python',
            'difficulty': '2',
            'common_uses': ['Data Science', 'Finance', 'Web Applications', 'Infrastructure'],
            'image': 'app/static/images/python.png'
        },
        {
            'lang_name': 'JavaScript',
            'difficulty': '2',
            'common_uses': ['Web Applications'],
            'image': 'app/static/images/javascript.png'

        },
        {
            'lang_name': 'Java',
            'difficulty': '4',
            'common_uses': ['Enterprise Applications', 'Web Applications'],
            'image': 'app/static/images/java.jpg'
        },
        {
            'lang_name': 'Swift',
            'difficulty': '3',
            'common_uses': ['Mobile Applications'],
            'image': 'app/static/images/swift.png'
        },
        {
            'lang_name': 'ReactJS',
            'difficulty': '3',
            'common_uses': ['Mobile Applications', 'Web Applications'],
            'image': 'app/static/images/react.png'
        },
        {
            'lang_name': 'Android',
            'difficulty': '4',
            'common_uses': ['Mobile Applications'],
            'image': 'app/static/images/android.png'
        }
    ]
    return render_template('index.html', title='Language Quick Reference Guide', languages=languages)

