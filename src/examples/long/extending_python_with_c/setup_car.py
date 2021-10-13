"""
setup.py file for SWIG car
"""


from setuptools import setup, Extension


car_module = Extension(
    '_car',
    sources=['car_wrap.cxx', 'car.cc'],
)

setup(
    name='car',
    version='0.1',
    author='SWIG Docs',
    description='Simple swig a from docs',
    ext_modules=[car_module],
    py_modules=['car'],
)
