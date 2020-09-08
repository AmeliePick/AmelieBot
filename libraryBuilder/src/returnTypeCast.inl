#include <type_traits>
#include "function.h"



template<typename Type>
inline Type ReturnType::pointer_cast(void** pointer)
{
    if (std::is_same<Type, const char*>::value || std::is_same<Type, void*>::value)
        return *(Type*)pointer;
    return **(Type**)pointer;
}



template<typename keyType, typename valueType>
inline std::multimap<keyType, valueType> ReturnType::ToDict()
{
    PyObject* keys = PyDict_Keys(value);
    PyObject* values = PyDict_Values(value);


    void** keyDecoded = (void**)malloc(sizeof(void*));
    void** valueDecoded = (void**)malloc(sizeof(void*));

    *keyDecoded = *valueDecoded = nullptr;


    std::multimap<keyType, valueType> dict;
    for (int i = 0; i < PyDict_Size(value); ++i)
    {
        ToType<keyType>(PyList_GetItem(keys, i), keyDecoded);
        ToType<valueType>(PyList_GetItem(values, i), valueDecoded);

        dict.insert(std::pair<keyType, valueType>(pointer_cast<keyType>(keyDecoded), pointer_cast<valueType>(valueDecoded)));
    }


    free(keyDecoded);
    free(valueDecoded);

    return dict;
}



template<typename Type>
inline void ReturnType::ToType(PyObject* obj, void** decodedMemory)
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
        **(long**)decodedMemory = PyLong_AsLong(obj);
    else if (std::is_same<Type, double>::value)
        *(double*)decodedMemory = PyFloat_AsDouble(obj);
}