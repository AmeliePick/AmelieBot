#include "function.h"
#include <cstdarg>


// Python library method overriding
PyObject* Function::Arguments::Args_Pack(size_t n, std::vector<PyObject*>* args)
{
    Py_ssize_t i;
    PyObject *obj;
    PyObject *result;
    PyObject **items;
    va_list vargs;

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



Function::Function(PyObject* moduleHandle, const char* functionName, const char* returnType) : returnType(returnType)
{
    this->pyFunc = Interpreter::init("")->loadFunction(moduleHandle, functionName);
}



Function::Function(const char* moduleName, const char* functionName, const char* returnType) : returnType(returnType)
{
    this->pyFunc = Interpreter::init("")->loadFunction(moduleName, functionName);
}



Function::Arguments::Arguments(int argsCount, const char* typeDecoder, ...)
{
    if (argsCount == 0) return;

    std::vector<PyObject*> argsObjects = std::vector<PyObject*>();

    va_list args;
    va_start(args, typeDecoder);

    bool isPointer = false;
    for (int index = 0; index <= argsCount; ++index)
    {
        //TODO: Remake it.

        if (typeDecoder[index] == 'b' && isPointer)
        {
            bool* ptr = va_arg(args, bool*);
            argsObjects.push_back(PyBool_FromLong((long)(*ptr)));
        }
        else if (typeDecoder[index] == 'b')
        {
            argsObjects.push_back(PyBool_FromLong(va_arg(args, long)));
        }
        else if (typeDecoder[index] == 'c' && isPointer)
        {
            char* ptr = va_arg(args, char*);
            argsObjects.push_back(PyUnicode_FromOrdinal((int)(*ptr)));
        }
        else if (typeDecoder[index] == 'c')
        {
            argsObjects.push_back(PyUnicode_FromOrdinal(va_arg(args, int)));
        }
        else if (typeDecoder[index] == 'i' && isPointer)
        {
            __int64* ptr = va_arg(args, __int64*);
            argsObjects.push_back(PyLong_FromLong((long)(*ptr)));
        }
        else if (typeDecoder[index] == 'i')
        {
            argsObjects.push_back(PyLong_FromLong(va_arg(args, long)));
        }
        else if (typeDecoder[index] == 'd' && isPointer)
        {
            double* ptr = va_arg(args, double*);
            argsObjects.push_back(PyFloat_FromDouble(*ptr));
        }
        else if (typeDecoder[index] == 'd')
        {
            argsObjects.push_back(PyFloat_FromDouble(va_arg(args, double)));
        }
        else if (typeDecoder[index] == 's' && isPointer)
        {
            const char* ptr = va_arg(args, const char*);
            argsObjects.push_back(PyUnicode_FromString((const char*)(*ptr)));
        }
        else if (typeDecoder[index] == 's')
        {
            argsObjects.push_back(PyUnicode_FromString(va_arg(args, const char*)));
        }

        if (isPointer) isPointer = false;

        if (typeDecoder[index] == '*') isPointer = true;
    }

    this->args = Args_Pack(argsCount, &argsObjects);
}



PyObject* Function::Arguments::get()
{
    return args;
}



void Function::operator()(void* result, Arguments* args)
{
    PyObject* res = PyObject_CallObject(pyFunc, args->get());


}
