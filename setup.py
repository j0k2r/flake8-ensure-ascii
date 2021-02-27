"""Python package metadata."""

from setuptools import setup


def _get_readme() -> str:
    with open("README.md") as readme_handle:
        return readme_handle.read()


setup(
    name="flake8-ensure-ascii",
    version="1.0.0",
    description="Flake8 Ensure ASCII encoding plugin.",
    long_description=_get_readme(),
    long_description_content_type="text/markdown",
    keywords="flake8 plugin encoding ascii",
    author="Hamza Z.",
    author_email="16209548+j0k2r@users.noreply.github.com",
    url="https://github.com/j0k2r/flake8-ensure-ascii",
    license="MIT",
    py_modules=["flake8_ensure_ascii"],
    install_requires=["flake8>=3.7"],
    extras_require={
        "dev": [
            "flake8",
            "mypy",
            "pydocstyle",
            "pytest",
            "isort",
            "black",
            "wheel",
        ]
    },
    zip_safe=False,
    entry_points={
        "flake8.extension": ["ENC = flake8_ensure_ascii:Flake8EnsureASCII"]
    },
    classifiers=[
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
