#include "class.h"



Class::Class(const char* moduleName, const char* className, Function::Arguments args)
{
    this->moduleName = moduleName;
    PyObject* _class = Interpreter::init()->loadClass(moduleName, className);

    if(_class != nullptr) pyClass = PyObject_CallObject(_class, args.get());

    Py_DECREF(_class);
}



void Class::callMethod(const char* methodName, void* result, Function::Arguments args)
{
    Function func(pyClass, methodName);

    func.call<int>(result, args);
}



Class::~Class()
{
    PyObject_CallMethod(pyClass, "__del__", nullptr);
    Py_DECREF(pyClass);
}