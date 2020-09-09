#include "utils/types_conversion.h"


template<typename keyType, typename valueType>
inline std::multimap<keyType, valueType> ReturnType::ToDict()
{
    PyObject* keys = PyDict_Keys(value);
    PyObject* values = PyDict_Values(value);


    void* keyDecoded = nullptr;
    void* valueDecoded = nullptr;


    std::multimap<keyType, valueType> dict;
    for (int i = 0; i < PyDict_Size(value); ++i)
    {
        ToType<keyType>(PyList_GetItem(keys, i), &keyDecoded);
        ToType<valueType>(PyList_GetItem(values, i), &valueDecoded);

        dict.insert(std::pair<keyType, valueType>(pointer_data<keyType>(keyDecoded), pointer_data<valueType>(valueDecoded)));
    }


    if (std::is_same<keyType, const char*>::value == false && std::is_same<keyType, void*>::value == false)
        free(keyDecoded);

    if (std::is_same<valueType, const char*>::value == false && std::is_same<valueType, void*>::value == false)
        free(valueDecoded);

    return dict;
}
