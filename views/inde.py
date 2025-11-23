import os
import threading

from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for

home = Blueprint('home', __name__)
@home.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')