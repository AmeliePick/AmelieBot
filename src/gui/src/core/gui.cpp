#include "gui.h"


GUI::GUI(int argc, char** argv)
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    this->app = new QGuiApplication(argc, argv);
    this->engine = new QQmlApplicationEngine();

    app->setWindowIcon(QIcon("../../../resources/AppIcon/icon.ico"));
}


int GUI::showMainWindow(void* chat, void* dialog)
{
    engine->rootContext()->setContextProperty("Chat", (QObject*)chat);
    engine->rootContext()->setContextProperty("Dialog", (QObject*)dialog);
    engine->load(QUrl::fromLocalFile("../src/view/main.qml"));

    return app->exec();
}


int GUI::showSettingsWindow(void* settings)
{
    engine->rootContext()->setContextProperty("Chat", (QObject*)settings);
    engine->load(QUrl::fromLocalFile("../src/view/settingsWindow.qml"));

    return app->exec();
}
