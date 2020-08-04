#pragma once
#include <Python.h>



class Interpreter
{
private:
    Interpreter();
    Interpreter(const Interpreter &);

public:
    // -- Interpreter initialization --
    // * workDir: working directory is a path to python code.
    static Interpreter* init(char* workDir);


    // -- Get the handle of python module --
    // * moduleName: the module name without file format.
    PyObject* initModule(char* moduleName);

    PyObject* loadClass(char* moduleName, char* className);

    PyObject* loadClass(PyObject* moduleHandle, char* className);

    PyObject* loadFunction(char* moduleName, char* functionName);

    PyObject* loadFunction(PyObject* moduleHandle, char* functionName);



    ~Interpreter();
};
