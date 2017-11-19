import setuptools

setuptools.setup(name='flask_github_jobs',
      version='0.1.0',
      description='A simple flask that lists jobs from the github jobs api',
      url='https://github.com/lex00/flask-github-jobs',
      author='Albert Artigues',
      author_email='',
      license='MIT',
      packages=['flask_github_jobs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'flask',
          'requests'
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
)

