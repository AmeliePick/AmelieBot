#include "interpreter.h"



Interpreter* Interpreter::init(char* workDir)
{
    Py_Initialize();
    PyObject* sys = PyImport_ImportModule("sys");
    PyObject* path = PyObject_GetAttrString(sys, "path");
    PyList_Append(path, PyUnicode_FromString(workDir));
}



PyObject* Interpreter::initModule(char* moduleName)
{
    PyObject* module = PyUnicode_FromString(moduleName);
    PyObject* moduleHandle = PyImport_Import(module);
    
    // TODO: write data of possible errors to log.

    return moduleHandle;
}



PyObject* Interpreter::loadClass(char* moduleName, char* className)
{
    return this->loadClass(initModule(moduleName), className);
}



PyObject* Interpreter::loadClass(PyObject* moduleHandle, char* className)
{
    if (moduleHandle == nullptr) return nullptr;
    
    PyObject* dict = PyModule_GetDict(moduleHandle);
    PyObject* python_class = PyDict_GetItemString(dict, className);

    // TODO: write data of possible errors to log.

    return python_class;
}



PyObject* Interpreter::loadFunction(char* moduleName, char* functionName)
{
    return this->loadFunction(initModule(moduleName), functionName);
}



PyObject* Interpreter::loadFunction(PyObject* moduleHandle, char* functionName)
{
    if (moduleHandle == nullptr) return nullptr;

    // TODO: write data of possible errors to log.

    return PyObject_GetAttrString(moduleHandle, functionName);
}



Interpreter::~Interpreter()
{
    Py_Finalize();
}
