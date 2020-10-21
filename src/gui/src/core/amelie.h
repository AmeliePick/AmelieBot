#ifndef AMELIE_H
#define AMELIE_H
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QIcon>
#include <QString>
#include "dllimport.inl"



class Settings : public QObject
{
private:
    Q_OBJECT

    Settings();
    Settings(const Settings &) = delete;

    void* classInstance;

public:
    static Settings* getInstance();

    Q_INVOKABLE void setLanguage(QString langValue);

    Q_INVOKABLE void setUsername(QString nameValue);

    const char* getLanguage();

    Q_INVOKABLE std::vector<const char*> getSupportingLangs();

    Q_INVOKABLE QString getUsername();

    std::multimap<const char*, void*> getMethodsToResolveErrors();
};



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


    class GUI
    {
    private:
        QGuiApplication* app;
        QQmlApplicationEngine* engine;

    public:
        GUI(int argc, char** argv);

        int showMainWindow(Chat* chat, Dialog* dialog);

        int showSettingsWindow(Settings* settings);
    };


    AmelieApplication();
    AmelieApplication(const AmelieApplication &) = delete;



    typedef void(*input)();
    input inputMode;

    FileManager* fileManager;
    Network* network;

    Settings* settings;
    Dialog* dialog;
    Chat* chat;

    GUI* gui;


public:
    static AmelieApplication* getInstance();

    void initChatBot();

    void changeInputMode(bool enableVoice);

    void showSettingsWindow();

    QString chatConversation(QString input);

    void setVoice(bool enableVoice);

    int main(int argc, char** argv);
};



class AmelieEvent : public QObject
{
private:
    Q_OBJECT

    AmelieApplication* amelie;

public:
    AmelieEvent();

    Q_INVOKABLE QString chatConversation(QString input);

    Q_INVOKABLE void showSettingsWindow();

    Q_INVOKABLE void setVoice(bool enableVoice);

public:

};

#endif // AMELIE_H
