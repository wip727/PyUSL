clean:
	  find . -name '*.pyc' -exec rm --force {} +

install: clean
		python setup.py install
