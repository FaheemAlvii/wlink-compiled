from . import zstring
from ..global_py import Config  # noqa

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

    def fill(self, objects: list[object]):
        variables = self.template.get_variables()
        results: dict[str, str] = {}

        for var in variables:
            path: str | None = self.paths.get(var)

            if not path:
                continue

            result = self.get(objects, path.split('.'))
            results[var] = result

        return self.template.fill(results)

    @staticmethod
    def get(objects: list[object], names: list[str]):
        for object in objects:  # noqa
            try:
                current = object

                for name in names:
                    current = getattr(current, name)

                return current
            except (AttributeError, NameError):
                continue