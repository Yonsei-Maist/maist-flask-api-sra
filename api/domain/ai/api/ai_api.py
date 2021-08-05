from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from lib.jwt import create_jwt_token, get_claims

from api.common.response.response_message import response_message
from api.domain.ai.service.ai_service import AIService

bp = Blueprint('ai', __name__, url_prefix='/ai')
ai_service = AIService()


class AIApi:

    @jwt_required()  # jwt check
    @cross_origin()  # cross origin check
    @bp.route('/', methods=['GET'])
    def ai_list(*args):
        claims = get_claims()  # get saved data in token
        return response_message(ai_service.ai_list())

    @cross_origin()
    @bp.route('/', methods=['POST'])
    def create(*args):
        ai_service.create(request.get_json())
        return response_message()

    @cross_origin()
    @bp.route('/<int:ai_id>', methods=['PUT'])
    def update(*args, ai_id):
        ai_service.update(ai_id, request.get_json())
        return response_message()

    @cross_origin()
    @bp.route('/<int:ai_id>', methods=['DELETE'])
    def delete(*args, ai_id):
        ai_service.delete(ai_id)
        return response_message()

    @cross_origin()
    @bp.route('/login', methods=['POST'])
    def login(*args):
        json = request.get_json()
        id = json['id']

        return create_jwt_token(id)  # create token
