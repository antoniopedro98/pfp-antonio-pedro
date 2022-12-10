# pfp-antonio-pedro
This repository contains my Final Programming Project and is part of my master's dissertation, which is related to the challenges and problems encountered in the use of Machine Learning in Industry. My orientor is Dr. Prof. Marcos Kalinowski

# Requirements

- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Pipenv](https://pypi.org/project/pipenv/)

# How to start

We use a virtual environment, provided by *pipenv*. In order to activate and set this environment, you must:

- *git clone* this project
- Open the command line in this project base folder and type
  - pipenv install = this install all the necessary libraries
  - pipenv shell = this activate the virtual environemnt

# Running

Once you activate your virtual environment, you can type on this project base folder:

## Run the Notebooks

Just type:
- jupyter notebook

## Run the tests

Unit Tests only:
- python -m unittest -v

Unit Tests with Coverage Report:
- python -m coverage run -m unittest
- python -m coverage html

# New Libraries

If you wish to install new libraries, you just need to install them on your virtual environment and not on your system environment. In other words, to install new libraries in this project, just type:

- pipenv install lib-name
