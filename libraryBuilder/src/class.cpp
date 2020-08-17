#include "class.h"
#include "python/interpreter.h"


Class::Class(const char* moduleName, const char* className, Function::Arguments&& args)
{
    PyObject* _class = Interpreter::init()->loadClass(moduleName, className);

    if (_class != nullptr)
    {
        pyClass = PyObject_CallObject(_class, args.get());
        Py_DECREF(_class);
    }   
}



ReturnType Class::callMethod(const char* methodName, Function::Arguments& args)
{
    Function func(pyClass, methodName);

    return func.call(args);
}



Class::~Class()
{
    PyObject_CallMethod(pyClass, "__del__", nullptr);

    // The class will be deleted in interpreter.
}
