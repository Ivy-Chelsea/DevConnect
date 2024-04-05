from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from scp.models import User
from flask_wtf.file import FileAllowed


class SignupForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists, choose a different one!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists, try a different one!')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed('jpg', 'png')])
    submit = SubmitField('Update')


class TaskForm(FlaskForm):
    title = StringField('title',
                        validators=[DataRequired(), Length(min=3, max=20)])
    description = TextAreaField('description', validators=[DataRequired()])
    due_date = TextAreaField('due_date', validators=[DataRequired()])
    start = TextAreaField('start', validators=[DataRequired()])
    end = TextAreaField('end', validators=[DataRequired()])
    reminder_date = TextAreaField('reminder_date', validators=[DataRequired()])
    priority = TextAreaField('priority', validators=[DataRequired()])
    submit = SubmitField('create')


class ChatForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=20)])
    code = StringField('code',
                        validators=[DataRequired(), Length(min=3, max=10)])
    join = SubmitField('join', False)
    create = SubmitField('create', False)


class RequestResetForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
