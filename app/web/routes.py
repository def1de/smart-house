from flask import Blueprint, render_template

web = Blueprint("web", __name__, template_folder="templates", static_folder="static")

@web.route("/")
def index():
    return render_template("index.html", data = [
        {'column1': 'Value1', 'column2': 'Value2', 'column3': 'Value3'},
        {'column1': 'Value4', 'column2': 'Value5', 'column3': 'Value6'}])