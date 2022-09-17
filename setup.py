from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='spike',
  version='0.0.1',
  description='Spike Powerful Ranger Scanner',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='BarakIL',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='Spike', 
  packages=find_packages(),
  install_requires=['requests==2.28.1', 'progressbar2==4.0.0'] 
)
