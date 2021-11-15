from setuptools import setup, find_packages

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name='mailtrap_handler',
    version="0.0.1",
    author="Said Tahali (trusta)",
    url="https://github.com/trustedshops-public/mailtrap-handler",
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>3.8.0'
)
