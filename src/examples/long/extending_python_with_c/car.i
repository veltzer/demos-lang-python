/* File: car.i */
%module car

%{
#include "car.hh"
%}

class Car {
  private:
    int number;
  public:
    void setNumber(int number);
    int getNumber(void);
    void printSelf(void);
    int add(int a,int b);
};
