#include <type_traits>



template<typename keyType, typename valueType>
inline std::multimap<keyType, valueType> ReturnType::ToDict()
{
    PyObject* keys = PyDict_Keys(value);
    PyObject* values = PyDict_Values(value);


    keyType* keyDecoded = (keyType*)malloc(sizeof(keyType));
    valueType* valueDecoded = (valueType*)malloc(sizeof(valueType));


    std::multimap<keyType, valueType> dict;
    for (int i = 0; i < PyDict_Size(value); ++i)
    {
        ToType<keyType>(PyList_GetItem(keys, i), keyDecoded);
        ToType<keyType>(PyList_GetItem(values, i), keyDecoded);

        dict.insert(std::pair<keyType, valueType>(*keyDecoded, *valueDecoded));
    }


    free(keyDecoded);
    free(valueDecoded);

    return dict;
}



template<typename Type>
inline void ReturnType::ToType(PyObject* obj, void* decodedMemory)
{
    if (std::is_same<Type, bool>::value)
        *(bool*)decodedMemory = PyLong_AsLong(obj);
    else if (std::is_same<Type, char>::value)
        *(char*)decodedMemory = *PyUnicode_AsUTF8(obj);
    else if (std::is_same<Type, int>::value)
        *(long*)decodedMemory = PyLong_AsLong(obj);
    else if (std::is_same<Type, double>::value)
        *(double*)decodedMemory = PyFloat_AsDouble(obj);
    else if (std::is_same<Type, const char>::value)
        *(char*)decodedMemory = *PyUnicode_AsUTF8(value);
}