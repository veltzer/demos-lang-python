#include "car.hh"
#include <iostream>

Car::Car() {
	number=666;
}

void Car::printSelf() {
	std::cout << "This is car number " << number << std::endl;
}

void Car::setNumber(int inumber) {
	number=inumber;
}

int Car::getNumber(void) {
	return number;
}

int Car::add(int a,int b) {
	return a+b;
}
