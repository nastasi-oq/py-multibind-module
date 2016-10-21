from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([Extension("cynative", sources=["cynative.pyx"], libraries=[":libnative.so.1.1.0"],
                                       library_dirs=["../nativelib"])])
)
