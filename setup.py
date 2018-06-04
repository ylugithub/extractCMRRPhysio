from setuptools import setup

setup(name='extractCMRRPhysio',
      version='0.1',
      description='extractCMRRPhysio in python.https://github.com/CMRR-C2P/MB/blob/master/extractCMRRPhysio.m',
      author='YingLi Lu',
      author_email='yinglilu@gmail.com',
      license='MIT',
      entry_points={
          'console_scripts': [
              'extractCMRRPhysio = extractCMRRPhysio.main:run']},
      packages=['extractCMRRPhysio'],
      install_requires=['pydicom']
      zip_safe=False)
