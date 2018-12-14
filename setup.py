from setuptools import setup

setup(
    name='flask-prom',
    version='0.1.0',
    url='https://github.com/noqcks/flask-prom',
    license='BSD',
    author='Benji Visser',
    author_email='benny@noqcks.io',
    maintainer='Benji Visser',
    maintainer_email='benny@noqcks.io',
    description='Prometheus client instrumentation for flask.',
    long_description=__doc__,
    packages=['flask_prom'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'prometheus-client>=0.0.14'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',

        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Topic :: System :: Monitoring',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='prometheus monitoring'
)
