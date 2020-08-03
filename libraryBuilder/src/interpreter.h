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

    PyObject* loadClass(char* className);

    PyObject* loadFunction(char* functionName);



    ~Interpreter();
};