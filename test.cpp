#include "test.hpp"

/*
 * Методы класса
 */

int test::ret_int(int val) {
    return val;
}

double test::ret_double(double val) {
    return val;
}

test *test_new() {
    return new test();
}

void test_del(test *test) {
    delete test;
}

// Обертка над методом ret_int
int sum(test *test, int val1, int val2) {
    return test->ret_int(val1+val2);
}

int sub(test *test, int val1, int val2) {
    return test->ret_int(val1-val2);
}
int mul(test *test, int val1, int val2) {
    return test->ret_int(val1*val2);
}
// Обертка над методом ret_double
double divi(test *test, int val1, int val2) {
    double rr =(double)val1/(double)val2;
    return test->ret_double(rr);
}

