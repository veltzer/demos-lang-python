#ifndef __car_hh
#define __car_hh

class Car {
private:
  int number;

public:
  Car(void);
  void setNumber(int number);
  int getNumber(void);
  void printSelf(void);
};

#endif // __car_hh
