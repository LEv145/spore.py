MAKEDIR = pyinstaller_builds


.PHONY: build
build:
	pip install --editable .

.PHONY: binary
binary:
	pyinstaller pyinstaller.spec \
		--distpath pyinstaller_builds/linux_dist \
		--workpath pyinstaller_builds/linux_build

.PHONY: clean
clean:
	rm -R pyinstaller_builds
