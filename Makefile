MAKEDIR = pyinstaller_builds


.PHONY: build
build:
	pip install --editable .

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: binary
binary:
	pyinstaller pyinstaller.spec \
		--distpath pyinstaller_builds/dist \
		--workpath pyinstaller_builds/build

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: upload
upload: sdist
	twine upload dist/*

.PHONY: clean
clean:
	rm -R pyinstaller_builds
