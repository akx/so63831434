from setuptools import setup, find_packages

setup(
    name="good-day",
    version="0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["good_day=mod1.good_day:main",],},
)
