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

help:
	@echo "HELP: "
	@echo "    make                - build libs and run tests"
	@echo "    make build-libs     - build all libraries"
	@echo "    make run-test       - run all tests"
	@echo "    make run-test-symm  - run symmetrical loading of libraries test"
	@echo "    make run-test-asym  - run asymmetrical loading of libraries test"
	@echo "    make clean          - clean all"
	@echo "    make help           - this help"

.PHONY: build-libs run-test run-test-symm run-test-asym clean help
