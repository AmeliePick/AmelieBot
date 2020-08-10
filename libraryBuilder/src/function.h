#pragma once
#include <typeinfo>
#include <vector>
#include "python/interpreter.h"
#define function class



class Function
{
private:
    PyObject* pyFunc;

public:
    class Arguments
    {
    private:
        PyObject* args;
        std::vector<PyObject*> argsVector;
        

        PyObject* Args_Pack(size_t n, std::vector<PyObject*>* args);
        
        template<typename Type>
        void arguments(Type* object);

        template<typename Type>
        void arguments(Type object);

        template<typename Type, typename ...Types>
        void arguments(Type t, Types... types);

    public:
        Arguments() = delete;

        template<typename Type, typename ...Types>
        Arguments(Type t, Types... types);


        PyObject* get();

    };


    Function() = delete;
    Function(PyObject* moduleHandle, const char* functionName);
    Function(const char* moduleName, const char* functionName);

    template<typename returnType = nullptr_t>
    void call(void* result, Arguments* args);
};

#include "function.inl"
#include "function_arguments.inl"
