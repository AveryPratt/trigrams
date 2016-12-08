"""Benny and Avery's Trigram."""


from setuptools import setup


setup(
    name="trigram",
    description="An implementation of the Trigram assignment.",
    version=0.1,
    author="Avery Pratt, Benjamin Petty",
    author_email="contact@benpetty.me, apratt91@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["trigram"],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov"]
    },
    entry_points={
        "console scripts": [
            "trigram = trigram:read_story"]
    }
)
