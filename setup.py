import pathlib

from setuptools import setup


here = pathlib.Path(__file__).parent


def read(name):
    fname = here / name
    with fname.open() as f:
        return f.read()


install_requires = [
    "typing_extensions>=3.6.5",
]


setup(
    name="async-timeout-pre",
    version='4.0.0',
    description=("Timeout context manager for asyncio programs"),
    long_description="No long description, sorry",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Framework :: AsyncIO",
    ],
    author="Andrew Svetlov",
    author_email="andrew.svetlov@gmail.com",
    url="https://github.com/aio-libs/async_timeout/",
    license="Apache 2",
    packages=["async_timeout_pre"],
    python_requires=">=3.5.3",
    install_requires=install_requires,
    include_package_data=True,
)
