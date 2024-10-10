from setuptools import find_packages, setup
#installing the local package within the local system, use setuptools.

setup(
    name = "QASystem with haystack",
    version = "0.0.1",
    author = "Shrimanta_Satpati",
    author_email = "satpatishrimanta@gmail.com",
    packages = find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","fastapi","uvicorn","python-dotenv","pathlib"]
)