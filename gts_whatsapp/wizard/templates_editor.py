from ..global_py import Config
from odoo import api, fields, models


class TemplatesEditor(models.TransientModel):
    _name = 'gts_whatsapp.templates_editor'

    template = fields.Selection([(template_id, template_id.replace('_', ' ').capitalize()) for template_id in Config().get('templates_text').keys()], string='Template Name', required=True, default='sales_quotations')
    template_text = fields.Text(string='Template Text')

    @api.onchange('template')
    def onchange_template(self):
        if self.template:
            self.template_text = Config().get_template_text(self.template)

    @api.onchange('template_text')
    def onchange_template_text(self):
        if self.template_text:
            Config().set_template_text(self.template, self.template_text)