from flask import Flask, request
from flask_restful import Resource, Api
from iptv import *

app = Flask(__name__)
api = Api(app)


class IPTVApi(Resource):
    def get(self):
        name = request.args.get('name')
        search_type = request.args.get('search_type')
        if search_type == "lang":
            return get_by_lang(name)
        elif search_type == "country":
            return get_by_country(name)
        elif search_type == "name":
            return get_by_name(name)
        else:
            return get_by_category(name)


api.add_resource(IPTVApi, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
