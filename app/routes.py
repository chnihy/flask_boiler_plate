from app import app
from flask import Flask, render_template, url_for


@app.route('/')
@app.route('/index')
	return render_template('index.html')


