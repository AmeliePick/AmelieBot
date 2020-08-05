#pragma once
#include <Python.h>



class Interpreter
{
private:
    Interpreter();
    Interpreter(const Interpreter &);


    Interpreter(const char* workDir);

public:
    // -- Interpreter initialization --
    // * workDir: working directory is a path to python code.
    static Interpreter* init(const char* workDir);


    // -- Get the handle of python module --
    // * moduleName: the module name without file format.
    PyObject* initModule(const char* moduleName);

    PyObject* loadClass(const char* moduleName, const char* className);

    PyObject* loadClass(PyObject* moduleHandle, const char* className);

    PyObject* loadFunction(const char* moduleName, const char* functionName);

    PyObject* loadFunction(PyObject* moduleHandle, const char* functionName);



    ~Interpreter();
};
