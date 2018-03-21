from setuptools import setup, find_packages

setup(
	name='redactor',
	version='1.0',
	author='Qianyun Zhu',
	authour_email='qianyun.zhu@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']
)
