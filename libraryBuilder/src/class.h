#pragma once
#include "function.h"



class Class
{
private:
    PyObject* pyClass;
    const char* moduleName;


public:
    Class() = delete;

    Class(const char* moduleName, const char* className, Function::Arguments args);


    void callMethod(const char* methodName, void* result, Function::Arguments args);


    ~Class();
};
