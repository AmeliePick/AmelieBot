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

    Q_INVOKABLE QString chatConversation(bool enableVoice, QString input = "");

    Q_INVOKABLE QUrl initSettingsWindow();

    Q_INVOKABLE bool setUsername(QString nameValue);

    Q_INVOKABLE QString getUsername();

    Q_INVOKABLE void setLanguage(QString langValue);

    Q_INVOKABLE QString getLanguage();

    Q_INVOKABLE std::vector<const char*> getSupportingLangs();

    Q_INVOKABLE QString getUserInput();

    Q_INVOKABLE std::vector<const char*> getBotAvatars();

    Q_INVOKABLE std::vector<const char*> getUserAvatars();

    Q_INVOKABLE QString getBotAvatar();

    Q_INVOKABLE QString getUserAvatar();

    Q_INVOKABLE void setBotAvatar(QString avatarName);

    Q_INVOKABLE void setUserAvatar(QString avatarName);

    Q_INVOKABLE QString setPreviewAvatar(QString avatarType, QString avatarName);


    Q_INVOKABLE void closeAmelieEvent();

    Q_INVOKABLE ~AmelieEvent();
};





class AmelieApplication
{
private:
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

        ~Settings();
    };



    class Chat
    {
    private:
        Chat() = delete;
        Chat(const char* appLanguage);
        Chat(const Chat &) = delete;


        void* classInstance;

    public:
        static Chat* getInstance(const char* appLanguage);

        void changeLanguage(const char* language);

        char* conversation(bool enableVoice, const char* userInput = "");

        void tts(const char* pharse);

        bool getVoice();

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

        int showMainWindow();

        QUrl initSettingsWindow();

        void showSettingsWindow();

        ~GUI();
    };



    AmelieApplication();
    AmelieApplication(const AmelieApplication &) = delete;


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

    QUrl initSettingsWindow();

    char* chatConversation(bool enableVoice, QString input = "");

    QString getUserInput();

    std::vector<const char*> getBotAvatars();

    std::vector<const char*> getUserAvatars();

    void setBotAvatar(QString avatarName);

    void setUserAvatar(QString avatarName);

    QString getBotAvatar();

    QString getUserAvatar();

    int main(int argc, char** argv);

    ~AmelieApplication();
};

#endif // AMELIE_H
