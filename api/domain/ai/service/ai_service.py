from datetime import datetime

from api import db
from api.domain.ai.model.ai_model import AI, AISchema, AIRequestSchema
from api.domain.ai.dao.ai_dao import AIDao

ai_dao = AIDao()


class AIService:

    def ai_list(self):
        ai_list = AI.query.order_by(AI.create_date.desc())
        ai_schema = AISchema(many=True)
        ai = ai_schema.dump(ai_list)
        return ai

    # SQLAlchemy 사용
    def create(self, payload):
        ai_schema = AIRequestSchema()
        payload = ai_schema.load(payload)
        ai = AI(subject=payload["subject"], content=payload['content'], create_date=datetime.now())
        db.session.add(ai)
        db.session.commit()

    # MySQL-Connector 사용
    #def create(self, payload):
    #    ai_dao.create(payload)

    def update(self, ai_id, payload):
        ai_schema = AIRequestSchema()
        payload = ai_schema.load(payload)
        ai = AI.query.get(ai_id)
        ai.subject = payload["subject"]
        ai.content = payload['content']
        db.session.commit()

    def delete(self, ai_id):
        ai = AI.query.get(ai_id)
        db.session.delete(ai)
        db.session.commit()