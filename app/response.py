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

def not_found(data, message):
  return make_response(jsonify({
    'status': 404,
    'message': message,
    'data': data
  }), 404)

def created(data, message):
  return make_response(jsonify({
    'status': 201,
    'message': message,
    'data': data
  }), 201)

def internal_server_error(data, message):
  return make_response(jsonify({
    'status': 500,
    'message': message,
    'data': data
  }), 500)

def conflict(data, message):
  return make_response(jsonify({
    'status': 409,
    'message': message,
    'data': data
  }), 409)