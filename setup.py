from setuptools import setup, find_packages


setup(
    name = "django-flag",
    version = "0.2.dev4",
    description = "flagging of inapproriate/spam content",
    author = "Greg Newman",
    author_email = "greg@20seven.org",
    url = "http://code.google.com/p/django-flag/",
    packages = find_packages(),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data = True,
    zip_safe = False,
)
