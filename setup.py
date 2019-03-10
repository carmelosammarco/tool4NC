from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='tool4nc',
      version='0.1.9',
      description='Software for the netCDF files manipulations',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url="https://github.com/carmelosammarco/tool4nc",
      author='Carmelo Sammarco',
      author_email='sammarcocarmelo@gmail.com',
      license='gpl-3.0',
      python_requires='~=3.6',

      install_requires=[
        'netCDF4>=1.4.2',
        'csv342>=1.0.0', 
        'pandas>=0.23.4', 
        'xarray>=0.11.0',  
        'shapely>=1.6.4.post2', 
        'fiona>=1.8.4', 
        'cdo>=1.4.0'
      ],
      packages=find_packages(),
      
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3.6',
       ], 

)
