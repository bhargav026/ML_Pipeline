from setuptools import setup, find_packages

setup(name = "census-income",
      version = 1 ,
      author= 'Bhargav',
      author_email= "bhargavec026@gmail.com",
      packages= find_packages(),
      install_requires = ["pandas", "numpy", "flask"]
      )
