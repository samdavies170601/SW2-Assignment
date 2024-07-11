from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class ToDoForm(FlaskForm):
    item = StringField("Item") # validators=[DataRequired()])
    # priority = IntegerField("Priority", validators=[DataRequired()])
    submit = SubmitField("Submit")

    # def validate_priority(self, priority):
    #     if priority.data not in range(0, 11):
    #         raise ValidationError("The priority needs to be between 0 and 10 inclusive.")


class ToDoFileUploadForm(FlaskForm):
    todo_file = FileField("New ToDo File", validators=[FileAllowed(["txt"])])
    submit = SubmitField("Upload File")
