from flask_restful import reqparse

post_parser = reqparse.RequestParser()
post_parser.add_argument('email', required=True, location='args')
post_parser.add_argument('password', required=True, location='args')
post_parser.add_argument('surname', required=True, location='args')
post_parser.add_argument('name', required=True, location='args')
post_parser.add_argument('birthdate', required=True, location='args')
post_parser.add_argument('place_of_stay', required=True, location='args')
post_parser.add_argument('place_of_born', required=True, location='args')
post_parser.add_argument('age', required=True, type=int, location='args')
post_parser.add_argument('status', required=True, location='args')

get_parser = reqparse.RequestParser()
get_parser.add_argument('type', location='args')
get_parser.add_argument('email', location='args')
get_parser.add_argument('password', location='args')
