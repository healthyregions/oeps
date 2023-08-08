from distutils.core import setup

setup(
    name='oeps_backend',
    version='0.1.0',
    packages=['oeps_backend'],
    install_requires=[
        'requests==2.31.0',
        'python-dotenv==1.0.0',
        'google-cloud-bigquery==3.11.3',
        'urllib3<2.0',
    ]
)