from flask import request
from flask_restful import Resource
from Model import db, Wallet, WalletSchema

wallets_schema = WalletSchema(many=True)
wallet_schema = WalletSchema()

class WalletResource(Resource):
    def get(self):
        wallets = Wallet.query.all()
        wallets = wallets_schema.dump(wallets).data
        return {
            'status': 'success', 'data': 'wallets'
        }, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = wallet_schema.load(json_data)

        if errors:
            return errors, 422
        userwallet = (
            db.session.query(Wallet)
            .filter(Topic.Subject.has(Subject.accountID.in_(usersID)))
            .all())

        if userwallet:
            return {'message': "user wallet exist already"}, 400
        userwallet = Wallet(
            profileID=json_data['profileID'],
            totalbalance=json_data['totalbalance'],
            list_of_coin=json_data['list_of_coin={}']
        )
        db.session.add(userwallet)
        db.session.commit()
        result = wallet_schema.dump(userwallet).data
        return { 'status': 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_jason(force=True)
        if not json_data:
            return {'message': 'data is not json'}, 400
        data, errors = wallet_schema.load(json_data)

        if errors:
            return errors, 422
        userwallet = Wallet,query.filter_by(profileID=data['profileID'])

        if not userwallet:
            return {'message': 'userwallet does not exist'}
        userwallet.totalbalance=data['totalbalance']
        userwallet.list_of_coin=data['list_of_coin']
        db.session.commit()
        result = wallet_schema.dump(userwallet).data
        return  {'status': 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = wallet_schema.load(json_data)

        if errors:
            return errors, 422
        user = Wallet.query.filter_by(profileID=data['profileID']).delete()
        db.session.commit()
        result = wallet_schema.dump(user).data
        return { "status": 'success', 'data': result}, 204






