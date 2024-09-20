# production
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


""" Models """
if not os.path.exists(f'{PWD}/models'):
    version = get_python_version()

    if version == '3.10':
        shutil.copytree(f'{PWD}/_CB/models3_10', f'{PWD}/models')
    elif version == '3.9':
        shutil.copytree(f'{PWD}/_CB/models3_9', f'{PWD}/models')
    else:
        print(f'Invalid python version: {version}')


from . import models

""" Wizard """
if not os.path.exists(f'{PWD}/wizard'):
    version = get_python_version()

    if version == '3.10':
        shutil.copytree(f'{PWD}/_CB/wizard3_10', f'{PWD}/wizard')
    elif version == '3.9':
        shutil.copytree(f'{PWD}/_CB/wizard3_9', f'{PWD}/wizard')
    else:
        print(f'Invalid python version: {version}')

from . import wizard


# dev mode
# from . import models
# from . import wizard
