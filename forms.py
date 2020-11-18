from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from marksheet.models import Marksheet

class Marksheetform(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired(), Length(min=2, max=20)])
    rollno = IntegerField('ROll No', validators=[DataRequired()])
    maths = IntegerField("Maths Mark", validators=[DataRequired()])
    science = IntegerField("Science Mark", validators=[DataRequired()])
    english = IntegerField("English Mark", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

    # def validate_rollno(self, rollno):
    #     user = Marksheet.query.filter_by(rollno=rollno.data).first()
    #     if user:
    #         raise ValidationError("That rollno is already taken")

class Updatemarksheetform(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired(), Length(min=2, max=20)])
    rollno = IntegerField('ROll No', validators=[DataRequired()])
    maths = IntegerField("Maths Mark", validators=[DataRequired()])
    science = IntegerField("Science Mark", validators=[DataRequired()])
    english = IntegerField("English Mark", validators=[DataRequired()])
    submit = SubmitField("Update")