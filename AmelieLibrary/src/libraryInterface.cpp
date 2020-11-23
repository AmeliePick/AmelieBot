#include "libraryInterface.h"
#include <map>




__declspec(dllexport) void* AmelieCreateInstance(const char* appLanguage)
{
    return Amelie::getInstance(appLanguage);
}



__declspec(dllexport) void AmelieChangeLanguage(Amelie* object, const char* language)
{
    object->changeLanguage(language);
}



__declspec(dllexport) char* AmelieConversation(Amelie* object, bool enableVoice, const char* userInput)
{
    return object->conversation(enableVoice, userInput);
}



__declspec(dllexport) void AmelieTTS(Amelie* object, const char* pharse)
{
    object->tts(pharse);
}



__declspec(dllexport) bool AmelieGetVoice(Amelie* object)
{
    return object->getVoice();
}



__declspec(dllexport) const char* AmelieGetUserInput(Amelie* object)
{
    return object->getUserInput();
}



__declspec(dllexport) void AmelieDelete(Amelie* object)
{
    delete object;
}





__declspec(dllexport) Settings* SettingsGetInstance()
{
    return Settings::getInstance();
}



__declspec(dllexport) void setLanguage(Settings* object, const char* langValue)
{
    object->setLanguage(langValue);
}



__declspec(dllexport) bool setUsername(Settings* object, const char* nameValue)
{
    return object->setUsername(nameValue);
}



__declspec(dllexport) const char* getLanguage(Settings* object)
{
    return object->getLanguage();
}



__declspec(dllexport) std::vector<const char*> getSupportingLangs(Settings* object)
{
    return object->getSupportingLangs();
}



__declspec(dllexport) const char* getUsername(Settings* object)
{
    return object->getUsername();
}



__declspec(dllexport) std::vector<const char*> getBotAvatars(Settings* object)
{
    return object->getBotAvatars();
}



__declspec(dllexport) std::vector<const char*> getUserAvatars(Settings* object)
{
    return object->getUserAvatars();
}



const char* getBotAvatar(Settings* object)
{
    return object->getBotAvatar();
}



const char* getUserAvatar(Settings* object)
{
    return object->getUserAvatar();
}



void setBotAvatar(Settings* object, const char* avatarName)
{
    object->setBotAvatar(avatarName);
}



void setUserAvatar(Settings* object, const char* avatarName)
{
    object->setUserAvatar(avatarName);
}



__declspec(dllexport) std::multimap<const char*, void*> getMethodsToResolveErrors(Settings* object)
{
    return object->getMethodsToResolveErrors();
}



__declspec(dllexport) void SettingsDelete(Settings* object)
{
    delete object;
}


