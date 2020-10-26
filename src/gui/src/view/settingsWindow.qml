import QtQuick 2.0
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

Window
{
    function setPreviewAvatar(avatarType, avatarName)
    {
        if(avatarType == "bot")
            botAvatar.source = "../../../../resources/AppIcon/" + avatarType + "/avatar/" + avatarName + ".png";
        else if(avatarType == "user")
            userAvatar.source = "../../../../resources/AppIcon/" + avatarType + "/avatar/" + avatarName + ".png";
    }



    id: settingsWindow;
    title: qsTr("Settings")
    color: "#0c1128";
    visible: true;

    minimumHeight: 800;
    maximumHeight: 800;
    minimumWidth: 800;
    maximumWidth: 800;



    Item
    {
        x: 150;
        y: 32;

        height: 86
        width: 500;

        Text {
            width: 500;
            height: 20;
            horizontalAlignment: Text.AlignHCenter;
            font.pixelSize: 20;
            color: "white";
            text: qsTr("User Avatar")
        }

        Rectangle
        {
            id: user_avatar_circle;
            transform: mirror;
            width: 86;
            height: 86
            radius: 400;
            Image
            {
                id: userAvatar;
                width: 86
                height: 86;
                source: setPreviewAvatar("user", userAvatarList[0]);
            }
        }

        ComboBox
        {
            id: userAvatars;
            x: 150;
            y: 43;
            width: 316;
            height: 33;

            model: userAvatarList;


            onActivated:
            {
                setPreviewAvatar("user", userAvatars.currentText);
            }
        }

    }

    Item
    {
        x: 150;
        y: 182;

        height: 86
        width: 500;

        Text {
            width: 500;
            height: 20;
            horizontalAlignment: Text.AlignHCenter;
            font.pixelSize: 20;
            color: "white";
            text: qsTr("Bot's Avatar")
        }

        Rectangle
        {
            id: bot_avatar_circle;
            transform: mirror;
            width: 86;
            height: 86
            radius: 400;
            Image
            {
                id: botAvatar;
                width: 86
                height: 86;
                source: setPreviewAvatar("bot", botAvatarList[0]);
            }
        }

        ComboBox
        {
            id: botAvatars;
            x: 150;
            y: 43;
            width: 316
            height: 33;

            model: botAvatarList;


            onActivated:
            {
                setPreviewAvatar("bot", botAvatars.currentText);
            }
        }

    }

    Rectangle
    {
        y: 300;
        width: 800;
        height: 1;
        color: "gray";
    }

    Item
    {
        x: 150
        y: 350;
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
        x: 150;
        y: 450;
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


    Rectangle
    {
        y: 550;
        width: 800;
        height: 1;
        color: "gray";
    }

    Item
    {
        id: buttons
        x: 137;
        y: 625;
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
                    Event.setBotAvatar(botAvatars.currentText);
                    Event.setUserAvatar(userAvatars.currentText);
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
    D{i:0;autoSize:true;formeditorZoom:0.8999999761581421;height:800;width:800}
}
##^##*/
