from setuptools import setup, find_packages

from typing import List

DOT = "-e ."

def get_requirements(file_path: str) -> list[str]:
    with open(file_path) as file_obj:  # Burada open fonksiyonunu düzeltin
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]
        if DOT in requirements:
            requirements.remove(DOT)

    return requirements

setup(
    name="MLOProject",
    version="0.0.1",
    author="Ramazan",
    author_email="Ramazanklc7654@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")  # Burada da 'install_requires' düzeltildi
)

