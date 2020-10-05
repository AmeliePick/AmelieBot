#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QIcon>

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    QGuiApplication app(argc, argv);
    app.setWindowIcon(QIcon("../../../resources/AppIcon/icon.ico"));

    QQmlApplicationEngine engine;
    engine.load(QUrl::fromLocalFile("../src/view/main.qml"));

    return app.exec();
}
