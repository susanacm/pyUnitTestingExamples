from setuptools import setup, find_packages

setup(
    name='pyUnitTestingExamples ',
    version='1.0.0',
    description='Factorial y mocking',
    url='https://github.com/susanacm/pyUnitTestingExamples.git',
    author='Susana Cano Marín',
    author_email='susanacm@uma.es',
    license='MIT',
    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=["test.*", "tests"]),
)
