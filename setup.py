from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.4"
AUTHOR = "Amar"
DESCRIPTION = "This is the 2025 ML project"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    """Returns a list of dependencies from requirements.txt, excluding '-e .'"""
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements = requirement_file.read().splitlines()  # Read lines properly
        
    if "-e ." in requirements:
        requirements.remove("-e .")  # Remove "-e ." safely
    return requirements

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),  # Finds all Python packages with __init__.py
    install_requires=get_requirements_list()  # Installs dependencies
)
# find_packages() will search all the packages that you are created and its going to return that names