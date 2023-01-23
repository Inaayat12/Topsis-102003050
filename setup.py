from distutils.core import setup
setup(
  name = 'Topsis-102003050',         
  packages = ['Topsis-102003050'],  
  version = '0.1',
  license='MIT',
  description = 'Calculate Topsis score and save it in a csv file',
  author = 'Inaayat Goyal',                   
  author_email = 'igoyal1_be20@thapar.edu',     
  url = 'https://github.com/Inaayat12/Topsis-102003050.git',
  download_url = '',
  keywords = ['TOPSISSCORE', 'RANK', 'DATAFRAME'],
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
