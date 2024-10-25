from odoo import api, models, fields


class RestaurantChef(models.Model):
    _name = "restaurant.chef"
    _description = "Restaurant Chef Description"

    name = fields.Char('Name', required=True)