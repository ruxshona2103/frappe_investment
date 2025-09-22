from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="investment",
    version="0.0.1",
    description="Investment Management App",
    author="ruxshona2103",
    author_email="your_email@example.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
