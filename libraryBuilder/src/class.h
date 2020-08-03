#pragma once
#include <map>


class Class
{
private:
    class PyObject* self;
    std::map<char*, PyObject*> methods;


public:
    Class() = delete;

    Class(char* pyClass);
};