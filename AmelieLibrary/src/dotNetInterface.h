#pragma once
#include "library.h"

#define Amelie library::main::Amelie


__declspec(dllexport) void* AmelieCreateInstance(const char* appLanguage);


__declspec(dllexport) void AmelieChangeLanguage(Amelie* object, const char* language);

__declspec(dllexport) const char* AmelieConversation(Amelie* object, const char* userInput);

__declspec(dllexport) void AmelieTTS(Amelie* object, const char* pharse);

__declspec(dllexport) void AmelieUpdate(Amelie* object);

__declspec(dllexport) const char* AmelieGetPathToProgram(Amelie* object, const char* programName);

__declspec(dllexport) void AmelieAddProgram(Amelie* object, const char* program, const char* path);

__declspec(dllexport) bool AmelieGetVoice(Amelie* object);

__declspec(dllexport) void AmelieSetVoice(Amelie* object, bool value);

__declspec(dllexport) const char* AmelieGetUserInput(Amelie* object);
