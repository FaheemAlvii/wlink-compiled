import shelve


def generate_payload(id, phone, model='whatsapp_contacts.messaging_menu', template_mode=True, template_name=None, template_paths=None, document_name=None, document_filename=None):
    if template_paths is None:
        template_paths = {'name': 'send_to.name'}

    payload = {
        'type': 'ir.actions.act_window',
        'name': 'Send Whatsapp Message',
        'res_model': model,
        'target': 'new',
        'view_mode': 'form',
    }

    if template_mode:
        payload['context'] = {  # noqa
            'default_user_id': id,
            'default_send_to': phone,
            'default_template_name': template_name,
            'default_template_paths': template_paths,
            'default_document_name': document_name,
            'default_document_filename': document_filename
        }
    else:
        payload['context'] = {
            'default_user_id': id,
            'default_send_to': phone,
        }

    return payload


class Config:
    def __init__(self):
        with shelve.open('gts_config') as db:
            # If anything about the config doesn't exist, Make it none
            db['pos_connection'] = db.get('pos_connection')

            if db.get('templates_text') == None:
                db['templates_text'] = {'sales_quotations': 'Hello $name, Here\' your quotation/order. Please check the attached document below.', 'invoice': 'Hello $name, Here\'s your invoice. Please check the attached document below.', 'purchase_quotation': 'Hello $name, Here\'s your purchase quotation. Please check the attached document below.', 'stock.action_report_delivery': "Hello $name, Here's your delivery slip. Please check the attached document below.", "stock.action_report_picking": "Hello $name, Here's your picking operation slip. Please check the attached document below."}

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
