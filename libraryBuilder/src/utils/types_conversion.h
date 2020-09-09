#pragma once
#include <type_traits>

template<typename Type>
void ToType(PyObject* obj, void** decodedMemory)
{
    /* Python pointer is saving like PyObject. Then it's possible to call.
     *
     */


    if (*decodedMemory == nullptr && std::is_same<Type, const char*>::value == false)
        *decodedMemory = malloc(sizeof(Type));


    if (std::is_same<Type, const char*>::value)
    {
        const char* string = PyUnicode_AsUTF8(obj);

        if (*decodedMemory == nullptr)
            *decodedMemory = malloc(strlen(string) + 1);

        char* decodedString = *(char**)decodedMemory;
        for (int i = 0; i < strlen(string) + 1; ++i, ++decodedString)
        {
            *decodedString = string[i];
        }
    }
    else if (std::is_same<Type, void*>::value)
        **(PyObject**)decodedMemory = *obj;
    else if (std::is_same<Type, bool>::value)
        *(bool*)decodedMemory = PyLong_AsLong(obj);
    else if (std::is_same<Type, char>::value)
        *(char*)decodedMemory = *PyUnicode_AsUTF8(obj);
    else if (std::is_same<Type, int>::value)
        **(int**)decodedMemory = (int)PyLong_AsLong(obj);
    else if (std::is_same<Type, double>::value)
        *(double*)decodedMemory = PyFloat_AsDouble(obj);
}


template<typename Type>
Type pointer_data(void* pointer)
{
    if (std::is_same<Type, const char*>::value || std::is_same<Type, void*>::value)
        return (Type)pointer;
    else
        return *(Type*)pointer;
}
