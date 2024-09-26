import re


class TextTemplate:
    def __init__(self,
                 template_string: str,
                 seperator: str = "$value",
                 allow_invalid_names: bool = False,
                 allow_nonexistent_names: bool = False):

        """
        Format for template strings:
            'Hello, $name! I heard you're feeling $mood'

        Although the delimiter (seperator) can be changed
        """
        self.template_string: str = template_string
        self.separator: str = seperator
        self.allow_invalid_names: bool = allow_invalid_names
        self.allow_nonexistent_names: bool = allow_nonexistent_names

    def fill(self, variables: dict[str, str]) -> str:
        result = self.template_string

        for name, value in variables.items():
            if not self.allow_invalid_names and not name.isidentifier():
                raise ValueError(f"The variable name {name} is not a proper variable name. To disable this, Set allow_invalid_names=True")  # noqa: E501

            # Turn seperator into what we will actually find in the string,
            # Eg to "$name" from "$value" (the seperator)
            value_replacer = self.separator.replace('value', name)

            previous_result = result
            result = result.replace(value_replacer, value)

            # Check if the previous result is the same as the current result,
            # If true, It means that the variable name is invalid and doesn't exist.
            if previous_result == result:
                raise ValueError(f"The variable name '{name}' doesnt exist in the template with a valid format. Disable this by setting allow_nonexistent_names=True")  # noqa: E501

        return result

    def count_variables(self) -> int:
        """
        Counts the number of variables in the template string
        based on the separator format.
        """
        pattern = re.escape(self.separator).replace('value', r'\w+')
        return len(re.findall(pattern, self.template_string))

    def get_variables(self) -> list[str]:
        """
        Gets the list of variable names in the template string
        based on the separator format.
        """
        pattern = re.escape(self.separator).replace('value', r'(\w+)')
        return re.findall(pattern, self.template_string)


class StringFormatter:
    def format(self, value: str, format_mode: str) -> str:
        raise NotImplementedError("StringFormatter shouldn't be used directly. Instead, You should create a subclass.")

    def format_string(self, text: str, values: dict[str, str]) -> str:
        placeholders = re.findall(r'\{(.*?)}', text)

        new_text = text

        for placeholder in placeholders:
            splitted = placeholder.split(':')

            key = splitted[0]
            format_spec = splitted[1].removeprefix(' ') if len(splitted) >= 2 else ''

            value = values.get(key, '{' + key + '}')

            if 'format_mode' in self.format.__code__.co_varnames:
                formatted_value = self.format(value, format_spec)
            else:
                formatted_value = self.format(value)

            new_text = new_text.replace(f'{{{placeholder}}}', formatted_value)

        return new_text


if __name__ == '__main__':
    text_template = TextTemplate('Hello $name')

    result = text_template.fill({'name': 'Alice'})
    variables_count = text_template.count_variables()
    variables = text_template.get_variables()

    print(f'{result=}')
    print(f'{variables_count=}')
    print(f'{variables=}')