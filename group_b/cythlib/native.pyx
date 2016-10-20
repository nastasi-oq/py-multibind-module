cimport native

cdef class Native:
    def print_native_version(self):
        native.print_native_version()
