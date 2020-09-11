#pragma once
#include "function.h"



class Class
{
private:
    PyObject* pyClass;
    std::multimap<const char*, Function> loadedMethods;

protected:
    Class() = delete;

    Class(const char* moduleName, const char* className, Function::Arguments&& args);

    static ReturnType callStaticMethod(const char* moduleName, const char* className, const char* methodName, Function::Arguments& args);

    ReturnType callMethod(const char* methodName, Function::Arguments& args);


    ~Class(); 
};