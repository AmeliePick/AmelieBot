#pragma once
#include "function.h"
#include "class.h"



namespace library
{
    namespace audio
    {
        namespace processing
        {
            void playAudio(const char* soundFile, int reps = 1);

            class TextToSpeech : private Class
            {
            private:
                TextToSpeech();
                TextToSpeech(const TextToSpeech &) = delete;

            public:
                static TextToSpeech* getInstance();

                void operator ()(const char* textSource, const char* srcLang);
            };
        }


        namespace recognition
        {
            class SpeechRecognition : private Class
            {
            private:
                SpeechRecognition() = delete;
                SpeechRecognition(const char* appLanguage);
                SpeechRecognition(const SpeechRecognition &) = delete;

            public:
                static SpeechRecognition* getInstance(const char* appLanguage);

                void calibration();

                void recognize();
            };
        }
    }


    namespace chat
    {
        namespace AICore
        {
            class Chat : private Class
            {
            private:
                Chat() = delete;
                Chat(const char* appLanguage);
                Chat(const Chat &) = delete;

            public:
                static Chat* getInstance(const char* appLanguage);

                const char* getInput();

                const char* getInputType();

                const char* getSessionInput();

                const char* getLanguage();

                const char* launch(const char* input_ = "");


                void changeLanguage(const char* language);

                void stemming(const char* expression);

                void editInput(int meaningLength = 2);
            };
        }
    }


    namespace tools
    {

    }
}

