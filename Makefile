ALL: build-libs run-test

build-libs:
	$(MAKE) -C group_a/nativelib
	$(MAKE) -C group_a/cythlib
	$(MAKE) -C group_b/nativelib
	$(MAKE) -C group_b/cythlib

run-test:
	LD_LIBRARY_PATH=group_a/nativelib:group_b/nativelib ./multibind.py 3

clean:
	$(MAKE) -C group_a/nativelib clean
	$(MAKE) -C group_a/cythlib clean
	$(MAKE) -C group_b/nativelib clean
	$(MAKE) -C group_b/cythlib clean

.PHONY: build-libs run-test clean
