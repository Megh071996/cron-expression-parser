from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cron-expression-parser",
    version="1.0.0",
    author="Megha Kumari",
    author_email="megha.sandalya.07@gmail.com",
    description="Cron Expression Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["cron_expression_parser"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "cron-expression-parser = cron_expression_parser.on_click:on_click"
        ]
    },
    python_requires='>=3.10',
)