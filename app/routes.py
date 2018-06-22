from flask import render_template
from app import langDict
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
            'image': 'app/static/images/python.png',
            'diff_expanded': langDict.python['difficulty'],
            'requirements': langDict.python['requirements'],
            'certifications': langDict.python['certifications'],
            'libraries': langDict.python['libraries'],
            'pop_apps': langDict.python['pop_apps'],
        },
        {
            'id': 2,
            'lang_name': 'JavaScript',
            'difficulty': '2',
            'common_uses': ['Web Applications', 'Scripting'],
            'image': 'app/static/images/javascript.png',
            'diff_expanded': langDict.javascript['difficulty'],
            'requirements': langDict.javascript['requirements'],
            'certifications': langDict.javascript['certifications'],
            'libraries': langDict.javascript['libraries'],
            'pop_apps': langDict.javascript['pop_apps'],

        },
        {
            'id': 3,
            'lang_name': 'Java',
            'difficulty': '4',
            'common_uses': ['Enterprise Applications', 'Web Applications'],
            'image': 'app/static/images/java.jpg',
            'diff_expanded': langDict.java['difficulty'],
            'requirements': langDict.java['requirements'],
            'certifications': langDict.java['certifications'],
            'libraries': langDict.java['libraries'],
            'pop_apps': langDict.java['pop_apps'],
        },
        {
            'id': 4,
            'lang_name': 'Swift',
            'difficulty': '3',
            'common_uses': ['Mobile Applications'],
            'image': 'app/static/images/swift.png',
            'diff_expanded': langDict.swift['difficulty'],
            'requirements': langDict.swift['requirements'],
            'certifications': langDict.swift['certifications'],
            'libraries': langDict.swift['libraries'],
            'pop_apps': langDict.java['pop_apps'],
        },
        {
            'id': 5,
            'lang_name': 'ReactJS',
            'difficulty': '3',
            'common_uses': ['Mobile Applications', 'Web Applications'],
            'image': 'app/static/images/react.png',
            'diff_expanded': langDict.react['difficulty'],
            'requirements': langDict.react['requirements'],
            'certifications': langDict.react['certifications'],
            'libraries': langDict.react['libraries'],
            'pop_apps': langDict.react['pop_apps'],
        },
        {
            'id': 6,
            'lang_name': 'Android',
            'difficulty': '4',
            'common_uses': ['Mobile Applications'],
            'image': 'app/static/images/android.png',
            'diff_expanded': langDict.android['difficulty'],
            'requirements': langDict.android['requirements'],
            'certifications': langDict.android['certifications'],
            'libraries': langDict.android['libraries'],
            'pop_apps': langDict.android['pop_apps'],
        }
    ]
    return render_template('index.html', title='Language Quick Reference Guide', languages=languages)
