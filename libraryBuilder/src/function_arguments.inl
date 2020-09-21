


template<typename Type, typename ...Types>
Function::Arguments::Arguments(Type t, Types ...types)
{
    this->argsVector = new std::vector<PyObject*>;

    arguments(t, types...);
    this->args = Args_Pack(1 + sizeof...(types), argsVector);
}



template<typename Type>
inline void Function::Arguments::arguments(Type* object)
{
    if (typeid(object) == typeid(bool*))
        this->argsVector->push_back(PyBool_FromLong((long)(*object)));
    else if (typeid(object) == typeid(char*))
        this->argsVector->push_back(PyUnicode_FromOrdinal((int)(*object)));
    else if (typeid(object) == typeid(int*))
        this->argsVector->push_back(PyLong_FromLong((int)(*object)));
    else if (typeid(object) == typeid(double*))
        this->argsVector->push_back(PyFloat_FromDouble(*object));
    else if (typeid(object) == typeid(const char*))
        /* In Python 3 string object represented internally as a sequence of Unicode codepoints.
         * So it can be created by PyUnicode_FromString and we will get Python string.
         * In Python code we can check the type of the variable: type(var) and get "str" type name.
         *
         * Also we can create a string by str-method(in Python 3 code) and PyObject_Str(using Python API).
         * But in Python 3 the string is already represented by unicode bytes.
         *
         * So, the guess is that first and second ways are the same and will take python string in unicode represente.
         * And if python variable must be as str object, it can be created by PyUnicode_FromString or PyObject_Str.
         *
         *
         * Python API about types: https://docs.python.org/3/c-api/object.html
         * Python string and unicode: https://medium.com/better-programming/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686
         *
         */
        this->argsVector->push_back(PyUnicode_FromString(object));
}



template<typename Type>
void Function::Arguments::arguments(Type object)
{
    if (typeid(object) == typeid(bool))
        this->argsVector->push_back(PyBool_FromLong((long)object));
    else if (typeid(object) == typeid(char))
        this->argsVector->push_back(PyUnicode_FromOrdinal((int)object));
    else if (typeid(object) == typeid(int))
        this->argsVector->push_back(PyLong_FromLong((int)object));
    else if (typeid(object) == typeid(double))
        this->argsVector->push_back(PyFloat_FromDouble(object));
}



template<typename Type, typename ...Types>
inline void Function::Arguments::arguments(Type t, Types ...types)
{
    arguments(t);
    arguments(types...);
}