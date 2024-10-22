'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements

    """
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)

    except FileNotFoundError:
        print('requiremnets.txt file not found')      

    return requirements_lst              

     



setup(
    name='Network Anomaly Detection',
    version="0.0.1",
    author='Abhijeet',
    packages=find_packages(),
    install_requires=get_requirements()
)