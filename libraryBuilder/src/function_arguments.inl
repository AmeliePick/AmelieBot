


template<typename Type, typename ...Types>
Function::Arguments::Arguments(Type t, Types ...types)
{
    this->argsVector = std::vector<PyObject*>();

    arguments(t, types...);
    this->args = Args_Pack(1 + sizeof...(types), &argsVector);
}



template<typename Type>
inline void Function::Arguments::arguments(Type* object)
{
    if (typeid(object) == typeid(bool*))
        this->argsVector.push_back(PyBool_FromLong((long)(*object)));
    else if (typeid(object) == typeid(char*))
        this->argsVector.push_back(PyUnicode_FromOrdinal((int)(*object)));
    else if (typeid(object) == typeid(int*))
        this->argsVector.push_back(PyLong_FromLong((int)(*object)));
    else if (typeid(object) == typeid(double*))
        this->argsVector.push_back(PyFloat_FromDouble(*object));
    else if (typeid(object) == typeid(const char*))
        this->argsVector.push_back(PyUnicode_FromString(object));
}



template<typename Type>
void Function::Arguments::arguments(Type object)
{
    if (typeid(object) == typeid(bool))
        this->argsVector.push_back(PyBool_FromLong((long)object));
    else if (typeid(object) == typeid(char))
        this->argsVector.push_back(PyUnicode_FromOrdinal((int)object));
    else if (typeid(object) == typeid(int))
        this->argsVector.push_back(PyLong_FromLong((int)object));
    else if (typeid(object) == typeid(double))
        this->argsVector.push_back(PyFloat_FromDouble(object));
    else if (typeid(object) == typeid(const char))
        this->argsVector.push_back(PyUnicode_FromString((const char*)object));
}



template<typename Type, typename ...Types>
inline void Function::Arguments::arguments(Type t, Types ...types)
{
    arguments(t);
    arguments(types...);
}