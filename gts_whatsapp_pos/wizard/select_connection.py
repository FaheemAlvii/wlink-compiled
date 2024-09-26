from odoo import fields, api, models
from ..global_py import Config


class SelectConnection(models.TransientModel):
    _name = "gts_whatsapp_pos.select_connection"

    connection = fields.Many2one('whatsapp.connection', string="Whatsapp Connection", required=True)

    @api.model
    def get_selected_connection(self):
        connection_id = Config().get('pos_connection')
        connection = self.env['whatsapp.connection'].search([('id', '=', connection_id)], limit=1)
        return connection

    @api.model
    def default_get(self, fields):
        result = super(SelectConnection, self).default_get(fields)

        connection = self.get_selected_connection()

        if connection:
            result['connection'] = connection

        return result

    @api.onchange('connection')
    def onchange_connection(self):
        if self.connection:
            Config().set('pos_connection', self.connection)