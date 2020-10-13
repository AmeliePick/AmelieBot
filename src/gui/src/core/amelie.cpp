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



Amelie::Amelie(const char* appLanguage)
{
    this->classInstance = AmelieCreateInstance(appLanguage);
}



Amelie* Amelie::getInstance(const char* appLanguage)
{
    static Amelie* instance = new Amelie(appLanguage);
    return instance;
}



void Amelie::changeLanguage(const char* language)
{
    AmelieChangeLanguage(classInstance, language);
}



char* Amelie::conversation(const char* userInput)
{
    return AmelieConversation(classInstance, userInput);
}



void Amelie::tts(const char* phrase)
{
    AmelieTTS(classInstance, phrase);
}



void Amelie::update()
{
    AmelieUpdate(classInstance);
}



const char* Amelie::getPathToProgram(const char* programName)
{
    return AmelieGetPathToProgram(classInstance, programName);
}



void Amelie::addProgram(const char* program, const char* path)
{
    AmelieAddProgram(classInstance, program, path);
}



bool Amelie::getVoice()
{
    return AmelieGetVoice(classInstance);
}



void Amelie::setVoice(bool value)
{
    AmelieSetVoice(classInstance,value);
}



const char* Amelie::getUserInput()
{
   return AmelieGetUserInput(classInstance);
}



Amelie::~Amelie()
{
    AmelieDelete(classInstance);
}
