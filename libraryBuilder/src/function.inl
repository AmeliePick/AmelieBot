#include <type_traits>


template<typename returnType>
inline void Function::call(void* result, Arguments * args)
{
    if (result != nullptr && typeid(returnType) != typeid(nullptr_t))
    {
        PyObject* res = PyObject_CallObject(pyFunc, args->get());

        if (typeid(returnType) == typeid(bool))
            (*(bool*)result) = PyLong_AsLong(res);
        else if (typeid(returnType) == typeid(char))
            (*(char*)result) = *PyUnicode_AsUTF8(res);
        else if (typeid(returnType) == typeid(int))
            (*(int*)result) = (int)PyLong_AsLong(res);
        else if (typeid(returnType) == typeid(double))
            (*(double*)result) = (double)PyFloat_AsDouble(res);
        else if (typeid(returnType) == typeid(const char))
            (*(char*)result) = *PyBytes_AsString(res);
    }
}
