# -*- coding: utf-8 -*-
"""User views."""
import pandas as pd

from flask import Blueprint, render_template, request
from flask_login import login_required

from Budget.user.forms import UploadCSVForm
from Budget.utils import flash_errors

blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    """List members."""
    form = UploadCSVForm()
    return render_template("users/members.html", form=form)


@blueprint.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadCSVForm()
    if form.validate_on_submit():
        uploaded_file = form.csv_file.data
        if uploaded_file.filename != '':
            data = pd.read_csv(uploaded_file)
            return data.head().to_html()
    else:
        flash_errors(form)
    return render_template("users/members.html", form=form)
