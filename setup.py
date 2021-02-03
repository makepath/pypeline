from setuptools import setup
setup(name='pypeline',
      use_scm_version={
          "write_to": "pypeline/_version.py",
          "write_to_template": '__version__ = "{version}"',
          "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
      },
      description='Dask-powered Inspectable Function Pipelines',
      url='https://github.com/makepath/pypeline',
      packages=['pypeline',
                'pypeline.tests'],
      install_requires=['dask',
                        'pytest',
                        'tbb'],
      zip_safe=False,
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent"],
      include_package_data=True)
