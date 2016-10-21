ALL: build-libs run-test

build-libs:
	$(MAKE) -C group_a/nativelib
	$(MAKE) -C group_a/cythlib
	$(MAKE) -C group_b/nativelib
	$(MAKE) -C group_b/cythlib

run-test: run-test-symm run-test-asym

run-test-symm:
	LD_LIBRARY_PATH=group_a/nativelib:group_b/nativelib ./multibind_symm.py 3

run-test-asym:
	LD_LIBRARY_PATH=group_a/nativelib:group_b/nativelib PYTHONPATH=group_a/cythlib ./multibind_asym.py

clean:
	$(MAKE) -C group_a/nativelib clean
	$(MAKE) -C group_a/cythlib clean
	$(MAKE) -C group_b/nativelib clean
	$(MAKE) -C group_b/cythlib clean

.PHONY: build-libs run-test run-test-symm run-test-asym clean
