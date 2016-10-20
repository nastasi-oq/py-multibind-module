from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([Extension("cynative", sources=["cynative.pyx"], libraries=["native"],
                                       library_dirs=["../nativelib"])])
)
