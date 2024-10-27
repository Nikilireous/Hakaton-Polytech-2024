from flask import url_for, render_template, redirect, flash, abort
from flask import Blueprint, g, session, request
from werkzeug.security import check_password_hash
import functools
from db import *

bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
			if g.user is None:
					return redirect(url_for("auth.login"))

			return view(**kwargs)

	return wrapped_view


@bp.before_app_request
def load_logged_in_user():
	user_id = session.get("user_id")
	g.is_admin = session.get("is_admin")

	if user_id is None:
			g.user = None
	else:
			g.user = (get_user_by_id(user_id))


@bp.route('/login', methods=('GET', 'POST'))
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		error = None
		user = get_user_by_name(username)

		if user is None:
			error = 'Неверное имя пользователя'
		elif not check_password_hash(user['password'], password):
			error = 'Неверный пароль'

		if error is None:
			session.clear()
			session['user_id'] = user['id']
			return redirect(url_for('routing.admin_panel'))
		flash(error)

	return render_template('public/login.html')


@bp.route("/logout")
def logout():
	session.clear()
	return redirect(url_for("index"))