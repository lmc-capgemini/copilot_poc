from flask import Blueprint
from flask_restx import Api

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(
    api_bp,
    version='1.0',
    title='Github Copilot POC API',
    description='A RESTful API for Copilot POC',
    doc='/docs'
)

# Import and add namespaces
from .endpoints.inventory import api as inventory_ns
api.add_namespace(inventory_ns)