#include <iostream>
#include <string.h>

class test {
public:
    int a = 5;
    double b = 5.12345;
    char c = 'X';

    int ret_int(int val);
    double ret_double(double val);
};

#ifdef __cplusplus
extern "C" {
#endif

    test *test_new();
    void test_del(test *test);
    int sum(test *test, int val1, int val2);
    int sub(test *test, int val1, int val2);
    int mul(test *test, int val1, int val2);
    double divi(test *test, int val1, int val2);


#ifdef __cplusplus
}
#endif
