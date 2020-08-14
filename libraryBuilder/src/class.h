#pragma once
#include "function.h"



class Class
{
private:
    PyObject* pyClass;

protected:
    Class() = delete;

    Class(const char* moduleName, const char* className, Function::Arguments&& args);

    void callMethod(const char* methodName, void* result, Function::Arguments& args);


    ~Class(); 
};
