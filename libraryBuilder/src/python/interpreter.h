#pragma once
#include <Python.h>
#include <vector>


class Interpreter
{
private:
    Interpreter();
    Interpreter(const Interpreter &);

    class Logger* logger;

    std::vector<PyObject*> modules;
    std::vector<PyObject*> objects;

    Interpreter(const char* workDir);

public:
    // -- Interpreter initialization --
    static Interpreter* init();


    // -- Get the handle of python module --
    // * moduleName: the module name without file format.
    PyObject* initModule(const char* moduleName);

    PyObject* loadClass(const char* moduleName, const char* className);

    PyObject* loadClass(PyObject* moduleHandle, const char* className);

    PyObject* loadFunction(const char* moduleName, const char* functionName);

    PyObject* loadFunction(PyObject* moduleHandle, const char* functionName);


    void Python_traceback_toFile();

    void deleteObject(PyObject* object);


    ~Interpreter();
};
