from flask import Flask, jsonify, request, abort
from api.v1.auth.auth import Auth
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
auth = None
auth = Auth()

@app.errorhandler(404)
def not_found(error) -> str:


    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404
@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def before_request() -> str:
    """Filter each request before it's handled by the proper route"""
    if auth is None:
        return
        
    excluded_paths = ['/api/v1/status/',
                     '/api/v1/unauthorized/',
                     '/api/v1/forbidden/']
                     
    if not auth.require_auth(request.path, excluded_paths):
        return
        
    if auth.authorization_header(request) is None:
        abort(401)
        
    if auth.current_user(request) is None:
        abort(403)


