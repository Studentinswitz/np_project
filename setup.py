# coding: utf-8

"""
    ChemOS Web Portal

    API entry point for ChemOS Web Portal. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Web Portal account. You can generate your `API KEY` on your [account information page](https://scientia.chemos.io/user).  # noqa: E501

    The version of the OpenAPI document: beta
    Contact: support@chemos.io
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="ChemOS Web Portal",
    author="ChemOS Web Portal",
    author_email="support@chemos.io",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "ChemOS Web Portal"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="License",
    long_description="""\
    API entry point for ChemOS Web Portal. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an &#x60;API KEY&#x60;, associated to your Web Portal account. You can generate your &#x60;API KEY&#x60; on your [account information page](https://scientia.chemos.io/user).  # noqa: E501
    """
)