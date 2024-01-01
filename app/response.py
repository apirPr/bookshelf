from flask import jsonify, make_response

def success(data, message):
  return make_response(jsonify({
    'status': 200,
    'message': message,
    'data': data
  }), 200)

def badRequest(data, message):
  return make_response(jsonify({
    'status': 400,
    'message': message,
    'data': data
  }), 400)

def unauthorized(data, message):
  return make_response(jsonify({
    'status': 401,
    'message': message,
    'data': data
  }), 401)

def notFound(data, message):
  return make_response(jsonify({
    'status': 404,
    'message': message,
    'data': data
  }), 404)