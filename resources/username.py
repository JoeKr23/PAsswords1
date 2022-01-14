from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.username import UsernameModel


class Username(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('domain_id',
                        type=int,
                        required=True,
                        help="Every username needs a domain_id."
                        )

    @jwt_required()
    def get(self, name):
        username = UsernameModel.find_by_name(name)
        if username:
            return username.json()
        return {'message': 'Username not found'}, 404

    def post(self, name):
        if UsernameModel.find_by_name(name):
            return {'message': "Username '{}' already exists.".format(name)}, 400

        data = Username.parser.parse_args()

        username = UsernameModel(name, **data)

        try:
            username.save_to_db()
        except:
            return {"message": "An error occurred inserting the username."}, 500

        return username.json(), 201

    def delete(self, name):
        username = UsernameModel.find_by_name(name)
        if username:
            username.delete_from_db()
            return {'message': 'Username deleted.'}
        return {'message': 'Username not found.'}, 404

    def put(self, name):
        data = Username.parser.parse_args()

        username = UsernameModel.find_by_name(name)

        if username:
            username.password = data['password']
        else:
            username = UsernameModel(name, **data)

        username.save_to_db()

        return username.json()


class UsernameList(Resource):
    def get(self):
        return {'username': list(map(lambda x: x.json(), UsernameModel.query.all()))}
