#define _AMD64_
#include <QMultiMap>
#include <vector>
#include <Libloaderapi.h>



typedef void*(*AmelieInstance)(const char* appLanguage);

typedef void*(*ChangeLanguage)(void* object, const char* language);

typedef char*(*Conversation)(void* object, bool enableVoice, const char* userInput);

typedef void(*Tts)(void* object, const char* prase);

typedef bool(*GetVoice)(void* object);

typedef const char*(*GetUserInput)(void* object);

typedef void(*Delete)(void* object);





typedef void*(*SettingsInstance)();

typedef void(*setLang)(void* object, const char* langValue);

typedef bool(*setUsername)(void* object, const char* nameValue);

typedef void(*setBotAvatar)(void* object, const char* avatarName);

typedef void(*setUserAvatar)(void* object, const char* avatarName);

typedef const char*(*getLang)(void* object);

typedef std::vector<const char*>(*getSupportingLangs)(void* object);

typedef const char*(*getUsername)(void* object);

typedef std::vector<const char*>(*getBotAvatars)(void* object);

typedef std::vector<const char*>(*getUserAvatars)(void* object);

typedef const char*(*getBotAvatar)(void* object);

typedef const char*(*getUserAvatar)(void* object);

typedef std::multimap<const char*, void*> (*getMethods)(void* object);






static AmelieInstance AmelieCreateInstance = (AmelieInstance)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieCreateInstance");
static ChangeLanguage AmelieChangeLanguage = (ChangeLanguage)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieChangeLanguage");
static Conversation AmelieConversation = (Conversation)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieConversation");
static Tts AmelieTTS = (Tts)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieTTS");
static GetVoice AmelieGetVoice = (GetVoice)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieGetVoice");
static GetUserInput AmelieGetUserInput = (GetUserInput)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieGetUserInput");
static Delete AmelieDelete = (Delete)GetProcAddress(LoadLibraryA("AmelieLibrary"), "AmelieDelete");





static SettingsInstance SettingsCreateInstance = (SettingsInstance)GetProcAddress(LoadLibraryA("AmelieLibrary"), "SettingsGetInstance");
static setLang SettingsSetLanguage = (setLang)GetProcAddress(LoadLibraryA("AmelieLibrary"), "setLanguage");
static getLang SettingsGetLanguage = (getLang)GetProcAddress(LoadLibraryA("AmelieLibrary"), "getLanguage");
static setUsername SettingsSetUsername = (setUsername)GetProcAddress(LoadLibraryA("AmelieLibrary"), "setUsername");
static setBotAvatar SettingsSetBotAvatar = (setBotAvatar)GetProcAddress(LoadLibraryA("AmelieLibrary"), "setBotAvatar");
static setUserAvatar SettingsSetUserAvatar = (setUserAvatar)GetProcAddress(LoadLibraryA("AmelieLibrary"), "setUserAvatar");
static getSupportingLangs SettingsGetSupportingLangs = (getSupportingLangs)GetProcAddress(LoadLibraryA("AmelieLibrary"), "?getSupportingLangs@@YA?AV?$vector@PEBDV?$allocator@PEBD@std@@@std@@PEAVSettings@main@library@@@Z");
static getUsername SettingsGetUsername = (getUsername)GetProcAddress(LoadLibraryA("AmelieLibrary"), "getUsername");
static getBotAvatars SettingsGetBotAvatars = (getBotAvatars)GetProcAddress(LoadLibraryA("AmelieLibrary"), "?getBotAvatars@@YA?AV?$vector@PEBDV?$allocator@PEBD@std@@@std@@PEAVSettings@main@library@@@Z");
static getUserAvatars SettingsGetUserAvatars = (getUserAvatars)GetProcAddress(LoadLibraryA("AmelieLibrary"), "?getUserAvatars@@YA?AV?$vector@PEBDV?$allocator@PEBD@std@@@std@@PEAVSettings@main@library@@@Z");
static getBotAvatar SettingsGetBotAvatar = (getBotAvatar)GetProcAddress(LoadLibraryA("AmelieLibrary"), "getBotAvatar");
static getUserAvatar SettingsGetUserAvatar = (getUserAvatar)GetProcAddress(LoadLibraryA("AmelieLibrary"), "getUserAvatar");
static getMethods SettingsGetMethodsToResolveErrors = (getMethods)GetProcAddress(LoadLibraryA("AmelieLibrary"), "?getMethodsToResolveErrors@@YA?AV?$multimap@PEBDPEAXU?$less@PEBD@std@@V?$allocator@U?$pair@QEBDPEAX@std@@@2@@std@@PEAVSettings@main@library@@@Z");
static Delete SettingsDelete = (Delete)GetProcAddress(LoadLibraryA("AmelieLibrary"), "SettingsDelete");




