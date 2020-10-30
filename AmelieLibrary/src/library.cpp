#include "library.h"
#include <iostream>

// PROCESSING MODULE

void library::audio::processing::playAudio(const char* soundFile)
{
    static Function pyFunc("audio.processing", "playAudio");
    
    Function::Arguments args(soundFile);
    pyFunc.call(args);
}



library::audio::processing::TextToSpeech::TextToSpeech() : Class("audio.processing", "TextToSpeech", Function::Arguments())
{

}



library::audio::processing::TextToSpeech* library::audio::processing::TextToSpeech::getInstance()
{
    static TextToSpeech* instance = new TextToSpeech();
    return instance;
}



void library::audio::processing::TextToSpeech::operator()(const char* textSource, const char* srcLang)
{
    Function::Arguments args(textSource, srcLang);
    this->callMethod("__call__", args);
}



// RECOGNITION MODULE

library::audio::recognition::SpeechRecognition::SpeechRecognition(const char* appLanguage) : Class("audio.recognition", "SpeechRecognition", Function::Arguments(appLanguage))
{

}



library::audio::recognition::SpeechRecognition* library::audio::recognition::SpeechRecognition::getInstance(const char* appLanguage)
{
    static SpeechRecognition* instance = new SpeechRecognition(appLanguage);
    return instance;
}



void library::audio::recognition::SpeechRecognition::calibration()
{
    Function::Arguments arg;
    this->callMethod("calibration", arg);
}



void library::audio::recognition::SpeechRecognition::recognize()
{
    Function::Arguments arg;
    this->callMethod("recognize", arg);
}



// CHAT MODULE

library::chat::AICore::Chat::Chat(const char* appLanguage) : Class("chat.AICore", "Chat", Function::Arguments(appLanguage))
{

}



library::chat::AICore::Chat* library::chat::AICore::Chat::getInstance(const char* appLanguage)
{
    static Chat* instance = new Chat(appLanguage);
    return instance;
}



const char* library::chat::AICore::Chat::getInput()
{
    Function::Arguments arg;
    return callMethod("getInput", arg).ToString();
}



const char* library::chat::AICore::Chat::getInputType()
{
    Function::Arguments arg;
    return callMethod("getInputType", arg).ToString();
}



std::multimap<const char*, const char*> library::chat::AICore::Chat::getSessionInput()
{
    Function::Arguments arg;
    return callMethod("getSessionInput", arg).ToMultimap<const char*, const char*>();
}



const char* library::chat::AICore::Chat::getLanguage()
{
    Function::Arguments arg;
    return callMethod("getLanguage", arg).ToString();
}



const char* library::chat::AICore::Chat::launch(const char* input_)
{
    Function::Arguments arg(input_);
    return callMethod("launch", arg).ToString();
}



void library::chat::AICore::Chat::changeLanguage(const char* language)
{
    Function::Arguments arg(language);
    callMethod("changeLanguage", arg);
}



void library::chat::AICore::Chat::stemming(const char* expression)
{
    Function::Arguments arg(expression);
    callMethod("stemming", arg);
}



void library::chat::AICore::Chat::editInput(int meaningLength)
{
    Function::Arguments arg(meaningLength);
    callMethod("editInput", arg);
}



// DIALOG MODULE

library::chat::dialog::Dialog::Dialog(const char* applanguage) : Class("chat.module", "Dialog", Function::Arguments(applanguage))
{

}



library::chat::dialog::Dialog* library::chat::dialog::Dialog::getInstance(const char* appLanguage)
{
    static Dialog* instance = new Dialog(appLanguage);
    return instance;
}



const char* library::chat::dialog::Dialog::getMessageFor(const char* expression)
{
    Function::Arguments arg(expression);
    return callMethod("getMessageFor", arg).ToString();
}



void library::chat::dialog::Dialog::changeLanguage(const char* appLanguage)
{
    Function::Arguments arg(appLanguage);
    callMethod("changeLanguage", arg);
}



