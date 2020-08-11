#pragma once
#include "function.h"



class Class
{
private:
    PyObject* pyClass;
    const char* moduleName;


public:
    Class() = delete;

    Class(const char* moduleName, const char* className);

    void constructor(Function::Arguments* args);

    template<typename returnType>
    void callMethod(const char* methodName, returnType* result, Function::Arguments* args);


    ~Class();
};

#include "class.inl"
