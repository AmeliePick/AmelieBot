#ifndef GUI_H
#define GUI_H
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QIcon>

class GUI
{
private:
    QGuiApplication* app;
    QQmlApplicationEngine* engine;

public:
    GUI(int argc, char** argv);

    int showMainWindow(void* chat, void* dialog);

    int showSettingsWindow(void* settings);
};


#endif // GUI_H
