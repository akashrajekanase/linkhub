from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from . import db
from .forms import RegistrationForm, LoginForm
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

@main_bp.route('/login',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash,form.password.data):
            login_user(user,remember=form.remember_me.data)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password')
    return render_template('login.html',form=form)

@main_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return f'<h1> Welcome to your dashboard, {current_user.username}!</h1>'