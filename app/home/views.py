from flask import render_template, redirect, request

from . import home

from ..models import Image, Description

@home.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Image.query.paginate(page=page, per_page=10, error_out=False)
    images = pagination.items
    return render_template('home/index.j2', images=images, pagination=pagination)