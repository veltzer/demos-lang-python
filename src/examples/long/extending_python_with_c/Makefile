PYTHON=python
BINARY_FOLDER=build/lib.linux-x86_64-cpython-311
SUFFIX=.cpython-311-x86_64-linux-gnu.so
SO_CAR=$(BINARY_FOLDER)/_car$(SUFFIX)
SO_ATOI=$(BINARY_FOLDER)/_atoi$(SUFFIX)

.PHONY: all
all: $(SO_CAR) $(SO_ATOI)

$(SO_ATOI): atoi_wrap.c
	$(PYTHON) setup_atoi.py build

$(SO_CAR): car_wrap.cxx car.cc
	$(PYTHON) setup_car.py build

car.py car_wrap.cxx: car.i
	swig -python -c++ car.i
atoi.py atoi_wrap.c: atoi.i
	swig -python atoi.i

.PHONY: use_car
use_car:
	$(PYTHON) use_car.py $(BINARY_FOLDER)

.PHONY: use_atoi
use_atoi:
	$(PYTHON) use_atoi.py $(BINARY_FOLDER)

.PHONY: clean
clean:
	@rm -f *_wrap.cxx *_wrap.c car.py car.pyc atoi.py atoi.pyc *.so
	@rm -rf __pycache__
	@\rm -rf build
