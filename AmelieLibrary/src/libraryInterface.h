#pragma once
#include "library.h"

#define Amelie library::main::Amelie
#define Settings library::main::Settings


extern "C" __declspec(dllexport) void* AmelieCreateInstance(const char* appLanguage);


extern "C" __declspec(dllexport) void AmelieChangeLanguage(Amelie* object, const char* language);

extern "C" __declspec(dllexport) char* AmelieConversation(Amelie* object, const char* userInput);

extern "C" __declspec(dllexport) void AmelieTTS(Amelie* object, const char* pharse);

extern "C" __declspec(dllexport) void AmelieUpdate(Amelie* object);

extern "C" __declspec(dllexport) const char* AmelieGetPathToProgram(Amelie* object, const char* programName);

extern "C" __declspec(dllexport) void AmelieAddProgram(Amelie* object, const char* program, const char* path);

extern "C" __declspec(dllexport) bool AmelieGetVoice(Amelie* object);

extern "C" __declspec(dllexport) void AmelieSetVoice(Amelie* object, bool value);

extern "C" __declspec(dllexport) const char* AmelieGetUserInput(Amelie* object);

extern "C" __declspec(dllexport) void AmelieDelete(Amelie* object);



extern "C" __declspec(dllexport) Settings* getInstance();

extern "C" __declspec(dllexport) void setLanguage(Settings* object, const char* langValue);

extern "C" __declspec(dllexport) void setUsername(Settings* object, const char* nameValue);

extern "C" __declspec(dllexport) const char* getLanguage(Settings* object);

extern "C" __declspec(dllexport) std::multimap<int, const char*> getSupportingLangs(Settings* object);

extern "C" __declspec(dllexport) const char* getUsername(Settings* object);

extern "C" __declspec(dllexport) std::multimap<const char*, void*> getMethodsToResolveErrors(Settings* object);

extern "C" __declspec(dllexport) void SettingsDelete(Settings* object);
