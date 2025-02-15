from setuptools import setup, find_packages

setup(
    name="grafosbiblioteca",
    version="0.1", 
    author="André Rocha",
    author_email="andre.lucio@aluno.uece.br",
    description="Uma biblioteca para manipulação de grafos usando lista de adjacência",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andrelrocha/grafos-lib", 
    packages=find_packages(),
    install_requires=[
        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Teoria Grafos",
    ],
    python_requires=">=3.7",  
)
