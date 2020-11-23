#pragma once
#include "function.h"
#include "class.h"
#include <vector>


namespace library
{
    namespace main
    {
        class Amelie : private Class
        {
        private:
            Amelie() = delete;
            Amelie(const char* appLanguage);
            Amelie(const Amelie &) = delete;

        public:
            static Amelie* getInstance(const char* appLanguage);

            void changeLanguage(const char* language);

            char* conversation(bool enableVoice, const char* userInput = "");

            void tts(const char* pharse);

            bool getVoice();

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

            bool setUsername(const char* nameValue);

            void setBotAvatar(const char* avatarName);

            void setUserAvatar(const char* avatarName);

            const char* getLanguage();

            std::vector<const char*> getSupportingLangs();

            std::vector<const char*> getBotAvatars();

            std::vector<const char*> getUserAvatars();

            const char* getBotAvatar();

            const char* getUserAvatar();

            const char* getUsername();

            std::multimap<const char*, void*> getMethodsToResolveErrors();

            ~Settings();
        };
    }
}

