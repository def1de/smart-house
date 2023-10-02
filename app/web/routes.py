from flask import Blueprint, render_template, Response
from .camera import gen_frames

web = Blueprint("web", __name__, template_folder="templates", static_folder="static")

@web.route("/")
def index():
    return render_template("index.html")

@web.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')