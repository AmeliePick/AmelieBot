#define _AMD64_
#include <QMultiMap>
#include <vector>
#include <Libloaderapi.h>



typedef void*(*AmelieInstance)(const char* appLanguage);

typedef void*(*ChangeLanguage)(void* object, const char* language);

typedef char*(*Conversation)(void* object, const char* userInput);

typedef void(*Tts)(void* object, const char* prase);

typedef void(*Update)(void* object);

typedef const char*(*GetPathToProgram)(void* object, const char* programName);

typedef void(*AddProgram)(void* object, const char* program, const char* path);

typedef bool(*GetVoice)(void* object);

typedef void(*SetVoice)(void* object, bool value);

typedef const char*(*GetUserInput)(void* object);

typedef void(*Delete)(void* object);





typedef void*(*SettingsInstance)();

typedef void(*setLang)(void* object, const char* langValue);

typedef bool(*setUsername)(void* object, const char* nameValue);

typedef const char*(*getLang)(void* object);

typedef std::vector<const char*>(*getSupportingLangs)(void* object);

typedef const char*(*getUsername)(void* object);

typedef std::multimap<const char*, void*> (*getMethods)(void* object);





typedef void*(*FileManagerInstance)();

typedef bool(*fileExist)(void* object, const char* file);

typedef void (*writeToFile)(void* object, const char* value, const char* file, const char* mode, const char* _encoding);

typedef const char*(*readFile)(void* object, const char* file, const char* _encoding);

typedef void (*createFile)(void* object, const char* file);

typedef void (*deleteFile)(void* object, const char* file);

typedef void (*clearFile)(void* object, const char* file);





typedef void* (*NetworkInstance)();

typedef bool (*checkNetworkConnection)(void* object);





typedef void* (*LoggerInstance)();

typedef void (*addRecord)(void* object, const char* recordTitle, const char* value);

typedef void (*logWrite)(void* object);



typedef const char* (*vcInput)();





static AmelieInstance AmelieCreateInstance = (AmelieInstance)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieCreateInstance");
static ChangeLanguage AmelieChangeLanguage = (ChangeLanguage)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieChangeLanguage");
static Conversation AmelieConversation = (Conversation)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieConversation");
static Tts AmelieTTS = (Tts)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieTTS");
static Update AmelieUpdate = (Update)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieUpdate");
static GetPathToProgram AmelieGetPathToProgram = (GetPathToProgram)GetProcAddress(LoadLibraryA("AmelieLibrary"), "GetPathToProgram");
static AddProgram AmelieAddProgram = (AddProgram)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieAddProgram");
static GetVoice AmelieGetVoice = (GetVoice)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieGetVoice");
static SetVoice AmelieSetVoice = (SetVoice)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieSetVoice");
static GetUserInput AmelieGetUserInput = (GetUserInput)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieGetUserInput");
static Delete AmelieDelete = (Delete)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieDelete");





static SettingsInstance SettingsCreateInstance = (SettingsInstance)GetProcAddress(LoadLibraryA("AmelieLibrary"), "SettingsGetInstance");
static setLang SettingsSetLanguage = (setLang)GetProcAddress(LoadLibraryA("AmelieLibrary"), "setLanguage");
static getLang SettingsGetLanguage = (getLang)GetProcAddress(LoadLibraryA("AmelieLibrary"), "getLanguage");
static setUsername SettingsSetUsername = (setUsername)GetProcAddress(LoadLibraryA("AmelieLibrary"), "setUsername");
static getSupportingLangs SettingsGetSupportingLangs = (getSupportingLangs)GetProcAddress(LoadLibraryA("AmelieLibrary"), "?getSupportingLangs@@YA?AV?$vector@PEBDV?$allocator@PEBD@std@@@std@@PEAVSettings@main@library@@@Z");
static getUsername SettingsGetUsername = (getUsername)GetProcAddress(LoadLibraryA("AmelieLibrary"), "getUsername");
static getMethods SettingsGetMethodsToResolveErrors = (getMethods)GetProcAddress(LoadLibraryA("AmelieLibrary"), "?getMethodsToResolveErrors@@YA?AV?$multimap@PEBDPEAXU?$less@PEBD@std@@V?$allocator@U?$pair@QEBDPEAX@std@@@2@@std@@PEAVSettings@main@library@@@Z");
static Delete SettingsDelete = (Delete)GetProcAddress(LoadLibraryA("AmelieLibrary"), "SettingsDelete");





static FileManagerInstance FileManagerCreateInstance = (FileManagerInstance)GetProcAddress(LoadLibraryA("AmelieLibrary"), "SettingsGetInstance");
static fileExist FMfileExist = (fileExist)GetProcAddress(LoadLibraryA("AmelieLibrary"), "fileExist");
static writeToFile FMWriteToFile = (writeToFile)GetProcAddress(LoadLibraryA("AmelieLibrary"), "writeToFile");
static readFile FMreadFile = (readFile)GetProcAddress(LoadLibraryA("AmelieLibrary"), "readFile");
static createFile FMcreateFile = (createFile)GetProcAddress(LoadLibraryA("AmelieLibrary"), "createFile");
static deleteFile FMdeleteFile = (deleteFile)GetProcAddress(LoadLibraryA("AmelieLibrary"), "deleteFile");
static clearFile FMclearFile = (clearFile)GetProcAddress(LoadLibraryA("AmelieLibrary"), "clearFile");
static Delete FileManagerDelete = (Delete)GetProcAddress(LoadLibraryA("AmelieLibrary"), "FileManagerDelete");





static NetworkInstance NetworkCreateInstance = (NetworkInstance)GetProcAddress(LoadLibraryA("AmelieLibrary"), "NetworkGetInstance");
static checkNetworkConnection NetworkCheckNetworkConnection = (checkNetworkConnection)GetProcAddress(LoadLibraryA("AmelieLibrary"), "checkNetworkConnection");





static LoggerInstance LoggerCreateInstance = (LoggerInstance)GetProcAddress(LoadLibraryA("AmelieLibrary"), "LoggerGetInstance");
static addRecord LoggerAddRecord = (addRecord)GetProcAddress(LoadLibraryA("AmelieLibrary"), "addRecord");
static logWrite LoggerLogWrite = (logWrite)GetProcAddress(LoadLibraryA("AmelieLibrary"), "logWrite");





static vcInput voiceInput = (vcInput)GetProcAddress(LoadLibraryA("AmelieLibrary"), "voiceInput");




