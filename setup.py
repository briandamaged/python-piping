from setuptools import setup, find_packages

setup(
    name = 'piping',
    version = '0.2.1',
    description = 'Python Object Pipes',
    author = 'Brian Lauber',
    author_email = 'constructible.truth@gmail.com',
    packages = find_packages(exclude = ["tests"]),
    install_requires = [],
    test_suite = 'tests',
    tests_require = ["mock>=1.0.0"]
)
