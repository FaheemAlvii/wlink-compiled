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


version = get_python_version()

if not os.path.exists(f'{PWD}/api'):
    if version == '3.10':
        shutil.copytree(f'{PWD}/_CB/api3_10', f'{PWD}/api')
    elif version == '3.9':
        shutil.copytree(f'{PWD}/_CB/api3_9', f'{PWD}/api')
    else:
        print(f'Invalid python version: {version}')


if not os.path.exists(f'{PWD}/models'):
    if version == '3.10':
        shutil.copytree(f'{PWD}/_CB/models3_10', f'{PWD}/models')
    elif version == '3.9':
        shutil.copytree(f'{PWD}/_CB/models3_9', f'{PWD}/models')
    else:
        print(f'Invalid python version: {version}')


from . import models
