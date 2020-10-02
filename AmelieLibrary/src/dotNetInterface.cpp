#include "dotNetInterface.h"
#include <iostream>


__declspec(dllexport) void* AmelieCreateInstance(const char* appLanguage)
{
    return Amelie::getInstance(appLanguage);
}



__declspec(dllexport) void AmelieChangeLanguage(Amelie* object, const char* language)
{
    object->changeLanguage(language);
}



__declspec(dllexport) char* AmelieConversation(Amelie* object, const char* userInput)
{
    return object->conversation(userInput);
}



__declspec(dllexport) void AmelieTTS(Amelie* object, const char* pharse)
{
    object->tts(pharse);
}



__declspec(dllexport) void AmelieUpdate(Amelie* object)
{
    object->update();
}



__declspec(dllexport) const char* AmelieGetPathToProgram(Amelie* object, const char* programName)
{
    return object->getPathToProgram(programName);
}



__declspec(dllexport) void AmelieAddProgram(Amelie* object, const char* program, const char* path)
{
    object->addProgram(program, path);
}



__declspec(dllexport) bool AmelieGetVoice(Amelie* object)
{
    return object->getVoice();
}



__declspec(dllexport) void AmelieSetVoice(Amelie* object, bool value)
{
    object->setVoice(value);
}



__declspec(dllexport) const char* AmelieGetUserInput(Amelie* object)
{
    return object->getUserInput();
}
