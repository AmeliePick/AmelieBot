#include "interpreter.h"
#include <vector>


Interpreter::Interpreter(const char* workDir = "")
{
    Py_Initialize();
    PyObject* sys = PyImport_ImportModule("sys");
    PyObject* path = PyObject_GetAttrString(sys, "path");
    PyList_Append(path, PyUnicode_FromString(workDir));
}



Interpreter* Interpreter::init(const const char* workDir)
{
    static Interpreter* instance = new Interpreter(workDir);
    return instance;

}



PyObject* Interpreter::initModule(const char* moduleName)
{
    PyObject* module = PyUnicode_FromString(moduleName);
    PyObject* moduleHandle = PyImport_Import(module);
    
    modules.push_back(moduleHandle);
    Py_DECREF(module);
    
    // TODO: write data of possible errors to log.

    return moduleHandle;
}



PyObject* Interpreter::loadClass(const char* moduleName, const char* className)
{
    return this->loadClass(initModule(moduleName), className);
}



PyObject* Interpreter::loadClass(PyObject* moduleHandle, const char* className)
{
    if (moduleHandle == nullptr) return nullptr;
    
    PyObject* dict = PyModule_GetDict(moduleHandle);
    PyObject* python_class = PyDict_GetItemString(dict, className);

    objects.push_back(python_class);
    Py_DECREF(dict);

    // TODO: write data of possible errors to log.

    return python_class;
}



PyObject* Interpreter::loadFunction(const char* moduleName, const char* functionName)
{
    return this->loadFunction(initModule(moduleName), functionName);
}



PyObject* Interpreter::loadFunction(PyObject* moduleHandle, const char* functionName)
{
    if (moduleHandle == nullptr) return nullptr;

    PyObject* function = PyObject_GetAttrString(moduleHandle, functionName);

    objects.push_back(function);

    // TODO: write data of possible errors to log.

    return function;
}



Interpreter::~Interpreter()
{
    /* Py_Finalize() isn't working.
     * Log: Assertion failed: _PyGCHead_REFS(gc) != 0, file ..\Modules\gcmodule.c, line 380
     *
     * API: https://docs.python.org/2/c-api/init.html#c.Py_Finalize
     */


    // Manualy decrement objects references.
    for (int i = objects.size() - 1; i >= 0; --i)
    {
        Py_DECREF(objects[i]);
    }
    for (int i = modules.size() - 1; i >= 0; --i)
    {
        Py_DECREF(modules[i]);
    }

    
    // Here should be Py_Finalize calling.
}
