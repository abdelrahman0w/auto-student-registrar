import os
from setuptools import setup


about = {}
here = os.path.abspath(os.path.dirname(__file__))


with open('README.md', 'r') as f:
    readme = f.read()


setup(
    name='auto-student-registrar',
    description='''
                An automatic student registrar that allow inserting students and the instructors and automatically allocate the slots of the courses in accordance with the student courses.
                ''',
    long_description=readme,
    long_description_content_type='text/markdown',
    version='0.1.0',
    packages=['auto_student_registrar'],
    include_package_data=True,
    python_requires=">=3.7.*",
    install_requires=['tabulate'],
    license='MIT',
)
