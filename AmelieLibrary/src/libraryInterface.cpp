#include <iostream>
#include "libraryInterface.h"


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



__declspec(dllexport) void AmelieDelete(Amelie* object)
{
    delete object;
}





__declspec(dllexport) Settings* getInstance()
{
    return Settings::getInstance();
}



__declspec(dllexport) void setLanguage(Settings* object, const char* langValue)
{
    object->setLanguage(langValue);
}



__declspec(dllexport) void setUsername(Settings* object, const char* nameValue)
{
    object->setUsername(nameValue);
}



__declspec(dllexport) const char * getLanguage(Settings* object)
{
    return nullptr;
}



__declspec(dllexport) std::multimap<int, const char*> getSupportingLangs(Settings* object)
{
    return object->getSupportingLangs();
}



__declspec(dllexport) const char * getUsername(Settings* object)
{
    return object->getUsername();
}



__declspec(dllexport) std::multimap<const char*, void*> getMethodsToResolveErrors(Settings* object)
{
    return object->getMethodsToResolveErrors();
}



__declspec(dllexport) void SettingsDelete(Settings* object)
{
    delete object;
}
