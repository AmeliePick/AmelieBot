#include <Windows.h>
#include <interpreter.h>

BOOL WINAPI DllMain(HINSTANCE const instance, DWORD const reason, LPVOID const reserved)
{
    switch (reason)
    {
    case DLL_PROCESS_ATTACH:
        Interpreter::init(L"python");
        break;

    case DLL_THREAD_ATTACH:
        break;

    case DLL_THREAD_DETACH:
        break;

    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}