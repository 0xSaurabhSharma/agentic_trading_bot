from setuptools import find_packages, setup 

setup(
    name= "Agentic_Trading_Bot",
    version= "0.0.1",
    author= "Saurabh Sharma",
    author_email= "dm.sharmasaurabh@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchain_core","langchain_community","lancedb","tavily-python","langgraph","polygon"]
)