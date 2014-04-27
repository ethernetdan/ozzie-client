from distutils.core import setup

setup(
    name='Ozzie',
    version='0.2.0',
    author='Dan Gillespie',
    author_email='danielg@umd.edu',
    packages=['ozzie'],
    url='https://github.com/ethernetdan/ozzie-client',
    license='LICENSE.txt',
    description='Use a RaspberryPi to detect whether a room is occupied.',
    long_description=open('README.md').read(),
    install_requires=[
        "RPi.GPIO >= 0.5.5",
    ],
)