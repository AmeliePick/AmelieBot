#pragma once
#include "library.h"

#define Amelie library::main::Amelie
#define Settings library::main::Settings
#define FileManager library::tools::system::FileManager
#define Network library::tools::system::Network
#define Logger library::tools::logger::Logger
#define Dialog library::chat::dialog::Dialog



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



extern "C" __declspec(dllexport) Settings* SettingsGetInstance();

extern "C" __declspec(dllexport) void setLanguage(Settings* object, const char* langValue);

extern "C" __declspec(dllexport) void setUsername(Settings* object, const char* nameValue);

extern "C" __declspec(dllexport) const char* getLanguage();

extern "C++" __declspec(dllexport) std::multimap<int, const char*> getSupportingLangs(Settings* object);

extern "C" __declspec(dllexport) const char* getUsername(Settings* object);

extern "C++" __declspec(dllexport) std::multimap<const char*, void*> getMethodsToResolveErrors(Settings* object);

extern "C" __declspec(dllexport) void SettingsDelete(Settings* object);



extern "C" __declspec(dllexport) FileManager* FileManagerGetInstance();

extern "C" __declspec(dllexport) bool fileExist(FileManager* object, const char* file);

extern "C" __declspec(dllexport) void writeToFile(FileManager* object, const char* value, const char* file, const char* mode = "a", const char* _encoding = "utf-8");

extern "C" __declspec(dllexport) const char* readFile(FileManager* object, const char* file, const char* _encoding = "utf-8");

extern "C" __declspec(dllexport) void createFile(FileManager* object, const char* file);

extern "C" __declspec(dllexport) void deleteFile(FileManager* object, const char* file);

extern "C" __declspec(dllexport) void clearFile(FileManager* object, const char* file);

extern "C" __declspec(dllexport) void FileManagerDelete(FileManager* object);



extern "C" __declspec(dllexport) Network* NetworkGetInstance();

extern "C" __declspec(dllexport) bool checkNetworkConnection(Network* object);



extern "C" __declspec(dllexport) Logger* LoggerGetInstance();

extern "C" __declspec(dllexport) void addRecord(Logger* object, const char* recordTitle, const char* value);

extern "C" __declspec(dllexport) void logWrite(Logger* object);



extern "C" __declspec(dllexport) Dialog* DialogGetInstance(Dialog* object, const char* appLanguage);

extern "C" __declspec(dllexport) const char* getMessageFor(Dialog* object, const char* expression);

extern "C" __declspec(dllexport) void changeLanguage(Dialog* object, const char* appLanguage);
