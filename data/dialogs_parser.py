from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, location='args')
parser.add_argument('avatar', required=True, location='args')
