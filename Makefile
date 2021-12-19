MAKEDIR = pyinstaller_builds

ifeq ($(OS), Windows_NT)
	OS_NAME = ${OS}
else
	OS_NAME = ${shell uname -s}
endif

OS_NAME_LOWER = $(shell python -c "print('$(OS_NAME)'.lower())")


.PHONY: build
build:
	pip install --editable .

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: binary
binary:
	pyinstaller pyinstaller.spec \
		--distpath ${MAKEDIR}/dist_${OS_NAME_LOWER} \
		--workpath ${MAKEDIR}/build_${OS_NAME_LOWER}

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: upload
upload: sdist
	twine upload dist/*

.PHONY: clean
clean:
	rm -R ${MAKEDIR}
