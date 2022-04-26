from setuptools import setup

setup(
    name="hello",
    version="0.1.0",
    author="Juan D. Velasquez",
    author_email="jdvelasq@unal.edu.co",
    license="MIT",
    url="http://github.com/jdvelasq/package_demo",
    description="A demo package",
    long_description="Long description of a demo package",
    keywords="demo",
    platforms="any",
    provides=["hello"],
    install_requires=[
        # "sklearn==1.0.2",
        # etc
    ],
    packages=[
        "hello",
        "hello.files",
    ],
    package_dir={"hello": "hello"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ],
)
