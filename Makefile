CC=python2
FINALNAME=RootRoad


all:
	$(CC) main.py


clean:
	rm *.pyc
	rm */*.pyc
	rm */*/*.pyc
	rm */*/*/*.pyc

