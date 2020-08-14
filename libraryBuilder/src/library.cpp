#include "library.h"



// PROCESSING MODULE

void library::audio::processing::playAudio(const char* soundFile, int reps)
{
    static Function pyFunc("audio.processing", "playAudio");
    
    Function::Arguments args(soundFile, reps);
    pyFunc.call(nullptr, args);
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
    this->callMethod("__call__", nullptr, args);
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
    this->callMethod("calibration", nullptr, arg);
}



void library::audio::recognition::SpeechRecognition::recognize()
{
    Function::Arguments arg;
    this->callMethod("recognize", nullptr, arg);
}



// CHAT MODULE

library::chat::AICore::Chat* library::chat::AICore::Chat::getInstance(const char* appLanguage)
{
    static Chat* instance = new Chat(appLanguage);
    return instance;
}



const char* library::chat::AICore::Chat::getInput()
{
    
}



const char* library::chat::AICore::Chat::getInputType()
{
    
}



const char* library::chat::AICore::Chat::getSessionInput()
{
    
}



const char* library::chat::AICore::Chat::getLanguage()
{
    
}



const char* library::chat::AICore::Chat::launch(const char* input_)
{
    Function::Arguments arg(input_);
    callMethod("launch", nullptr, arg);
}



void library::chat::AICore::Chat::changeLanguage(const char* language)
{
    Function::Arguments arg(language);
    callMethod("changeLanguage", nullptr, arg);
}



void library::chat::AICore::Chat::stemming(const char* expression)
{
    Function::Arguments arg(expression);
    callMethod("stemming", nullptr, arg);
}



void library::chat::AICore::Chat::editInput(int meaningLength)
{
    Function::Arguments arg(meaningLength);
    callMethod("editInput", nullptr, arg);
}
