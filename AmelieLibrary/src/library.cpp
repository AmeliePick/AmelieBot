#include "library.h"
#include <iostream>



// MAIN MODULE

library::main::Amelie::Amelie(const char* appLanguage) : Class("Amelie", "Amelie", Function::Arguments(appLanguage))
{

}



library::main::Amelie* library::main::Amelie::getInstance(const char* appLanguage)
{
    static Amelie* instance = new Amelie(appLanguage);
    return instance;
}



void library::main::Amelie::changeLanguage(const char* language)
{
    Function::Arguments arg(language);
    callMethod("changeLanguage", arg);
}



char* library::main::Amelie::conversation(bool enableVoice, const char* userInput)
{
    Function::Arguments arg(enableVoice, userInput);
    return callMethod("conversation", arg).ToString();
}



void library::main::Amelie::tts(const char* pharse)
{
    Function::Arguments arg(pharse);
    callMethod("tts", arg);
}



bool library::main::Amelie::getVoice()
{
    Function::Arguments arg;
    return callMethod("getVoice", arg).ToBool();
}



const char* library::main::Amelie::getUserInput()
{
    Function::Arguments arg;
    return callMethod("getUserInput", arg).ToString();
}



library::main::Amelie::~Amelie()
{
    Function::Arguments arg;
    callMethod("__del__", arg);
}




library::main::Settings::Settings() : Class("Settings", "Settings", Function::Arguments())
{

}



library::main::Settings* library::main::Settings::getInstance()
{
    static Settings* instance = new Settings();
    return instance;
}



void library::main::Settings::setLanguage(const char* langValue)
{
    Function::Arguments arg(langValue);
    callMethod("setLanguage", arg);
}



bool library::main::Settings::setUsername(const char* nameValue)
{
    Function::Arguments arg(nameValue);
    return callMethod("setUsername", arg).ToBool();
}



void library::main::Settings::setBotAvatar(const char* avatarName)
{
    Function::Arguments arg(avatarName);
    callMethod("setBotAvatar", arg);
}



void library::main::Settings::setUserAvatar(const char* avatarName)
{
    Function::Arguments arg(avatarName);
    callMethod("setUserAvatar", arg);
}



const char* library::main::Settings::getLanguage()
{
    Function::Arguments arg;
    return callMethod("getLanguage", arg).ToString();
}



std::vector<const char*> library::main::Settings::getSupportingLangs()
{
    Function::Arguments arg;
    return callMethod("getSupportingLangs", arg).ToVector<const char*>();
}



std::vector<const char*> library::main::Settings::getBotAvatars()
{
    Function::Arguments arg;
    return callMethod("getBotAvatars", arg).ToVector<const char*>();
}



std::vector<const char*> library::main::Settings::getUserAvatars()
{
    Function::Arguments arg;
    return callMethod("getUserAvatars", arg).ToVector<const char*>();
}



const char* library::main::Settings::getBotAvatar()
{
    Function::Arguments arg;
    return callMethod("getBotAvatar", arg).ToString();
}



const char* library::main::Settings::getUserAvatar()
{
    Function::Arguments arg;
    return callMethod("getUserAvatar", arg).ToString();
}



const char* library::main::Settings::getUsername()
{
    Function::Arguments arg;
    return callMethod("getUsername", arg).ToString();
}



std::multimap<const char*, void*> library::main::Settings::getMethodsToResolveErrors()
{
    Function::Arguments arg;
    return callMethod("getMethodsToResolveErrors", arg).ToMultimap<const char*, void*>();
}



library::main::Settings::~Settings()
{
    Function::Arguments arg;
    callMethod("__del__", arg);
}
