from odoo import api, fields, models  # noqa
from odoo.exceptions import ValidationError  # noqa
from ..global_py import Config, fill_text  # noqa


class MessageMenu(models.TransientModel):
    _name = 'whatsapp_contacts.messaging_menu'
    _description = 'Messaging Menu'

    def get_default(self):
        default_connection = Config().get('default_connection')

        connection = self.env['whatsapp.connection'].search([('id', '=', default_connection)], limit=1)  # noqa

        if connection:
            return connection.id

        return False

    connection = fields.Many2one('whatsapp.connection', default=get_default, string='Whatsapp Connection', required=True)
    recipients = fields.Many2many('res.partner', string='Recipients', required=True)  # noqa
    message = fields.Text(string='Message')

    # Template mode
    document_name = fields.Char(string='Document Name')
    document_filename = fields.Char(string='Document Filename')
    user_id = fields.Integer(string='Res Id')

    @api.model
    def default_get(self, fields):
        res = super(MessageMenu, self).default_get(fields)  # noqa

        if 'default_send_to' in self.env.context:  # noqa
            phone = self.env.context['default_send_to']  # noqa
            partner = self.env['res.partner'].search([('phone', '=', phone)], limit=1)  # noqa

            if partner:
                res['recipients'] = [(6, 0, [partner.id])]

        if 'default_template_name' in self.env.context:  # noqa
            res['message'] = Config().get_template_text(self.env.context['default_template_name'])  # noqa
            res['user_id'] = self.env.context['default_user_id']  # noqa
            res['document_name'] = self.env.context['default_document_name']  # noqa
            res['document_filename'] = self.env.context['default_document_filename']  # noqa

        return res

    def generate_pdf(self, name):
        report = self.env.ref(name)  # noqa
        pdf_data, _ = report._render_qweb_pdf(name, res_ids=self.user_id)

        return pdf_data

    def get_document_name(self):
        # Overridden by whatsapp_contacts.message_menu.inventory
        return self.document_name

    def send_message(self):
        self.ensure_one()  # noqa

        if self.document_name:
            # Template mode
            pdf = self.generate_pdf(self.get_document_name())

            for recipient in self.recipients:  # Iterate over all recipients and send messages
                self.connection.send_pdf(recipient.phone, pdf, caption=fill_text(self, self.message), filename=fill_text(self, '$reference'), exception=ValidationError, exception_condition_equals='Invalid phone number!')  # noqa
        else:
            # Direct message mode
            for recipient in self.recipients:
                self.connection.send_message(recipient.phone, fill_text(self, self.message), exception=ValidationError, exception_condition_equals='Invalid phone number!')  # noqa