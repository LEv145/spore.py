.PHONY: build
build:
	pyinstaller pyinstaller.spec \
		--distpath .pyinstaller_dist \
		--workpath .pyinstaller_build

.PHONY: clean
clean:
	rm .pyinstaller_*
