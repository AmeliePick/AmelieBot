#ifndef AMELIE_H
#define AMELIE_H
#include "dllimport.inl"
#include "gui.h"

class AmelieApplication
{
private:
    class FileManager
    {
    private:
        FileManager();
        FileManager(const FileManager &) = delete;

        void* classInstance;


    public:
        static FileManager* getInstance();

        bool fileExist(const char* file);

        void writeToFile(const char* value, const char* file, const char* mode = "a", const char* _encoding = "utf-8");

        const char* readFile(const char* file, const char* _encoding = "utf-8");

        void createFile(const char* file);

        void deleteFile(const char* file);

        void clearFile(const char* file);

        ~FileManager();
    };


    class Settings
    {
    private:
        Settings();
        Settings(const Settings &) = delete;

        void* classInstance;

    public:
        static Settings* getInstance();

        void setLanguage(const char* langValue);

        void setUsername(const char* nameValue);

        const char* getLanguage();

        std::multimap<int, const char*> getSupportingLangs();

        const char* getUsername();

        std::multimap<const char*, void*> getMethodsToResolveErrors();
    };


    class Network
    {
    private:
        Network();
        Network(const Network &) = delete;

        void* classInstance;


    public:
        static Network* getInstance();

        bool checkNetworkConnection();
    };


    class Logger
    {
    private:
        Logger();
        Logger(const Logger &) = delete;

        void* classInstance;

    public:
        static Logger* getInstance();

        void addRecord(const char* recordTitle, const char* value);

        void logWrite();
    };


    class Dialog
    {
    private:
        Dialog() = delete;
        Dialog(const char* applanguage);
        Dialog(const Dialog &) = delete;

        void* classInstance;

    public:
        static Dialog* getInstance(const char* appLanguage);

        const char* getMessageFor(const char* expression);

        void changeLanguage(const char* appLanguage);
    };


    class Chat
    {
    private:
        Chat() = delete;
        Chat(const char* appLanguage);
        Chat(const Chat &) = delete;


        void doAction(const char* inputType);

        void updateProgramList();

        void* classInstance;

    public:
        static Chat* getInstance(const char* appLanguage);

        void changeLanguage(const char* language);

        char* conversation(const char* userInput);

        void tts(const char* pharse);

        void update();

        const char* getPathToProgram(const char* programName);

        void addProgram(const char* program, const char* path);

        bool getVoice();

        void setVoice(bool value);

        const char* getUserInput();


        ~Chat();
    };


    typedef void(*input)();
    input inputMode;

    FileManager* fileManager;
    Network* network;

    Settings* settings;
    Dialog* dialog;
    Chat* chat;


public:
    AmelieApplication();

    void initChatBot();

    void changeInputMode(bool enableVoice);

    int main(int argc, char** argv);
};

#endif // AMELIE_H
