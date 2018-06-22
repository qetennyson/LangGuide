from flask_wtf import FlaskForm
from wtforms import Form, SelectField


class SearchForm(FlaskForm):
    choices = [('Data Science', 'Data Science'),
               ('Mobile Apps', 'Mobile Apps'),
               ('Desktop Apps', 'Desktop Apps'),
               ('Web Apps', 'Web Apps')]
    select = SelectField('Filter languages:', choices=choices)
