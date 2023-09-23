import time
from flask_restx import Resource, Namespace
from .extentions import db
from .api_models import motion_model
from .models import Motion


ns = Namespace("api")

@ns.route("/motion")
class MotionAPI(Resource):
    @ns.marshal_list_with(motion_model)
    def get(self):
        return Motion.query.all()

    @ns.marshal_with(motion_model)
    def post(self):
        record = Motion()
        db.session.add(record)
        db.session.commit()
        return record, 201