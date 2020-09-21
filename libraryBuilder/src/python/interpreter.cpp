#include "interpreter.h"
#include "../utils/logger.h"
#include <frameobject.h>



Interpreter::Interpreter()
{

    this->logger = Logger::create();

    Py_Initialize();
}



Interpreter* Interpreter::init()
{
    static Interpreter* instance = new Interpreter();
    return instance;

}



PyObject* Interpreter::initModule(const char* moduleName)
{
    PyObject* module = PyUnicode_FromString(moduleName);
    PyObject* moduleHandle = PyImport_Import(module);
    
    modules.push_back(moduleHandle);
    Py_CLEAR(module);
    
    Python_traceback_toFile();

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
    Py_CLEAR(dict);

    Python_traceback_toFile();

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

    Python_traceback_toFile();

    return function;
}



void Interpreter::Python_traceback_toFile()
{
    PyObject *ptype, *pvalue, *ptraceback;
    PyErr_Fetch(&ptype, &pvalue, &ptraceback);

    if (pvalue && pvalue && ptraceback)
    {
        PyTracebackObject tb = *(PyTracebackObject*)ptraceback;
        this->logger->writeLog(PyUnicode_AsUTF8(PyObject_Str((PyObject*)tb.tb_frame->f_code)));
        this->logger->writeLog(" ");
        this->logger->writeLog(PyUnicode_AsUTF8(PyObject_Str(pvalue)));
        this->logger->writeLog("\n");
    }
}



void Interpreter::deleteObject(PyObject* object)
{
    if (object != nullptr)
    {
        auto obj = std::find(objects.begin(), objects.end(), object);

        if (obj != objects.end())
        {
            Py_CLEAR(objects[std::distance(objects.begin(), obj)]);
            objects.erase(obj);
        }
        else
        {
            obj = std::find(modules.begin(), modules.end(), object);

            Py_CLEAR(modules[std::distance(modules.begin(), obj)]);
            modules.erase(obj);
        }
    }
}



Interpreter::~Interpreter()
{
    /* Py_Finalize() isn't working.
     * Log: Assertion failed: _PyGCHead_REFS(gc) != 0, file ..\Modules\gcmodule.c, line 380
     *
     * API: https://docs.python.org/2/c-api/init.html#c.Py_Finalize
     */


    // Manualy delete objects instead Py_Finalize.
    for (int i = objects.size() - 1; i >= 0; --i)
    {
        Py_CLEAR(objects[i]);
    }
    for (int i = modules.size() - 1; i >= 0; --i)
    {
        Py_CLEAR(modules[i]);
    }

    
    // Here should be Py_Finalize calling.
}
