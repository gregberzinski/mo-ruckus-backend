from flask import Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Mo Ruckus Backend is Live!'
