from flask_restful import Resource
from models.domain import DomainModel


class Domain(Resource):
    def get(self, name):
        domain = DomainModel.find_by_name(name)
        if domain:
            return domain.json()
        return {'message': 'Domain not found'}, 404

    def post(self, name):
        if DomainModel.find_by_name(name):
            return {'message': "A domain with name '{}' already exists.".format(name)}, 400

        domain = DomainModel(name)
        try:
            domain.save_to_db()
        except:
            return {"message": "An error occurred creating the domain."}, 500

        return domain.json(), 201

    def delete(self, name):
        domain = DomainModel.find_by_name(name)
        if domain:
            domain.delete_from_db()

        return {'message': 'Domain deleted'}


class DomainList(Resource):
    def get(self):
        return {'domain': list(map(lambda x: x.json(), DomainModel.query.all()))}
