import ast
import sys
import os
from odoo import api, fields, models
from .template import Template
from ..global_py import Config


class MessageMenu(models.TransientModel):
    _name = 'whatsapp_contacts.messaging_menu'
    _description = 'Messaging Menu'

    def get_default(self):
        default_connection = Config().get('default_connection')

        if default_connection:
            return default_connection

        return False

    connection = fields.Many2one('whatsapp.connection', default=get_default, string='Whatsapp Connection', required=True)
    send_to = fields.Many2one('res.partner', string='Send to', required=True)
    message = fields.Text(string='Message')

    # Template mode
    template_paths = fields.Char(string='Paths')
    document_name = fields.Char(string='Document Name')
    document_filename = fields.Char(string='Document Filename')
    user_id = fields.Integer(string='Res Id')

    @api.model
    def default_get(self, fields):
        res = super(MessageMenu, self).default_get(fields)

        if 'default_send_to' in self.env.context:
            phone = self.env.context['default_send_to']
            partner = self.env['res.partner'].search([('phone', '=', phone)], limit=1)

            if partner:
                res['send_to'] = partner.id

        if 'default_template_paths' in self.env.context:
            res['template_paths'] = str(self.env.context['default_template_paths'])
            res['message'] = Config().get_template_text(self.env.context['default_template_name'])
            res['user_id'] = self.env.context['default_user_id']
            res['document_name'] = self.env.context['default_document_name']
            res['document_filename'] = self.env.context['default_document_filename']

        return res

    def generate_pdf(self, name):
        report = self.env.ref(name)
        pdf_data, _ = report._render_qweb_pdf(name, res_ids=self.user_id)

        return pdf_data

    def get_document_name(self):
        # Overridden by whatsapp_contacts.message_menu.inventory
        return self.document_name

    def send_message(self):
        self.ensure_one()

        if self.template_paths:
            # Template mode
            paths = ast.literal_eval(self.template_paths)
            template = Template(self.message, paths)
            pdf = self.generate_pdf(self.get_document_name())

            self.connection.send_pdf(self.send_to.phone, pdf, caption=template.fill(self), filename=self.document_filename or 'document')
        else:
            # Direct message mode
            self.connection.send_message_threaded(self.send_to.phone, self.message)