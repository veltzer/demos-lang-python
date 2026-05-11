"""
setup.py file for SWIG atoi
"""

from setuptools import setup, Extension

atoi_module = Extension(
    "_atoi",
    sources=["atoi_wrap.c"],
)

setup(
    name="atoi",
    version="0.1",
    author="SWIG Docs",
    description="""Simple swig atoi from docs""",
    ext_modules=[atoi_module],
    py_modules=["atoi"],
)
