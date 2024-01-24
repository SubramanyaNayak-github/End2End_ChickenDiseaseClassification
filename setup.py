import setuptools



with open('README.md', 'r') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End2End_ChickenDiseaseClassification"
AUTHOR_USER_NAME = "SubramanyaNayak-githiub"
SRC_REPO = "ChickenDiseaseClassification"
AUTHOR_EMAIL = "subramanayanayak3@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for ml/dl app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"))
