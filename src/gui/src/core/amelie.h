#ifndef AMELIE_H
#define AMELIE_H
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QIcon>
#include <QString>
#include "dllimport.inl"



class AmelieEvent : public QObject
{
private:
    Q_OBJECT

    class AmelieApplication* amelie;

    AmelieEvent();
    AmelieEvent(const AmelieEvent &) = delete;

public:
    static AmelieEvent* getInstance();

    Q_INVOKABLE QString chatConversation(QString input);

    Q_INVOKABLE void showSettingsWindow();

    Q_INVOKABLE void setVoice(bool enableVoice);

    Q_INVOKABLE bool setUsername(QString nameValue);

    Q_INVOKABLE QString getUsername();

    Q_INVOKABLE void setLanguage(QString langValue);

    Q_INVOKABLE QString getLanguage();

    Q_INVOKABLE std::vector<const char*> getSupportingLangs();

    Q_INVOKABLE QString voiceInput();

    Q_INVOKABLE std::vector<const char*> getBotAvatars();

    Q_INVOKABLE std::vector<const char*> getUserAvatars();

    Q_INVOKABLE QString getBotAvatar();

    Q_INVOKABLE QString getUserAvatar();

    Q_INVOKABLE void setBotAvatar(QString avatarName);

    Q_INVOKABLE void setUserAvatar(QString avatarName);

public:

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



    class Settings
    {
    private:
        Settings();
        Settings(const Settings &) = delete;

        void* classInstance;

    public:
        static Settings* getInstance();

        void setLanguage(QString langValue);

        bool setUsername(QString nameValue);

        void setBotAvatar(QString avatarName);

        void setUserAvatar(QString avatarName);

        const char* getLanguage();

        std::vector<const char*> getSupportingLangs();

        std::vector<const char*> getBotAvatars();

        std::vector<const char*> getUserAvatars();

        QString getUsername();

        const char* getBotAvatar();

        const char* getUserAvatar();

        std::multimap<const char*, void*> getMethodsToResolveErrors();
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

        int showMainWindow(Chat* chat);

        int showSettingsWindow();
    };



    AmelieApplication();
    AmelieApplication(const AmelieApplication &) = delete;



    FileManager* fileManager;
    Network* network;

    Settings* settings;
    Chat* chat;

    GUI* gui;

public:
    static AmelieApplication* getInstance();

    void initChatBot();

    void setLanguage(QString langValue);

    std::vector<const char*> getSupportingLangs();

    QString getLanguage();

    bool setUsername(QString nameValue);

    QString getUsername();

    void showSettingsWindow();

    QString chatConversation(QString input);

    void setVoice(bool enableVoice);

    QString voiceInput();

    void update();

    std::vector<const char*> getBotAvatars();

    std::vector<const char*> getUserAvatars();

    void setBotAvatar(QString avatarName);

    void setUserAvatar(QString avatarName);

    QString getBotAvatar();

    QString getUserAvatar();

    int main(int argc, char** argv);
};

#endif // AMELIE_H
