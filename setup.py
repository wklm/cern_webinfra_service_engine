from distutils.core import setup

with open('requirements.txt') as f:
        requirements = f.read().splitlines()

setup(
    name='cern_webinfra_service_engine',
    packages=['cern_webinfra_service_engine'],
    version='0.1.1',
    description='Library for connecting the microservices with CERN web infrastructure manager',
    author='CERN / Wojciech Kulma',
    author_email='wojciech.kulma@cern.ch',
    url='https://github.com/wklm/cern_webinfra_service_engine.git',
    download_url='https://github.com/wklm/cern_webinfra_service_engine.git',
    keywords=['cern', 'webinfra', 'activemq', 'stomp',
              'microservices',
              'integration'],
    classifiers=[],
    install_requires=requirements,
)
