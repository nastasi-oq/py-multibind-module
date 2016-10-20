ALL: cython run-test
	@echo "run 'make help' for more info"

cython:
	CFLAGS="-I../nativelib" LDFLAGS="-L../nativelib" python setup.py build_ext -i


run-test:
	LD_LIBRARY_PATH=../nativelib PYTHONPATH=. python -c 'import cynative ; cynative.cyprint_native_version()'

clean:
	rm -rf build *.so *.c

help:
	@echo "HELP:"
	@echo "    make           - produce module and run test"
	@echo "    make cython    - produce module"
	@echo "    make run-test  - run test" 
	@echo "    make clean     - remove produced modules and temporarily files"
	@echo "    make help      - this help"

.PHONY: clean run_test help
