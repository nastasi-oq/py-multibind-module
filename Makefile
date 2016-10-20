ALL:
	$(MAKE) -C group_a/nativelib
	$(MAKE) -C group_a/cythlib
	$(MAKE) -C group_b/nativelib
	$(MAKE) -C group_b/cythlib

clean:
	$(MAKE) -C group_a/nativelib clean
	$(MAKE) -C group_a/cythlib clean
	$(MAKE) -C group_b/nativelib clean
	$(MAKE) -C group_b/cythlib clean
