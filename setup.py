from setuptools import setup, find_packages

setup(
    name='mailtrap_handler',
    version="0.0.1",
    author="Said Tahali (trusta)",
    url="https://github.com/trustedshops/mailtrap-handler",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "polling",
        "requests"
    ],
    python_requires='>3.8.0'
)
