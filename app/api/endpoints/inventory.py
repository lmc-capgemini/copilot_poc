from flask import request
from flask_restx import Namespace, Resource, fields

api = Namespace('inventory', description='Inventory operations')

# Create db
db = [
    {
        'id': 0,
        'name': 'Luminous',
        'quantity': 220,
        'ppu': 12.50,
    },
    {
        'id': 1,
        'name': 'Orbital',
        'quantity': 1130,
        'ppu': 11.11,
    },
    {
        'id': 2,
        'name': 'James',
        'quantity': 464,
        'ppu': 19.84,
    }
]

# --- MODELS ---

# Inventory models for API documentation
inventory_model = api.model('Inventory', {
    'id': fields.Integer,
    'name': fields.String,
    'quantity': fields.Integer,
    'ppu': fields.Float,
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
        data = request.json
        new_inventory = {
            'id': len(db),
            'name': data['name'],
            'quantity': data['quantity'],
            'ppu': data['ppu']
        }
        db.append(new_inventory)
        return new_inventory, 201
    
    
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
        for item in db:
            if item['id'] == id:
                return item


    @api.doc('update_inventory')
    @api.expect(inventory_model)
    @api.marshal_with(inventory_model)
    @api.response(404, 'Inventory item not found')
    def put(self, id):
        '''
        Updates an inventory item
        '''
        data = request.json

        for item in db:
            if item['id'] == id:
                item['name'] = data['name']
                item['quantity'] = data['quantity']
                item['ppu'] = data['ppu']

                return item


    @api.doc('delete_inventory')
    @api.response(204, 'Inventory item deleted')
    @api.response(404, 'Inventory item not found')
    def delete(self, id):
        '''
        Delete an inventory item
        '''
        for item in db:
            if item['id'] == id:
                db.remove(item)
                return "Inventory item removed"