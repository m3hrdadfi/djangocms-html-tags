from setuptools import setup, find_packages
from djangocms_html_tags import __version__

REQUIREMENTS = [
    "django-cms>=3.5",
    "djangocms-attributes-field>=1.0.0"
]

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Framework :: Django",
    "Framework :: Django :: 1.11",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
]

setup(
    author="Gökmen Görgen",
    author_email="gkmngrgn@gmail.com",
    description=open("README.md").read(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    name="djangocms-html-tags",
    packages=find_packages(),
    test_suite="tests.settings.run",
    version=__version__,
    zip_safe=False,
)
