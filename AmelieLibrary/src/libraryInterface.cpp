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



__declspec(dllexport) char* AmelieConversation(Amelie* object, const char* userInput)
{
    return object->conversation(userInput);
}



__declspec(dllexport) void AmelieTTS(Amelie* object, const char* pharse)
{
    object->tts(pharse);
}



__declspec(dllexport) void AmelieUpdate(Amelie* object)
{
    object->update();
}



__declspec(dllexport) const char* AmelieGetPathToProgram(Amelie* object, const char* programName)
{
    return object->getPathToProgram(programName);
}



__declspec(dllexport) void AmelieAddProgram(Amelie* object, const char* program, const char* path)
{
    object->addProgram(program, path);
}



__declspec(dllexport) bool AmelieGetVoice(Amelie* object)
{
    return object->getVoice();
}



__declspec(dllexport) void AmelieSetVoice(Amelie* object, bool value)
{
    object->setVoice(value);
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



__declspec(dllexport) void setUsername(Settings* object, const char* nameValue)
{
    object->setUsername(nameValue);
}



__declspec(dllexport) const char* getLanguage(Settings* object)
{
    return object->getLanguage();
}



__declspec(dllexport) std::vector<const char*> getSupportingLangs(Settings* object)
{
    return object->getSupportingLangs();
}



__declspec(dllexport) const char * getUsername(Settings* object)
{
    return object->getUsername();
}



__declspec(dllexport) std::multimap<const char*, void*> getMethodsToResolveErrors(Settings* object)
{
    return object->getMethodsToResolveErrors();
}



__declspec(dllexport) void SettingsDelete(Settings* object)
{
    delete object;
}





__declspec(dllexport) FileManager* FileManagerGetInstance()
{
    return FileManager::getInstance();
}



__declspec(dllexport) bool fileExist(FileManager* object, const char* file)
{
    return object->fileExist(file);
}



__declspec(dllexport) void writeToFile(FileManager* object, const char* value, const char* file, const char* mode, const char* _encoding)
{
    object->writeToFile(value, file, mode, _encoding);
}



__declspec(dllexport) const char* readFile(FileManager* object, const char* file, const char* _encoding)
{
    return object->readFile(file, _encoding);
}



__declspec(dllexport) void createFile(FileManager* object, const char* file)
{
    object->createFile(file);
}



__declspec(dllexport) void deleteFile(FileManager* object, const char* file)
{
    object->deleteFile(file);
}



__declspec(dllexport) void clearFile(FileManager* object, const char* file)
{
    object->clearFile(file);
}



__declspec(dllexport) void FileManagerDelete(FileManager* object)
{
    delete object;
}





__declspec(dllexport) Network* NetworkGetInstance()
{
    return Network::getInstance();
}



__declspec(dllexport) bool checkNetworkConnection(Network* object)
{
    return object->checkNetworkConnection();
}





__declspec(dllexport) Logger* LoggerGetInstance()
{
    return Logger::getInstance();
}



__declspec(dllexport) void addRecord(Logger* object, const char* recordTitle, const char* value)
{
    object->addRecord(recordTitle, value);
}



__declspec(dllexport) void logWrite(Logger* object)
{
    object->logWrite();
}





__declspec(dllexport) Dialog* DialogGetInstance(Dialog* object, const char* appLanguage)
{
    return object->getInstance(appLanguage);
}



__declspec(dllexport) const char* getMessageFor(Dialog* object, const char* expression)
{
    return object->getMessageFor(expression);
}



__declspec(dllexport) void changeLanguage(Dialog* object, const char* appLanguage)
{
    object->changeLanguage(appLanguage);
}
