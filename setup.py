import setuptools

__project__ = "rpg"
__version__ = "0.0.1"
__description__ = "text game"
__packages__ = setuptools.find_packages()
__author__ = "Richard Harbord"
__author_email__ = "richardharbord@clara.co.uk"
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
]

setuptools.setup(    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,
    author_email = __author_email__,
    classifiers = __classifiers__,
)