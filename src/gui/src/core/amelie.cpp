#include "amelie.h"
#include <vector>
#include <QFileInfo>
#include <QResource>


#pragma region AmelieEvent
AmelieEvent::AmelieEvent()
{
    this->amelie = AmelieApplication::getInstance();
}



AmelieEvent* AmelieEvent::getInstance()
{
    static AmelieEvent* instance = new AmelieEvent();
    return instance;
}



QUrl AmelieEvent::initSettingsWindow()
{
    return amelie->initSettingsWindow();
}



QString AmelieEvent::chatConversation(bool enableVoice, QString input)
{
    return amelie->chatConversation(enableVoice, input);
}



bool AmelieEvent::setUsername(QString nameValue)
{
    return amelie->setUsername(nameValue);
}



QString AmelieEvent::getUsername()
{
    return amelie->getUsername();
}



void AmelieEvent::setLanguage(QString langValue)
{
    amelie->setLanguage(langValue);
}



QString AmelieEvent::getLanguage()
{
    return amelie->getLanguage();
}



std::vector<const char*> AmelieEvent::getSupportingLangs()
{
    return amelie->getSupportingLangs();
}



QString AmelieEvent::getUserInput()
{
    return amelie->getUserInput();
}



std::vector<const char*> AmelieEvent::getBotAvatars()
{
    return amelie->getBotAvatars();
}



std::vector<const char*> AmelieEvent::getUserAvatars()
{
    return amelie->getUserAvatars();
}



QString AmelieEvent::getBotAvatar()
{
    return amelie->getBotAvatar();
}



QString AmelieEvent::getUserAvatar()
{
    return amelie->getUserAvatar();
}



void AmelieEvent::setBotAvatar(QString avatarName)
{
    amelie->setBotAvatar(avatarName);
}



void AmelieEvent::setUserAvatar(QString avatarName)
{
    amelie->setUserAvatar(avatarName);
}



QString AmelieEvent::setPreviewAvatar(QString avatarType, QString avatarName)
{
    QFileInfo p("../resources/AppIcon/" + avatarType + "/avatar/" + avatarName + ".png");
    return QUrl::fromLocalFile(p.absoluteFilePath()).toString();
}



void AmelieEvent::closeAmelieEvent()
{
    delete amelie;
}


AmelieEvent::~AmelieEvent()
{
    delete amelie;
}

#pragma endregion





#pragma region AmelieApplication
AmelieApplication::AmelieApplication()
{
    this->settings = Settings::getInstance();

    this->chat = nullptr;
    this->gui = nullptr;
}



AmelieApplication* AmelieApplication::getInstance()
{
    static AmelieApplication* instance = new AmelieApplication();
    return instance;
}



void AmelieApplication::initChatBot()
{
    this->chat = Chat::getInstance(settings->getLanguage());
}



char* AmelieApplication::chatConversation(bool enableVoice, QString input)
{
    return chat->conversation(enableVoice, input.toStdString().c_str());
}



void AmelieApplication::setLanguage(QString langValue)
{
    settings->setLanguage(langValue);

    if(chat != nullptr)
        chat->changeLanguage(langValue.toStdString().c_str());
}



std::vector<const char*> AmelieApplication::getSupportingLangs()
{
    return settings->getSupportingLangs();
}



QString AmelieApplication::getLanguage()
{
    return settings->getLanguage();
}



bool AmelieApplication::setUsername(QString nameValue)
{
    return settings->setUsername(nameValue);
}



QString AmelieApplication::getUsername()
{
    return settings->getUsername();
}



QString AmelieApplication::getUserInput()
{
    return chat->getUserInput();
}



std::vector<const char*> AmelieApplication::getBotAvatars()
{
    return settings->getBotAvatars();
}



std::vector<const char*> AmelieApplication::getUserAvatars()
{
    return settings->getUserAvatars();
}



void AmelieApplication::setBotAvatar(QString avatarName)
{
    settings->setBotAvatar(avatarName);
}



void AmelieApplication::setUserAvatar(QString avatarName)
{
    settings->setUserAvatar(avatarName);
}



QString AmelieApplication::getBotAvatar()
{
    return settings->getBotAvatar();
}



QString AmelieApplication::getUserAvatar()
{
    return settings->getUserAvatar();
}



int AmelieApplication::main(int argc, char** argv)
{
    this->gui = new GUI(argc, argv);

    // Filling the settings file
    while(settings->getLanguage() == "-" || settings->getUsername() == "")
    {
        gui->showSettingsWindow();
    }


    initChatBot();


    return gui->showMainWindow();
}



QUrl AmelieApplication::initSettingsWindow()
{
    return this->gui->initSettingsWindow();
}


