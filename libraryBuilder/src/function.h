#pragma once
#include <Python.h>
#include <vector>
#include <map>
#include <typeinfo>



class ReturnType
{
private:
    PyObject* value;

    ReturnType() = delete;
    ReturnType(const ReturnType &) = delete;

    

public:
    ReturnType(PyObject* pyReturnValue);
    ReturnType(ReturnType &&);


    bool ToBool();

    char ToChar();

    int ToLong();

    double ToDouble();

    const char* ToString();

    PyObject ToPyObject();

    template<typename keyType, typename valueType>
    std::multimap<keyType, valueType> ToDict();

    
    

    ~ReturnType();
};






class Function
{
private:
    PyObject* pyFunc;

public:
    class Arguments
    {
    private:
        PyObject* args;
        std::vector<PyObject*>* argsVector;
        

        PyObject* Args_Pack(size_t n, std::vector<PyObject*>* args);
        
        template<typename Type>
        void arguments(Type* object);

        template<typename Type>
        void arguments(Type object);

        template<typename Type, typename ...Types>
        void arguments(Type t, Types... types);

    public:
        Arguments();
        Arguments(const Arguments &) = delete;

        template<typename Type, typename ...Types>
        Arguments(Type t, Types... types);


        PyObject* get();


        ~Arguments();
    };

    Function(const Function &) = delete;
    Function(Function &&);
    Function() = delete;
    Function(PyObject* pyFunction);
    Function(PyObject* moduleHandle, const char* functionName);
    Function(const char* moduleName, const char* functionName);

    
    ReturnType call(Arguments& args);


    ~Function();
};

#include "return_type.inl"
#include "function_arguments.inl"
