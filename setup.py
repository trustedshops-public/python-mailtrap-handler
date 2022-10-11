from setuptools import setup, find_packages
from os import environ

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.readlines()

with open("README.md", "r") as readme_file:
    readme = "".join(readme_file.readlines())

setup(
    name='mailtrap_handler',
    version=environ.get("VERSION", "snapshot"),
    author="Said Tahali (trusta)",
    url="https://github.com/trustedshops-public/python-mailtrap-handler",
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>3.8.0',
    long_description=readme,
    long_description_content_type='text/markdown'
)
