from . import zstring
from ..global_py import Config

TEMPLATES_SELECTION = [
    ('sales_quotations', 'Sales Quotation/Order'),
    ('purchase_quotation', 'Purchase Quotation'),
    ('invoice', 'Invoice')
]


class Template:
    def __init__(self, template_text: str, paths: dict[str, str]):
        self.template_text = template_text
        self.template = zstring.TextTemplate(template_text)
        self.paths: dict[str, str] = paths

    def fill(self, you):
        variables = self.template.get_variables()
        results: dict[str, str] = {}

        for var in variables:
            path: str | None = self.paths.get(var)

            if not path:
                continue

            result = self.get(you, path.split('.'))
            results[var] = result

        return self.template.fill(results)

    def get(self, obj, names: list[str]):
        current = obj

        for name in names:
            current = getattr(current, name)

        return current