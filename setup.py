from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
        :param file_path: path to the file that contains the names of all required packages
        :return: list of all the required packages
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(name='mlproject', version='0.0.1', author='Rohit Solanki',
      author_email='rsolanki1822@gmail.com', packages=find_packages(),
      requires=get_requirements('requirements.txt'))
