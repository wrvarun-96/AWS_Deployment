from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will retunr the list of requirements
    '''

    cons = "-"
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements
        


setup(
    name = 'AWS_Scaleble_Project',
    version = '0.0.1',
    author = 'Varun',
    author_email = 'wrvarun96@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)