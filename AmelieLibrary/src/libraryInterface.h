#pragma once
#include "library.h"

#define Amelie library::main::Amelie
#define Settings library::main::Settings



extern "C" __declspec(dllexport) void* AmelieCreateInstance(const char* appLanguage);

extern "C" __declspec(dllexport) void AmelieChangeLanguage(Amelie* object, const char* language);

extern "C" __declspec(dllexport) char* AmelieConversation(Amelie* object, bool enableVoice, const char* userInput);

extern "C" __declspec(dllexport) void AmelieTTS(Amelie* object, const char* pharse);

extern "C" __declspec(dllexport) bool AmelieGetVoice(Amelie* object);

extern "C" __declspec(dllexport) const char* AmelieGetUserInput(Amelie* object);

extern "C" __declspec(dllexport) void AmelieDelete(Amelie* object);



extern "C" __declspec(dllexport) Settings* SettingsGetInstance();

extern "C" __declspec(dllexport) void setLanguage(Settings* object, const char* langValue);

extern "C" __declspec(dllexport) bool setUsername(Settings* object, const char* nameValue);

extern "C" __declspec(dllexport) const char* getLanguage(Settings* object);

extern "C++" __declspec(dllexport) std::vector<const char*> getSupportingLangs(Settings* object);

extern "C" __declspec(dllexport) const char* getUsername(Settings* object);

extern "C++" __declspec(dllexport) std::vector<const char*> getBotAvatars(Settings* object);

extern "C++" __declspec(dllexport) std::vector<const char*> getUserAvatars(Settings* object);

extern "C" __declspec(dllexport) const char* getBotAvatar(Settings* object);

extern "C" __declspec(dllexport) const char* getUserAvatar(Settings* object);

extern "C" __declspec(dllexport) void setBotAvatar(Settings* object, const char* avatarName);

extern "C" __declspec(dllexport) void setUserAvatar(Settings* object, const char* avatarName);

extern "C++" __declspec(dllexport) std::multimap<const char*, void*> getMethodsToResolveErrors(Settings* object);

extern "C" __declspec(dllexport) void SettingsDelete(Settings* object);


