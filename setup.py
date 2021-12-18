from setuptools import setup


with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

with open("README.md") as fp:
    long_description = fp.read()


setup(
    name="spore.py",
    author="LEv145",
    version="1.1",
    description="Spore REST API client",
    install_requires=requirements,
    packages=["spore_api"],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7.0",
    project_urls={
        "Git": "https://github.com/LEv145/spore.py",
        "Issue tracker": "https://github.com/LEv145/spore.py/issues",
    },
    entry_points="""
    [console_scripts]
    spore_cli=spore_api.__main__:cli
    """
)
