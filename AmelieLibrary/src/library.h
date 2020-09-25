#pragma once
#include "function.h"
#include "class.h"



namespace library
{
    namespace audio
    {
        namespace processing
        {
            void playAudio(const char* soundFile);

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

                std::multimap<const char*, const char*> getSessionInput();

                const char* getLanguage();

                const char* launch(const char* input_ = "");


                void changeLanguage(const char* language);

                void stemming(const char* expression);

                void editInput(int meaningLength = 2);
            };
        }


        namespace dialog
        {
            class Dialog : private Class
            {
            private:
                Dialog() = delete;
                Dialog(const char* applanguage);
                Dialog(const Dialog &) = delete;

            public:
                static Dialog* getInstance(const char* appLanguage);

                const char* getMessageFor(const char* expression);

                void changeLanguage(const char* appLanguage);
            };
        }
    }


    namespace tools
    {
        namespace iniParser
        {
            class IniParser : private Class
            {
            public:
                IniParser(const char* fileToParsePath);

                void setSection(const char* section);

                const char* getValue(const char* section, const char* option, const char* path);

                const char* setValue(const char* section, const char* option, const char* value);

                void swapFile(const char* file_path);

                void clearConfig();

                void update();
            };
        }
        

        namespace input
        {
            const char* voiceInput();
        }


        namespace logger
        {
            class Logger : private Class
            {
            private:
                Logger();
                Logger(const Logger &) = delete;

            public:
                static Logger* getInstance();

                void addRecord(const char* recordTitle, const char* value);

                void logWrite();
            };
        }


        namespace runtime
        {
            void restart();
        }


        namespace system
        {
            class FileManager : private Class
            {
            private:
                FileManager();
                FileManager(const FileManager &) = delete;

            public:
                static FileManager* getInstance();

                static bool fileExist(const char* file);

                static void writeToFile(const char* value, const char* file, const char* mode = "a", const char* _encoding = "utf-8");

                static const char* readFile(const char* file, const char* _encoding = "utf-8");

                static void createFile(const char* file);

                static void deleteFile(const char* file);

                static void clearFile(const char* file);

                ~FileManager();
            };


            class Network : private Class
            {
            private:
                Network();
                Network(const Network &) = delete;

            public:
                static Network* getInstance();

                static bool checkNetworkConnection();
            };
        }


        namespace time
        {
            class Stopwatch : private Class
            {
            public:
                Stopwatch();

                void start();

                int stop();
            };
        }
    }


    namespace main
    {
        class Amelie : private Class
        {
        private:
            Amelie() = delete;
            Amelie(const char* appLanguage);
            Amelie(const Amelie &) = delete;


            void doAction(const char* inputType);

            void updateProgramList();

        public:
            static Amelie* getInstance(const char* appLanguage);

            void changeLanguage(const char* language);

            const char* conversation(const char* inputType);

            void tts(const char* pharse);

            void update();

            const char* getPathToProgram(const char* programName);

            void addProgram(const char* program, const char* path);

            bool getVoice();

            void setVoice(bool value);

            const char* getUserInput();


            ~Amelie();
        };


        class Settings : private Class
        {
        private:
            Settings();
            Settings(const Settings &) = delete;

        public:
            static Settings* getInstance();

            void setLanguage(const char* langValue);

            void setUsername(const char* nameValue);

            const char* getLanguage();

            std::multimap<int, const char*> getSupportingLangs();

            const char* getUsername();

            std::multimap<const char*, void*> getMethodsToResolveErrors();
        };
    }
}