// INIPARSER MODULE

library::tools::iniParser::IniParser::IniParser(const char* fileToParsePath) : Class("tools.iniParser", "IniParser", Function::Arguments(fileToParsePath))
{

}



void library::tools::iniParser::IniParser::setSection(const char* section)
{
    Function::Arguments arg(section);
    callMethod("setSection", arg);
}



const char* library::tools::iniParser::IniParser::getValue(const char* section, const char* option, const char* path)
{
    Function::Arguments args(section, option, path);
    return callMethod("getValue", args).ToString();
}



const char* library::tools::iniParser::IniParser::setValue(const char* section, const char* option, const char* value)
{
    Function::Arguments args(section, option, value);
    return callMethod("setValue", args).ToString();
}



void library::tools::iniParser::IniParser::swapFile(const char* file_path)
{
    Function::Arguments arg(file_path);
    callMethod("swapFile", arg);
}



void library::tools::iniParser::IniParser::clearConfig()
{
    Function::Arguments arg;
    callMethod("clearConfig", arg);
}



void library::tools::iniParser::IniParser::update()
{
    Function::Arguments arg;
    callMethod("update", arg);
}



// INPUT MODULE

const char* library::tools::input::voiceInput()
{  
    static Function func("tools.input", "voiceInput");

    Function::Arguments arg;
    return func.call(arg).ToString();
}



// LOGGER MODULE

library::tools::logger::Logger::Logger() : Class("tools.logger", "Logger", Function::Arguments())
{

}


library::tools::logger::Logger * library::tools::logger::Logger::getInstance()
{
    static Logger* instance = new Logger();
    return instance;
}



void library::tools::logger::Logger::addRecord(const char* recordTitle, const char* value)
{
    Function::Arguments args(recordTitle, value);
    callMethod("addRecord", args);
}



void library::tools::logger::Logger::logWrite()
{
    Function::Arguments arg;
    callMethod("logWrite", arg);
}



// RUNTIME MODULE

void library::tools::runtime::restart()
{
    static Function func("tools.runtime", "restart");

    Function::Arguments arg;
    func.call(arg);
}



// SYSTEM MODULE

library::tools::system::FileManager::FileManager() : Class("tools.system", "FileManager", Function::Arguments())
{

}



library::tools::system::FileManager* library::tools::system::FileManager::getInstance()
{
    static FileManager* instance = new FileManager();
    return instance;
}



bool library::tools::system::FileManager::fileExist(const char* file)
{
    Function::Arguments arg(file);
    return callStaticMethod("tools.system", "FileManager", "fileExist", arg).ToBool();
}



void library::tools::system::FileManager::writeToFile(const char* value, const char* file, const char* mode, const char* _encoding)
{
    Function::Arguments args(value, file, mode, _encoding);
    callStaticMethod("tools.system", "FileManager", "writeToFile", args);
}



const char* library::tools::system::FileManager::readFile(const char* file, const char* _encoding)
{
    Function::Arguments args(file, _encoding);
    return callStaticMethod("tools.system", "FileManager", "readFile", args).ToString();
}



void library::tools::system::FileManager::createFile(const char* file)
{
    Function::Arguments arg(file);
    callStaticMethod("tools.system", "FileManager", "createFile", arg);
}



void library::tools::system::FileManager::deleteFile(const char* file)
{
    Function::Arguments arg(file);
    callStaticMethod("tools.system", "FileManager", "deleteFile", arg);
}



void library::tools::system::FileManager::clearFile(const char* file)
{
    Function::Arguments arg(file);
    callStaticMethod("tools.system", "FileManager", "clearFile", arg);
}



library::tools::system::FileManager::~FileManager()
{
    Function::Arguments arg;
    callMethod("__del__", arg);
}




library::tools::system::Network::Network() : Class("tools.system", "Network", Function::Arguments())
{

}



library::tools::system::Network* library::tools::system::Network::getInstance()
{
    static Network* instance = new Network();
    return instance;
}



