#pragma once
#include <vector>
#include "python/interpreter.h"
#define function class



class Function
{
private:
    PyObject* pyFunc;
    const char* returnType;

public:
    class Arguments
    {
    private:
        PyObject* args;

        PyObject* Args_Pack(size_t n, std::vector<PyObject*>* args);

    public:
        Arguments() = delete;

        Arguments(int argsCount, const char* typeDecoder, ...);


        PyObject* get();

    };


    Function() = delete;
    Function(PyObject* moduleHandle, const char* functionName, const char* returnType);
    Function(const char* moduleName, const char* functionName, const char* returnType);

    void operator ()(void* result, Arguments* args);
};
