import shelve


def generate_payload(self, user_id=None, phone=None, model='whatsapp_contacts.messaging_menu', template_mode=True, template_name=None, template_paths=None, document_name=None, document_filename=None):
    if user_id is None:
        user_id = self.id

    if phone is None:
        phone = self.partner_id.phone

    if template_paths is None:
        template_paths = {'name': 'send_to.name', 'reference': 'name'}

    payload = {
        'type': 'ir.actions.act_window',
        'name': 'Send Whatsapp Message',
        'res_model': model,
        'target': 'new',
        'view_mode': 'form',
        'context': {
            'default_user_id': user_id,
            'default_send_to': phone
        }
    }

    if template_mode:
        payload['context'] = {  # noqa
            'default_user_id': user_id,
            'default_send_to': phone,
            'default_template_name': template_name,
            'default_template_paths': template_paths,
            'default_document_name': document_name,
            'default_document_filename': document_filename,
            'template_info_name': self.partner_id.name,
            'template_info_reference': self.name
        }

    return payload


class Config:
    def __init__(self):
        with shelve.open('gts_config') as db:
            # If anything about the config doesn't exist, Make it none
            db['pos_connection'] = db.get('pos_connection')
            db['default_connection'] = db.get('default_connection')
            db['base_url'] = db.get('base_url')

            if db.get('base_url') is None:
                db['base_url'] = 'https://whatapi.geektechsol.com'

            if db.get('templates_text') is None:
                db['templates_text'] = {'sales_quotations': 'Hello $name, Here\' your quotation/order. Please check the attached document below.', 'invoice': 'Hello $name, Here\'s your invoice. Please check the attached document below.', 'purchase_quotation': 'Hello $name, Here\'s your purchase quotation. Please check the attached document below.', 'stock.action_report_delivery': "Hello $name, Here's your delivery slip. Please check the attached document below.", "stock.action_report_picking": "Hello $name, Here's your picking operation slip. Please check the attached document below."}  # noqa

    def get_template_text(self, template):
        return self.get('templates_text').get(template, '')

    def set_template_text(self, template, text):
        new_templates_text = self.get('templates_text')
        new_templates_text[template] = text
        return self.set('templates_text', new_templates_text)

    @staticmethod
    def get(name):
        with shelve.open('gts_config') as db:
            return db[name]

    @staticmethod
    def set(name, value):
        with shelve.open('gts_config') as db:
            db[name] = value


def fill_text(self, text):
    name = self.env.context.get('template_info_name', '$name') or 'name'
    reference = self.env.context.get('template_info_reference', '$reference') or 'reference'

    return text.replace('$name', name).replace('$reference', reference)