bool library::tools::system::Network::checkNetworkConnection()
{
    Function::Arguments arg;
    return callStaticMethod("tools.system", "Network", "checkNetworkConnection", arg).ToBool();
}



// TIME MODULE

library::tools::time::Stopwatch::Stopwatch() : Class("tools.time", "Stopwatch", Function::Arguments())
{

}



void library::tools::time::Stopwatch::start()
{
    Function::Arguments arg;
    callMethod("start", arg);
}



int library::tools::time::Stopwatch::stop()
{
    Function::Arguments arg;
    return callMethod("start", arg).ToLong();
}



// MAIN MODULE

library::main::Amelie::Amelie(const char* appLanguage) : Class("Amelie", "Amelie", Function::Arguments(appLanguage))
{

}



library::main::Amelie* library::main::Amelie::getInstance(const char* appLanguage)
{
    static Amelie* instance = new Amelie(appLanguage);
    return instance;
}



void library::main::Amelie::changeLanguage(const char* language)
{
    Function::Arguments arg(language);
    callMethod("changeLanguage", arg);
}



char* library::main::Amelie::conversation(bool enableVoice, const char* userInput)
{
    Function::Arguments arg(enableVoice, userInput);
    return callMethod("conversation", arg).ToString();
}



void library::main::Amelie::tts(const char* pharse)
{
    Function::Arguments arg(pharse);
    callMethod("tts", arg);
}



bool library::main::Amelie::getVoice()
{
    Function::Arguments arg;
    return callMethod("getVoice", arg).ToBool();
}



const char* library::main::Amelie::getUserInput()
{
    Function::Arguments arg;
    return callMethod("getUserInput", arg).ToString();
}



library::main::Amelie::~Amelie()
{
    Function::Arguments arg;
    callMethod("__del__", arg);
}




library::main::Settings::Settings() : Class("Settings", "Settings", Function::Arguments())
{

}



library::main::Settings* library::main::Settings::getInstance()
{
    static Settings* instance = new Settings();
    return instance;
}



void library::main::Settings::setLanguage(const char* langValue)
{
    Function::Arguments arg(langValue);
    callMethod("setLanguage", arg);
}



bool library::main::Settings::setUsername(const char* nameValue)
{
    Function::Arguments arg(nameValue);
    return callMethod("setUsername", arg).ToBool();
}



void library::main::Settings::setBotAvatar(const char* avatarName)
{
    Function::Arguments arg(avatarName);
    callMethod("setBotAvatar", arg);
}



void library::main::Settings::setUserAvatar(const char* avatarName)
{
    Function::Arguments arg(avatarName);
    callMethod("setUserAvatar", arg);
}



const char* library::main::Settings::getLanguage()
{
    Function::Arguments arg;
    return callMethod("getLanguage", arg).ToString();
}



std::vector<const char*> library::main::Settings::getSupportingLangs()
{
    Function::Arguments arg;
    return callMethod("getSupportingLangs", arg).ToVector<const char*>();
}



std::vector<const char*> library::main::Settings::getBotAvatars()
{
    Function::Arguments arg;
    return callMethod("getBotAvatars", arg).ToVector<const char*>();
}



std::vector<const char*> library::main::Settings::getUserAvatars()
{
    Function::Arguments arg;
    return callMethod("getUserAvatars", arg).ToVector<const char*>();
}



const char* library::main::Settings::getBotAvatar()
{
    Function::Arguments arg;
    return callMethod("getBotAvatar", arg).ToString();
}



const char* library::main::Settings::getUserAvatar()
{
    Function::Arguments arg;
    return callMethod("getUserAvatar", arg).ToString();
}



const char* library::main::Settings::getUsername()
{
    Function::Arguments arg;
    return callMethod("getUsername", arg).ToString();
}



std::multimap<const char*, void*> library::main::Settings::getMethodsToResolveErrors()
{
    Function::Arguments arg;
    return callMethod("getMethodsToResolveErrors", arg).ToMultimap<const char*, void*>();
}
