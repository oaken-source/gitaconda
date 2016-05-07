
from os.path import join, dirname
from setuptools import setup


setup(
    name='gitaconda',
    version='0.1.0',
    author='Andreas Grapentin',
    author_email='andreas@grapentin.org',
    url='gitconda.readthedocs.io',
    description='a simple and deployable github clone',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    keywords='git management',
    packages=[
        'gitaconda_server',
        'gitaconda_shell',
    ],

    entry_points={
        'paste.app_factory': {
            'gitaconda-server = gitaconda_server:main'
        },
    },

    install_requires=[
        # gitaconda-server
        'pyramid',
    ],

    license='GPLv3+',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Version Control',
    ],

    test_suite='tests',
    tests_require=[
        'pytest',
        'webtest',
    ],

    setup_requires=[
        'pytest_runner',
    ],
)
