from flask_restx import fields
from .extentions import api

motion_model = api.model("Motion", {
    "id": fields.Integer,
    "time": fields.DateTime
})