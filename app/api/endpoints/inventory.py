from flask import request
from flask_restx import Namespace, Resource, fields

api = Namespace('inventory', description='Inventory operations')

# Create db
db = []

# --- MODELS ---

# Inventory models for API documentation
inventory_model = api.model('Inventory', {
    'id': fields.Integer,
    'name': fields.String,
    'quantity': fields.Integer,
    'ppu': fields.Float,
    'isAvailable': fields.Boolean
})

inventory_list_model = api.model('InventoryList', {
    'inventory': fields.List(fields.Nested(inventory_model)),
    'total': fields.Integer
})

# --- ROUTES ---
@api.route('/')
class InventoryList(Resource):
    @api.doc("list_inventory")
    @api.marshal_with(inventory_list_model)
    def get(self):
        '''
        Returns a list of all inventory items
        '''
        return {
            'inventory': db,
            'total': len(db)
        }
    
    @api.doc('create_inventory')
    @api.expect(inventory_model)
    @api.marshal_with(inventory_model, code=201)
    def post(self):
        '''
        Creates a new inventory item
        '''
        return True
    
@api.route('/<int:id>')
@api.param('id', 'The inventory ID')
@api.response(404, 'Inventory item not found')
class Inventory(Resource):
    @api.doc('get_inventory')
    @api.marshal_with(inventory_model)
    def get(self, id):
        '''
        Returns an inventory item
        '''
        return True
    
    @api.doc('update_inventory')
    @api.expect(inventory_model)
    @api.marshal_with(inventory_model)
    def put(self, id):
        '''
        Updates an inventory item
        '''
        return True
    
    @api.doc('delete_inventory')
    @api.response(204, 'Inventory item deleted')
    def delete(self, id):
        '''
        Delete an inventory item
        '''
        return 204
    