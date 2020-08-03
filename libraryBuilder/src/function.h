#pragma once


template<typename retrunType>
class Function
{
private:
    class PyObject* pyFunc;

public:
    class Arguments
    {
    private:
        PyObject* args;


    public:
        Arguments() = delete;

        Arguments(int argsCount, const char* typeDecoder, ...);

    };


    Function() = delete;
    Function(char* functionName);

    retrunType operator ()(Arguments* args);
};