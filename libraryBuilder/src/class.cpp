#include "class.h"



Class::Class(const char* moduleName, const char* className)
{
    this->moduleName = moduleName;
    this->pyClass = Interpreter::init("")->loadClass(moduleName, className);
}



void Class::constructor(Function::Arguments* args)
{
    PyObject_CallObject(pyClass, args->get());
}



Class::~Class()
{
    PyObject_CallMethod(pyClass, "__del__", nullptr);
    delete pyClass;
}
