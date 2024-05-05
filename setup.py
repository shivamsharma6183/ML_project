from setup.tools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirement s
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","" ) for req in requirements]

setup(
name='mlproject',
version = '0.0.1',
author='shivam',
author_email = 'shivamsharma6183@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)