from setuptools import setup

setup(
      name='HAM_Python',
      version='v1.0',
      author=['Duong Vu', 'Jordan Dubchak', 'Linsey'],
      packages=['HAM_Python',],
      license='MIT License',
      long_description=open('README.md').read(),
      install_requires=['setuptools', 'pandas','numpy', 'seaborn', 'matplotlib'],
      include_package_data=True
      )