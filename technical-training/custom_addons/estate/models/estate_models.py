from odoo import fields, models, api
from datetime import date, timedelta


class Estate_Model(models.Model):
    _name = "estate.property"
    _description = "Test Model"

    name = fields.Char(required = True)
    discription = fields.Text()
    postcode = fields.Char()
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
    bedrooms = fields.Integer(default = '2')
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    date_availability = fields.Date(default=lambda self: fields.Date.today() + timedelta(days=90), copy=False)
    garden_orientation = directive = fields.Selection(string='garden_orientation', selection=[
        ('NORTH', 'North'),
        ('SOUTH', 'South'),
        ('EAST', 'East'),
        ('WEST', 'West')
        ], default='NORTH')

    active = fields.Boolean()