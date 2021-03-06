import os
import setuptools

SETUP_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
README_FILEPATH = os.path.join(SETUP_DIRECTORY, 'README.md')

with open(README_FILEPATH, 'r') as fio:
    long_description = fio.read()

setuptools.setup(
    name='splitargs',
    packages=['splitargs'],
    version='0.0.1',
    description="Split quoted arguments like commands do",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Deadbeef-Development",
    author_email="deadbeef.development@gmail.com",
    url="https://github.com/deadbeef-development/splitargs",
)