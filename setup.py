from distutils.core import setup

setup(
    name="dirg-basicweb",
    version="0.1",
    description='A basic dirg web appplication. ',
    author = "Hans, Hoerberg och Daniel Evertsson",
    author_email = "hans.horberg@umu.se, daniel.evertsson@umu.se",
    license="Apache 2.0",
    packages=["dirg", "dirg/basicweb"],
    package_dir = {"": "src"},
    classifiers = ["Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    install_requires = ["cherrypy", "mako", "beaker"],
    zip_safe=False,
)