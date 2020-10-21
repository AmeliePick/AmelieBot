#include "amelie.h"
#include <vector>
#include <iostream>
#include <QDebug>



#pragma region AmelieApplication
AmelieApplication::AmelieApplication()
{
    this->fileManager = FileManager::getInstance();
    this->network = Network::getInstance();

    this->settings = Settings::getInstance();
}



AmelieApplication* AmelieApplication::getInstance()
{
    static AmelieApplication* instance = new AmelieApplication();
    return instance;
}



void AmelieApplication::initChatBot()
{
    this->chat = Chat::getInstance(settings->getLanguage());
    this->dialog = Dialog::getInstance(settings->getLanguage());
}



void AmelieApplication::changeInputMode(bool enableVoice)
{

}



QString AmelieApplication::chatConversation(QString input)
{
    return chat->conversation(input.toStdString().c_str());
}



void AmelieApplication::setVoice(bool enableVoice)
{
    chat->setVoice(enableVoice);
}



int AmelieApplication::main(int argc, char** argv)
{
    this->gui = new GUI(argc, argv);

    // Filling the settings file
    while(settings->getLanguage() == "-" || settings->getUsername() == "")
    {
        gui->showSettingsWindow(settings);
    }

    initChatBot();

    return gui->showMainWindow(chat, dialog);
}



void AmelieApplication::showSettingsWindow()
{
    this->gui->showSettingsWindow(settings);
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
AmelieApplication::FileManager::FileManager()
{
    this->classInstance = FileManagerCreateInstance();
}



AmelieApplication::FileManager* AmelieApplication::FileManager::getInstance()
{
    static FileManager* instance = new FileManager();
    return instance;
}



bool AmelieApplication::FileManager::fileExist(const char* file)
{
    return FMfileExist(classInstance, file);
}



void AmelieApplication::FileManager::writeToFile(const char* value, const char* file, const char* mode, const char* _encoding)
{
    FMWriteToFile(classInstance, value, file, mode, _encoding);
}



const char* AmelieApplication::FileManager::readFile(const char* file, const char* _encoding)
{
    return FMreadFile(classInstance, file, _encoding);
}



void AmelieApplication::FileManager::createFile(const char* file)
{
    FMcreateFile(classInstance, file);
}



void AmelieApplication::FileManager::deleteFile(const char* file)
{
    FMdeleteFile(classInstance, file);
}



void AmelieApplication::FileManager::clearFile(const char* file)
{
    FMclearFile(classInstance, file);
}



AmelieApplication::FileManager::~FileManager()
{
    FileManagerDelete(classInstance);
}
#pragma endregion





#pragma region Settings
Settings::Settings()
{
    this->classInstance = SettingsCreateInstance();
}


Settings* Settings::getInstance()
{
    static Settings* instance = new Settings();
    return instance;
}



void Settings::setLanguage(QString langValue)
{
    SettingsSetLanguage(classInstance, langValue.toStdString().c_str());
}



void Settings::setUsername(QString nameValue)
{
    SettingsSetUsername(classInstance, nameValue.toStdString().c_str());
}



const char* Settings::getLanguage()
{
    return SettingsGetLanguage(classInstance);
}



std::vector<const char*> Settings::getSupportingLangs()
{
    return SettingsGetSupportingLangs(classInstance);
}



QString Settings::getUsername()
{
    return SettingsGetUsername(classInstance);
}



std::multimap<const char*, void*> Settings::getMethodsToResolveErrors()
{
    return SettingsGetMethodsToResolveErrors(classInstance);
}
#pragma endregion





#pragma region Network
AmelieApplication::Network::Network()
{
    this->classInstance = NetworkCreateInstance();
}



AmelieApplication::Network* AmelieApplication::Network::getInstance()
{
    Network* instance = new Network();
    return instance;
}



bool AmelieApplication::Network::checkNetworkConnection()
{
    return NetworkCheckNetworkConnection(classInstance);
}
#pragma endregion





#pragma region Logger
AmelieApplication::Logger::Logger()
{
    this->classInstance = LoggerCreateInstance();
}



AmelieApplication::Logger* AmelieApplication::Logger::getInstance()
{
    static Logger* instance = new Logger();
    return instance;
}



void AmelieApplication::Logger::addRecord(const char* recordTitle, const char* value)
{
    LoggerAddRecord(classInstance, recordTitle, value);
}



void AmelieApplication::Logger::logWrite()
{
    LoggerLogWrite(classInstance);
}
#pragma endregion





#pragma region Dialog
AmelieApplication::Dialog::Dialog(const char* applanguage)
{
    this->classInstance = nullptr;//DialogCreateInstance(applanguage);
    qInfo() << "Reached";

}



AmelieApplication::Dialog* AmelieApplication::Dialog::getInstance(const char* appLanguage)
{
    static Dialog* instance = new Dialog(appLanguage);
    return instance;
}



const char* AmelieApplication::Dialog::getMessageFor(const char* expression)
{
    return DialogGetMessageFor(classInstance, expression);
}



void AmelieApplication::Dialog::changeLanguage(const char* appLanguage)
{
    DialogChangeLanguage(classInstance, appLanguage);
}





AmelieApplication::GUI::GUI(int argc, char** argv)
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    this->app = new QGuiApplication(argc, argv);
    this->engine = new QQmlApplicationEngine();

    app->setWindowIcon(QIcon("../../../resources/AppIcon/icon.ico"));
}



int AmelieApplication::GUI::showMainWindow(Chat* chat, Dialog* dialog)
{
    AmelieEvent notify;
    engine->rootContext()->setContextProperty("Event", &notify);
    engine->rootContext()->setContextProperty("Chat", (QObject*)chat);
    engine->rootContext()->setContextProperty("Dialog", (QObject*)dialog);
    engine->load(QUrl::fromLocalFile("../src/view/main.qml"));

    return app->exec();
}



int AmelieApplication::GUI::showSettingsWindow(Settings* settings)
{
    engine->rootContext()->setContextProperty("Settings", settings);

    std::vector<const char*> langs = settings->getSupportingLangs();
    QVariantList supLangs;

    QString currentLang = settings->getLanguage();
    // If value is actually language value
    if(currentLang != '-')
    {
        auto currentLangValue = std::find(langs.begin(), langs.end(), currentLang);
        if(currentLangValue != langs.end())
        {

            langs.erase(currentLangValue);
            supLangs.append(currentLang);
        }
    }

    for(int i = 0; i < langs.size(); ++i)
    {
        supLangs.append(langs[i]);
    }


    engine->rootContext()->setContextProperty("Langs", supLangs);
    engine->load(QUrl::fromLocalFile("../src/view/settingsWindow.qml"));

    return app->exec();
}
#pragma endregion



#pragma region AmelieEvent
AmelieEvent::AmelieEvent()
{
    this->amelie = AmelieApplication::getInstance();
}



void AmelieEvent::showSettingsWindow()
{
    amelie->showSettingsWindow();
}



QString AmelieEvent::chatConversation(QString input)
{
    return amelie->chatConversation(input);
}



void AmelieEvent::setVoice(bool enableVoice)
{
    amelie->setVoice(enableVoice);
}
#pragma endregion


