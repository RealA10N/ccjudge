from setuptools import find_packages, setup

import ccjudge

with open("README.md", encoding="utf8") as f:
    README = f.read()

with open("requirements.txt", encoding="utf8") as f:
    DEPENDENCIES = f.read().splitlines()

setup(
    name="ccjudge",
    version=ccjudge.__version__,
    description=ccjudge.__description__,
    url='https://github.com/RealA10N/ccjudge',

    python_requires=">=3.10",
    install_requires=DEPENDENCIES,

    long_description=README,
    long_description_content_type="text/markdown",

    author=ccjudge.__author__,
    author_email=ccjudge.__author_email__,
    packages=find_packages(include=['ccjudge*']),
)
