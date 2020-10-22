import QtQuick 2.0
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

Window
{
    id: settingsWindow;
    title: qsTr("Settings")
    color: "#0c1128";
    visible: true;

    minimumHeight: 390;
    maximumHeight: 390;
    minimumWidth: 800;
    maximumWidth: 800;


    Item
    {
        x: 150
        y: 85;
        width: 500;
        height: 50;


        Text
        {
            width: 116
            height: 50
            x: 0
            y: 0
            color: "white";
            text: qsTr("Username:")
            font.family: "Montserrat";
            font.pixelSize: 20;
            verticalAlignment: Text.AlignVCenter;
        }

        TextInput
        {
            id: userName;
            x: 117
            y: 0
            width: 383
            height: 50;
            verticalAlignment: Text.AlignVCenter;
            font.family: "Montserrat";
            font.pixelSize: 20;
            color: "white";
            text: Event.getUsername();

        }

        Text
        {
            id: usernameErrorText;
            width: 500
            height: 23
            x: 0
            y: 42
            color: "Red";
            font.family: "Montserrat";
            font.pixelSize: 15;
            verticalAlignment: Text.AlignVCenter;
        }
    }


    Item
    {
        x: 150
        y: 170
        width: 500;
        height: 50;


        Text
        {
            x: 0
            y: 0
            width: 183
            height: 50
            color: "white";
            text: qsTr("Bot's Language:")
            font.family: "Montserrat";
            font.pixelSize: 20;
            verticalAlignment: Text.AlignVCenter;
        }

        ComboBox
        {
            id: applang;
            x: 189
            y: 9
            width: 316
            height: 33

            model: Langs
        }
    }


    Item
    {
        id: buttons
        x: 137
        y: 269
        width: 350;
        height: 100;
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter

        Button
        {
            id: buttonApply;
            x: 75;
            y: 30;
            width: 80;
            height: 40;



            contentItem: Text
            {
                width: 60;
                height: 40;

                verticalAlignment: Text.AlignVCenter;
                horizontalAlignment: Text.AlignHCenter;

                color: "gray";
                font.pixelSize: 20;
                font.family: "Montserrat";
                text: "Apply";
            }

            background: Rectangle
            {
                color: "#1f2646";
            }

            onClicked:
            {
                if(Event.setUsername(userName.text))
                {

                    Event.setLanguage(applang.currentText);
                    settingsWindow.close();
                }
                else
                {
                    usernameErrorText.text = "Username is too short, please try again."
                }


            }
        }


        Button
        {
            x: 195;
            y: 30;
            width: 80;
            height: 40;

            contentItem: Text
            {
                width: 60;
                height: 40;

                verticalAlignment: Text.AlignVCenter;
                horizontalAlignment: Text.AlignHCenter;

                color: "gray";
                font.pixelSize: 20;
                font.family: "Montserrat";
                text: "Cancel";
            }

            background: Rectangle
            {
                color: "#1f2646";
            }

            onClicked:
            {
                settingsWindow.close();
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.75;height:480;width:640}
}
##^##*/
