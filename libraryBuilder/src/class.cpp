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



ReturnType Class::callStaticMethod(const char* moduleName, const char* className, const char* methodName, Function::Arguments& args)
{
    PyObject* _className = Interpreter::init()->loadClass(moduleName, className);

    Function func(_className, methodName);

    return func.call(args);
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
