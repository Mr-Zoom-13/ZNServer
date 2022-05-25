from flask_restful import reqparse

post_parser = reqparse.RequestParser()
post_parser.add_argument('email', required=True)
post_parser.add_argument('password', required=True)
post_parser.add_argument('surname', required=True)
post_parser.add_argument('name', required=True)
post_parser.add_argument('birthdate', required=True)
post_parser.add_argument('place_of_stay', required=True)
post_parser.add_argument('place_of_born', required=True)
post_parser.add_argument('age', required=True, type=int)
post_parser.add_argument('status', required=True)

get_parser = reqparse.RequestParser()
get_parser.add_argument('type')
get_parser.add_argument('email')
get_parser.add_argument('password')
