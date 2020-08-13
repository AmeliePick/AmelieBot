#include "function.h"
#include "python/interpreter.h"
#include <vector>
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
    this->pyFunc = Interpreter::init()->loadFunction(moduleHandle, functionName);
}



Function::Function(const char* moduleName, const char* functionName)
{
    this->pyFunc = Interpreter::init()->loadFunction(moduleName, functionName);
}




Function::Arguments::Arguments()
{
    this->args = nullptr;
    this->argsVector = nullptr;
}



PyObject* Function::Arguments::get()
{
    return args;
}



Function::~Function()
{
    // The function will be deleted in interpreter.
}



Function::Arguments::~Arguments()
{
    if (argsVector)
    {
        for (int i = 0; i < argsVector->size(); ++i)
        {
            
            Py_DECREF((*argsVector)[i]);
        }

        delete argsVector;
    }

    if(args) Py_DECREF(args);
}