AmelieApplication::~AmelieApplication()
{
    // this->gui will be deleted automatically when QML window triggers close event.
    delete chat;
    delete settings;
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



char* AmelieApplication::Chat::conversation(bool enableVoice, const char* userInput)
{   
    return AmelieConversation(classInstance, enableVoice, userInput);
}



void AmelieApplication::Chat::tts(const char* phrase)
{
    AmelieTTS(classInstance, phrase);
}



bool AmelieApplication::Chat::getVoice()
{
    return AmelieGetVoice(classInstance);
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





#pragma region Settings
AmelieApplication::Settings::Settings()
{
    this->classInstance = SettingsCreateInstance();
}


AmelieApplication::Settings* AmelieApplication::Settings::getInstance()
{
    static Settings* instance = new Settings();
    return instance;
}



void AmelieApplication::Settings::setLanguage(QString langValue)
{
    SettingsSetLanguage(classInstance, langValue.toStdString().c_str());
}



bool AmelieApplication::Settings::setUsername(QString nameValue)
{
    return SettingsSetUsername(classInstance, nameValue.toStdString().c_str());
}



const char* AmelieApplication::Settings::getLanguage()
{
    return SettingsGetLanguage(classInstance);
}



std::vector<const char*> AmelieApplication::Settings::getSupportingLangs()
{
    return SettingsGetSupportingLangs(classInstance);
}



QString AmelieApplication::Settings::getUsername()
{
    return SettingsGetUsername(classInstance);
}



void AmelieApplication::Settings::setBotAvatar(QString avatarName)
{
    SettingsSetBotAvatar(classInstance, avatarName.toStdString().c_str());
}



void AmelieApplication::Settings::setUserAvatar(QString avatarName)
{
    SettingsSetUserAvatar(classInstance, avatarName.toStdString().c_str());
}



std::vector<const char*> AmelieApplication::Settings::getBotAvatars()
{
    return SettingsGetBotAvatars(classInstance);
}



std::vector<const char*> AmelieApplication::Settings::getUserAvatars()
{
    return SettingsGetUserAvatars(classInstance);
}


const char* AmelieApplication::Settings::getBotAvatar()
{
    return SettingsGetBotAvatar(classInstance);
}



const char* AmelieApplication::Settings::getUserAvatar()
{
    return SettingsGetUserAvatar(classInstance);
}




std::multimap<const char*, void*> AmelieApplication::Settings::getMethodsToResolveErrors()
{
    return SettingsGetMethodsToResolveErrors(classInstance);
}



AmelieApplication::Settings::~Settings()
{
    SettingsDelete(classInstance);
}
#pragma endregion





#pragma region GUI
AmelieApplication::GUI::GUI(int argc, char** argv)
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    this->app = new QGuiApplication(argc, argv);
    this->engine = new QQmlApplicationEngine();
}



int AmelieApplication::GUI::showMainWindow()
{
    engine->rootContext()->setContextProperty("Event", AmelieEvent::getInstance());



    /* This is a crutch to fix a crash of the application.
     * aftter the call of engine->load it's raising an unhanlded excpetion in ucrtbase module.
     *
     * The stack trace:
     * > 	ucrtbase.dll!00007ffd1d0bdb8e() -> raise the 0xC0000409 exception.
     * > 	ucrtbase.dll!00007ffd1d0bd2cf()
     * >	AmelieBot.exe!__scrt_unhandled_exception_filter(_EXCEPTION_POINTERS * const pointers) in crt -> utility_app.cpp line 91
     */
    while(true)
    {
        try
        {
            engine->load("qrc:///qml/main.qml");
            break;
        }
        catch(...)
        {
            continue;
        }
    }

    return app->exec();
}


QUrl AmelieApplication::GUI::initSettingsWindow()
{
    // TODO: Refactoring.
    AmelieEvent* event = AmelieEvent::getInstance();
    engine->rootContext()->setContextProperty("Event", event);

    std::vector<const char*> langs = event->getSupportingLangs();
    QVariantList supLangs;

    QString currentLang = event->getLanguage();
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



    std::vector<const char*> botAvatars = event->getBotAvatars();
    QVariantList botAvatarList;


    QString currentBotAvatarName = event->getBotAvatar();
    auto currentBotAvatarPosition = std::find(botAvatars.begin(), botAvatars.end(), currentBotAvatarName);
    if(currentBotAvatarPosition != botAvatars.end())
    {
        botAvatars.erase(currentBotAvatarPosition);
        botAvatarList.append(currentBotAvatarName);
    }

    for(int i = 0; i < botAvatars.size(); ++i)
    {
        botAvatarList.append(botAvatars[i]);
    }
    engine->rootContext()->setContextProperty("botAvatarList", botAvatarList);



    std::vector<const char*> userAvatars = event->getUserAvatars();
    QVariantList userAvatarList;

    QString currentUserAvatarName = event->getUserAvatar();
    auto currentUserAvatarPosition = std::find(userAvatars.begin(), userAvatars.end(), currentUserAvatarName);
    if(currentUserAvatarPosition != userAvatars.end())
    {

        userAvatars.erase(currentUserAvatarPosition);
        userAvatarList.append(currentUserAvatarName);
    }


    for(int i = 0; i < userAvatars.size(); ++i)
    {
        userAvatarList.append(userAvatars[i]);
    }
    engine->rootContext()->setContextProperty("userAvatarList", userAvatarList);

    return QUrl("qrc:///qml/settingsWindow.qml");
}


void AmelieApplication::GUI::showSettingsWindow()
{

    engine->load(initSettingsWindow());
    app->exec();
}


AmelieApplication::GUI::~GUI()
{
    delete engine;
    delete app;
}
#pragma endregion




