from setuptools import setup, find_packages

setup(
    name='greeking',
    version='0.200',
    description='Django template tools for printing filler text, a \
    technique from the days of hot type known as greeking.',
    author='Ben Welsh',
    author_email='Benjamin.Welsh@latimes.com',
    url='http://github.com/palewire/django-greeking',
    download_url='http://github.com/palewire/django-greeking.git',
    packages=find_packages(),
    license='MIT',
    keywords='greeking pangrams lorem ipsum quotables comments \
    text jabberwocky placekittens fillmurray filler',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=['six==1.5.2']
)
