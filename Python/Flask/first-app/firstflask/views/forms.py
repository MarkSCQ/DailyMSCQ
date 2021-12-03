from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from firstflask.models.model import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("User exists, use another name")

    def validate_email_address(self, email_address_to_check):

        email = User.query.filter_by(
            email_address=email_address_to_check.data).first()
        if email:
            raise ValidationError("Email exists, use another email")

    username = StringField(label='User Name', validators=[
                           Length(min=2, max=30), DataRequired()])

    email_address = StringField(label='Email', validators=[
                                Email(), DataRequired()])

    password1 = PasswordField(label='Password', validators=[
                              Length(min=6), DataRequired()])

    password2 = PasswordField(label='Password Confirmation',
                              validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label='Create Account')

    # the naming for the validation functions follows some rules,
    # the flask validation system will check the the function whose name is like validate_[field name]
    # and then it will use this function to check the field


class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Buy it')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell it')
