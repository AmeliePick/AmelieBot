


template<typename returnType>
inline void Function::operator()(void* result, Arguments * args)
{
    PyObject* res = PyObject_CallObject(pyFunc, args->get());

    // TODO: add return value converting.
}
