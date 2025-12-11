from flask import request
from flask_restx import Namespace, Resource, fields

api = Namespace('inventory', description='Inventory operations')

# Create db
db = []

# --- MODELS ---


# --- ROUTES ---
@api.route('/')
class InventoryList(Resource):
    def get(self):
        '''
        Returns a list of all inventory items
        '''
        return db
    
    def post(self):
        '''
        Creates a new inventory item
        '''
        return True
    

@api.route('/<int:id>')
class Inventory(Resource):
    def get(self, id):
        '''
        Returns an inventory item
        '''
        return True
    
    def put(self, id):
        '''
        Updates an inventory item
        '''
        return True
    
    def delete(self, id):
        '''
        Delete an inventory item
        '''
        return True
    