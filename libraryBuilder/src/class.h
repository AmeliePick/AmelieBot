#pragma once
#include "function.h"



class Class
{
private:
    PyObject* pyClass;

protected:
    Class() = delete;

    Class(const char* moduleName, const char* className, Function::Arguments&& args);

    ReturnType callMethod(const char* methodName, Function::Arguments& args);


    ~Class(); 
};
