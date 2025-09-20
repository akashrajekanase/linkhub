from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash

from . import db
from .forms import RegistrationForm
from .models import User

from flask import Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return '<h1> Welcome to LinkHub </h1>'

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        hashed_password = generate_password_hash(form.password.data,method='pbkdf2:sha256')

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash = hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Congratulations, You are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template('register.html',form=form)