#include "class.h"
#include "python/interpreter.h"
#include <string>



Class::Class(const char* moduleName, const char* className, Function::Arguments&& args)
{
    loadedMethods = std::multimap<const char*, Function>();
    PyObject* _class = Interpreter::init()->loadClass(moduleName, className);

    if (_class != nullptr)
    {
        pyClass = PyObject_CallObject(_class, args.get());
        Py_CLEAR(_class);
    }   
}
 


ReturnType Class::callStaticMethod(const char* moduleName, const char* className, const char* methodName, Function::Arguments& args)
{
    // Storages all static method from all classes
    static std::multimap<const char*, Function> loadedStaticMethods = std::multimap<const char*, Function>();


    std::string strMethodString(methodName);
    auto elem = loadedStaticMethods.find(strMethodString.c_str());
    if (elem == loadedStaticMethods.end())
    {
        PyObject* _className = Interpreter::init()->loadClass(moduleName, className);
        auto func = loadedStaticMethods.insert(std::pair<const char*, Function>(strMethodString.c_str(), Function(_className, methodName)));

        if (func != loadedStaticMethods.end())
            return func->second.call(args);
        else return ReturnType(nullptr);
    }
    else
        return elem->second.call(args);
}



ReturnType Class::callMethod(const char* methodName, Function::Arguments& args)
{
    std::string strMethodString(methodName);
    auto elem = loadedMethods.find(strMethodString.c_str());
    if (elem == loadedMethods.end())
    {
        auto func = loadedMethods.insert(std::pair<const char*, Function>(strMethodString.c_str(), Function(pyClass, methodName)));

        if (func != loadedMethods.end())
            return func->second.call(args);
        else return ReturnType(nullptr);
    }
    else
        return elem->second.call(args);
}



Class::~Class()
{
    PyObject_CallMethod(pyClass, "__del__", nullptr);
    loadedMethods.clear();

    Interpreter::init()->deleteObject(pyClass);
}
