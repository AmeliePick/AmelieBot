#include "function.h"
#include "python/interpreter.h"
#include <vector>
#include <cstdarg>



ReturnType::ReturnType(PyObject* pyReturnValue) : value(pyReturnValue)
{

}



ReturnType::ReturnType(ReturnType && rvalue) : value(rvalue.value)
{
    rvalue.value = nullptr;
}



bool ReturnType::ToBool()
{
    return PyLong_AsLong(value);
}



char ReturnType::ToChar()
{
    return *PyUnicode_AsUTF8(value);
}



int ReturnType::ToLong()
{
    return PyLong_AsLong(value);
}



double ReturnType::ToDouble()
{
    return PyFloat_AsDouble(value);
}



const char* ReturnType::ToString()
{
    return PyUnicode_AsUTF8(value);
}



PyObject ReturnType::ToPyObject()
{
    return *value;
}



ReturnType::~ReturnType()
{
    if (value) Py_DECREF(value);
}



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



Function::Function(PyObject* pyFunction) : pyFunc(pyFunction)
{

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





ReturnType Function::call(Arguments& args)
{
    return ReturnType(PyObject_CallObject(pyFunc, args.get()));
}



Function::~Function()
{
    Interpreter::init()->deleteObject(pyFunc);
}



Function::Arguments::~Arguments()
{
    if (argsVector)
    {
        for (int i = 0; i < argsVector->size(); ++i)
        {
            
            Py_CLEAR((*argsVector)[i]);
        }

        delete argsVector;
    }

    if(args) Py_CLEAR(args);
}
