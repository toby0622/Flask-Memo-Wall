from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # looking for specific entry of the database
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged In Successfully!', category='success')
                # remember the user login session until session closed
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, Please Try Again.', category='error')
        else:
            flash('Email Does Not Exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        # check for restrictions
        if user:
            flash('Email Already Exists.', category='error')
        elif len(email) < 4:
            flash('Email Address Must Be Greater Than 3 Characters.', category='error')
        elif len(nickname) < 2:
            flash('Nickname Must Be Greater Than 1 Character.', category='error')
        elif password1 != password2:
            flash('Passwords Do Not Match.', category='error')
        elif len(password1) < 7:
            flash('Password Must Be At Least 7 Characters.', category='error')
        else:
            # add user to database
            new_user = User(email=email, nickname=nickname
                            , password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)
