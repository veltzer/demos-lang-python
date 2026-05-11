PYTHON=python
PYTHON_VERSION=311
BINARY_FOLDER=build/lib.linux-x86_64-cpython-$(PYTHON_VERSION)
SUFFIX=.cpython-$(PYTHON_VERSION)-x86_64-linux-gnu.so
SO_CAR=$(BINARY_FOLDER)/_car$(SUFFIX)
SO_ATOI=$(BINARY_FOLDER)/_atoi$(SUFFIX)

.PHONY: all
all: $(SO_CAR) $(SO_ATOI)

$(SO_ATOI): atoi_wrap.c
	$(info doing [$@])
	@$(PYTHON) setup_atoi.py build

$(SO_CAR): car_wrap.cxx car.cc
	$(info doing [$@])
	@$(PYTHON) setup_car.py build

car.py car_wrap.cxx: car.i
	$(info doing [$@])
	@swig -python -c++ car.i
atoi.py atoi_wrap.c: atoi.i
	$(info doing [$@])
	@swig -python atoi.i

.PHONY: use_car
use_car:
	$(info doing [$@])
	@$(PYTHON) use_car.py $(BINARY_FOLDER)

.PHONY: use_atoi
use_atoi:
	$(info doing [$@])
	@$(PYTHON) use_atoi.py $(BINARY_FOLDER)

.PHONY: clean
clean:
	$(info doing [$@])
	@rm -f *_wrap.cxx *_wrap.c car.py car.pyc atoi.py atoi.pyc *.so
	@rm -rf __pycache__
	@\rm -rf build
