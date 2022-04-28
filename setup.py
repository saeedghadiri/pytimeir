import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytimeir",
    version="0.2",
    author="Saeed Ghadiri",
    author_email="saeed.ghadiri@gmail.com",
    description="Get events and holidays from time.ir",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saeedghadiri/pytimeir",
    project_urls={
        "Bug Tracker": "https://github.com/saeedghadiri/pytimeir/issues",
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['pytimeir'],
    python_requires=">=3.6",
    
    install_requires=[
        'requests',
        'pandas',
        'jdatetime',
        'Unidecode',
        'beautifulsoup4'
    ]
)
