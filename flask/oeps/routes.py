from flask import Blueprint, redirect, url_for, request, render_template, flash

api = Blueprint('api', __name__)

@api.route("/")
def hello_world():
    return "<p>Hello, World!</p>"