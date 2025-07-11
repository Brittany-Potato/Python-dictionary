# Important modules/package for Python

# * ~~ Python Standard Library (Built in modules) ~~

# math -> Provides mathematical functions like sqrt, sin, log etc
# random -> Functions to generate random numbers and make random selections
# datetime -> Deals with dates and times
# time -> Time-related function(sleep, current time, etc)
# os -> Interact with the operating system (File, directories etc)
# sys -> Access system-specific parameters and functions
# re -> Regular expression for text searching and pattern matching
# json -> Parse and create JSON data
# csv -> Read/write CSV files
# subprocess -> Run system commands or programs from Python
# collections -> Specalized container datatypes like counter, deque
# itertools -> Functions for efficent looping 
# functools -> Tools for higher-order functions like lru_cache 
# typing -> Type hints for variables and functions
# statistics -> Basic statistial operations (mean, median, etc)
# uuid -> Creates unique identifiers 
# pathlib -> OO interface to manipulate filysystem paths
# threading & multiprocessing -> For concurrent execution of code

# * ~~ External packages (Installed via pip) ~~
#? Popular Categories & Examples

#? Data science
# numpy -> Numerical computations and arrays
# pandas -> Data analysis and manipulation
# matplotlib/seaborn -> Data visulization 
# scipy -> Scientific computing
# scikit-learn -> Machine learning algorithms 

#? Web development
# flask -> Lightweight web framework 
# django -> Full-stack web framework
# requests -> Easy HTTP requests
# beautifulsoup4 -> Web scraping HTML parser
# fastapi -> High-performance web APIs

#? AI / ML
# tensorflow -> Deep learning framework
# torch (PyTorch) -> Machine learning library
# transformers -> State-of-the-art NLP models

#? Utilities
# pytest -> Testing framework
# pydantic -> Data validation and settings management
# click -> CLI tool builder
# loguru -> Simplified logging
# dotenv -> Load enviroment variables

#? Dev Tools
# black -> Code formatter
# flake8 -> :inter for Python
# mypy -> Static type checker

# * ~~ Creating Your Own Modules and Packages ~~

# Module -> Any .py file is a module:
def greet(name):
    return f"Hello, {name}!"

# Package -> A folder with an __init__.py file:
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
# import like:
# from mypackage import from module1

# * ~~ Exploring Modules ~~

# Check built-ins
help("modules")

# List installed packages
# pip list