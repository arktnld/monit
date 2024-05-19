from setuptools import setup, find_packages
import pathlib

setup(
    name='pymonit',
    version='1.4.7',
    description='Programa de monitoramento de código python, desenvolvido para ser utilizado pelas funcionário da Agência de dados',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    author='arktnld',
    author_email='arktnld@gmail.com',
    url='https://github.com/arktnld/monit',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sqlalchemy',
        'pymysql',
        'psutil',
        'python-dotenv'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
