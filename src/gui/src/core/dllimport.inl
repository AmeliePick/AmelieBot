#define _AMD64_
#include "amelie.h"
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
