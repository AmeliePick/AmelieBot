#include "function.h"
#include <cstdarg>


// Python library method overriding
PyObject* Function::Arguments::Args_Pack(size_t n, std::vector<PyObject*>* args)
{
    size_t i;
    PyObject *obj;
    PyObject *result;
    PyObject **items;

    result = PyTuple_New(n);
    if (result == NULL) {
        args->clear();
        return NULL;
    }
    items = ((PyTupleObject *)result)->ob_item;
    for (i = 0; i < n; i++) {
        obj = (PyObject*)(*args)[i];
        Py_INCREF(obj);
        items[i] = obj;
    }
    return result;
}



Function::Function(PyObject* moduleHandle, const char* functionName)
{
    this->pyFunc = Interpreter::init("")->loadFunction(moduleHandle, functionName);
}



Function::Function(const char* moduleName, const char* functionName)
{
    this->pyFunc = Interpreter::init("")->loadFunction(moduleName, functionName);
}



PyObject* Function::Arguments::get()
{
    return args;
}
