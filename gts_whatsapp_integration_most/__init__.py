import sys
import os
import shutil

PWD = os.path.abspath(os.path.dirname(__file__))


def get_python_version():
    version_info = sys.version_info
    major, minor = version_info.major, version_info.minor

    if major == 3 and minor in (9, 10, 12):
        return f"{major}.{minor}"

    raise Exception('Unsupported Python version.')


if not os.path.exists(f'{PWD}/models'):
    version = get_python_version()

    if '3.10' in version:
        shutil.copytree(f'{PWD}/_CB/models3_10', f'{PWD}/models')
    elif '3.9' in version:
        shutil.copytree(f'{PWD}/_CB/models3_9', f'{PWD}/models')
    else:
        print(f'Invalid python version: {version}')


from . import models
