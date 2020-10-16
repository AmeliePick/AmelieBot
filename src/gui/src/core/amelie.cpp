#include "dllimport.inl"



#pragma region AmelieApplication
AmelieApplication::AmelieApplication()
{
    this->fileManager = FileManager::getInstance();
    this->network = Network::getInstance();

    this->settings = Settings::getInstance();
}



void AmelieApplication::initChatBot()
{
    this->chat = Chat::getInstance(settings->getLanguage());
    this->dialog = Dialog::getInstance(settings->getLanguage());
}

void AmelieApplication::changeInputMode(bool enableVoice)
{

}



int AmelieApplication::main(int argc, char** argv)
{
    GUI gui(argc, argv);

    /* Filling the settings file
    while(settings->getLanguage() == "-" || settings->getUsername() == "")
    {
        gui.showSettingsWindow(settings);
    }

    initChatBot();*/
    return gui.showSettingsWindow(settings);
}

#pragma endregion







#pragma region Chat
AmelieApplication::Chat::Chat(const char* appLanguage)
{
    this->classInstance = AmelieCreateInstance(appLanguage);
}



AmelieApplication::Chat* AmelieApplication::Chat::getInstance(const char* appLanguage)
{
    static Chat* instance = new Chat(appLanguage);
    return instance;
}



void AmelieApplication::Chat::changeLanguage(const char* language)
{
    AmelieChangeLanguage(classInstance, language);
}



char* AmelieApplication::Chat::conversation(const char* userInput)
{
    return AmelieConversation(classInstance, userInput);
}



void AmelieApplication::Chat::tts(const char* phrase)
{
    AmelieTTS(classInstance, phrase);
}



void AmelieApplication::Chat::update()
{
    AmelieUpdate(classInstance);
}



const char* AmelieApplication::Chat::getPathToProgram(const char* programName)
{
    return AmelieGetPathToProgram(classInstance, programName);
}



void AmelieApplication::Chat::addProgram(const char* program, const char* path)
{
    AmelieAddProgram(classInstance, program, path);
}



bool AmelieApplication::Chat::getVoice()
{
    return AmelieGetVoice(classInstance);
}



void AmelieApplication::Chat::setVoice(bool value)
{
    AmelieSetVoice(classInstance,value);
}



const char* AmelieApplication::Chat::getUserInput()
{
   return AmelieGetUserInput(classInstance);
}



AmelieApplication::Chat::~Chat()
{
    AmelieDelete(classInstance);
}
#pragma endregion





#pragma region FileManager
AmelieApplication::FileManager* AmelieApplication::FileManager::getInstance()
{
    return nullptr;
}



bool AmelieApplication::FileManager::fileExist(const char* file)
{
    return false;
}



void AmelieApplication::FileManager::writeToFile(const char* value, const char* file, const char* mode, const char* _encoding)
{

}



const char * AmelieApplication::FileManager::readFile(const char* file, const char* _encoding)
{
    return nullptr;
}

void AmelieApplication::FileManager::createFile(const char* file)
{

}



void AmelieApplication::FileManager::deleteFile(const char* file)
{

}



void AmelieApplication::FileManager::clearFile(const char* file)
{

}



AmelieApplication::FileManager::~FileManager()
{

}
#pragma endregion





#pragma region Settings
AmelieApplication::Settings* AmelieApplication::Settings::getInstance()
{
    return nullptr;
}



void AmelieApplication::Settings::setLanguage(const char* langValue)
{

}



void AmelieApplication::Settings::setUsername(const char* nameValue)
{

}



const char* AmelieApplication::Settings::getLanguage()
{
    return nullptr;
}



std::multimap<int, const char*> AmelieApplication::Settings::getSupportingLangs()
{
    return std::multimap<int, const char*>();
}



const char* AmelieApplication::Settings::getUsername()
{
    return nullptr;
}



std::multimap<const char*, void*> AmelieApplication::Settings::getMethodsToResolveErrors()
{
    return std::multimap<const char*, void*>();
}
#pragma endregion





#pragma region Network
AmelieApplication::Network* AmelieApplication::Network::getInstance()
{
    return nullptr;
}



bool AmelieApplication::Network::checkNetworkConnection()
{
    return false;
}
#pragma endregion





#pragma region Logger
AmelieApplication::Logger* AmelieApplication::Logger::getInstance()
{
    return nullptr;
}



void AmelieApplication::Logger::addRecord(const char* recordTitle, const char* value)
{

}



void AmelieApplication::Logger::logWrite()
{

}
#pragma endregion





#pragma region Dialog
AmelieApplication::Dialog* AmelieApplication::Dialog::getInstance(const char* appLanguage)
{
    return nullptr;
}


const char* AmelieApplication::Dialog::getMessageFor(const char* expression)
{
    return nullptr;
}


void AmelieApplication::Dialog::changeLanguage(const char* appLanguage)
{

}
#pragma endregion
