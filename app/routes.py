from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    languages = [
        {
            'lang_name': 'Python',
            'difficulty': '2',
            'common_uses': ['Data Science', 'Finance', 'Web Applications', 'Infrastructure']
        },
        {
            'lang_name': 'JavaScript',
            'difficulty': '2',
            'common_uses': ['Web Applications']

        },
        {
            'lang_name': 'Java',
            'difficulty': '4',
            'common_uses': ['Enterprise Applications', 'Web Applications']
        },
        {
            'lang_name': 'Swift',
            'difficulty': '3',
            'common_uses': ['Mobile Applications']
        },
        {
            'lang_name': 'ReactJS',
            'difficulty': '3',
            'common_uses': ['Mobile Applications', 'Web Applications']
        },
        {
            'lang_name': 'Android',
            'difficulty': '4',
            'common_uses': ['Mobile Applications']
        }
    ]
    return render_template('index.html', title='Language Quick Reference Guide', languages=languages)

