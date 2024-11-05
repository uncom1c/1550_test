import ctypes
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


testpp = ctypes.CDLL('./libtestpp.so')

testpp.test_new.restype = ctypes.c_void_p
test = testpp.test_new()

##
# Работа с методами
##
a = 3
b = 6
c = 6.6
d = 3.3

testpp.sum.restype = ctypes.c_int
testpp.sum.argtypes = [ctypes.c_void_p, ctypes.c_int]
testpp.sub.restype = ctypes.c_int
testpp.sub.argtypes = [ctypes.c_void_p, ctypes.c_int]
testpp.mul.restype = ctypes.c_int
testpp.mul.argtypes = [ctypes.c_void_p, ctypes.c_int]

# Указываем, что функция возвращает double
testpp.divi.restype = ctypes.c_double
# Указываем, что функция принимает аргумент void * и double
testpp.divi.argtypes = [ctypes.c_void_p, ctypes.c_int]

print('Работа с методами:')
# В качестве 1-ого аргумента передаем указатель на наш класс
print('ret sum: ', testpp.sum(test, a, b))
print('ret sub: ', testpp.sub(test, a, b))
print('ret mul: ', testpp.mul(test, a, b))
print('ret div: ', testpp.divi(test, a, b))

# Указываем, что функция принимает аргумент void *
testpp.test_del.argtypes = [ctypes.c_void_p]
# Удаляем класс
testpp.test_del(test)


class operation(str, Enum):
    div = "div"
    sub = "sub"
    sum = "sum"
    mul = "mul"


class schemacalc(BaseModel):
    a: int
    b: int
    op: operation


@app.post("/calc")
async def calc(typeab: schemacalc):
    whattodo = typeab.op
    a = typeab.a
    b = typeab.b
    if whattodo == "div":
        if b != 0:
            return {"result": testpp.divi(test, a, b)}
        else:
            return {"result": "НА НОЛЬ НЕ ДЕЛИМ"}
    elif whattodo == "sub":
        return {"result": testpp.sub(test, a, b)}
    elif whattodo == "sum":
        return {"result": testpp.sum(test, a, b)}
    elif whattodo == "mul":
        return {"result": testpp.mul(test, a, b)}
