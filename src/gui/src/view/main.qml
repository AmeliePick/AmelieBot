import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.1



Window
{
    function pushMessagesToChat(userInput, answer)
    {
        messageModel.append({positionX: 0, toReflect: 1,text: userInput, avatar: "../../../../resources/AppIcon/userAvatar.png"})
        messageModel.append({positionX: 1255, toReflect: -1, text: answer, avatar: "../../../../resources/AppIcon/botAvatar.png"});
    }


    color: "#0c1128";
    visible: true;

    minimumHeight: 780;
    maximumHeight: 780;
    minimumWidth: 1600;
    maximumWidth: 1600;

    title: qsTr("Amelie Bot")

    Grid {
        width: 1600; height: 780; columns: 3;


        // Left panel
        Rectangle
        {
            width: 300;  height: 780; color: "#0c1128";

            // Left top line
            Rectangle
            {
                y: 100; width: 300;  height: 5; color: "#545454";
            }

            Text {
                width: 300;
                height: 100;
                horizontalAlignment: Text.AlignHCenter;
                verticalAlignment: Text.AlignVCenter;
                color: "#9382dc";
                font.pixelSize: 32;
                font.family: "Magneto"
                text: qsTr("Amelie Bot");

            }


            // Menu
            Rectangle
            {
                x: 0;
                y: 106;
                width: 300;
                height: 594;
                color: "#0c1128";


                Button
                {
                    x: 75;
                    y: 50;
                    width: 150;
                    height: 44;

                    background: Rectangle
                    {
                        color: "#0c1128";
                    }

                    contentItem: Text
                    {
                        width: 150;
                        height: 44;

                        verticalAlignment: Text.AlignVCenter;

                        color: "gray";
                        font.pixelSize: 32;
                        font.family: "Montserrat";
                        text: "History";
                    }


                }



                Button
                {
                    x: 75;
                    y: 110;
                    width: 150;
                    height: 44;
                    palette { button: "#0c1128"; }

                    background: Rectangle
                    {
                        color: "#0c1128";
                    }

                    contentItem: Text
                    {
                        width: 150;
                        height: 44;

                        verticalAlignment: Text.AlignVCenter;

                        color: "gray";
                        font.pixelSize: 32;
                        font.family: "Montserrat";
                        text: "Settings";
                    }

                    onClicked:
                    {
                        Event.showSettingsWindow();
                    }
                }


            }


            // Left bottom line
            Rectangle
            {
                y: 700; width: 300;  height: 5; color: "#545454";
            }

            Text {
                y: 700;
                width: 300;
                height: 80;
                horizontalAlignment: Text.AlignHCenter;
                verticalAlignment: Text.AlignVCenter;
                color: "#9382dc";
                font.pixelSize: 20;
                font.family: "Magneto";
                text: qsTr("AmeliePick ©");

            }
        }


        // Menu border line
        Rectangle { width: 5;    height: 780; color: "#545454"; }


        // Chat window
        Rectangle
        {
            width: 1295; height: 780; color: "#0c1128";


            // Chat
            ListModel
            {
                id: messageModel;
            }

            ListView
            {
                topMargin: 20;
                leftMargin: 20;
                rightMargin: 20;

                id: chat;
                width: 1295;
                height: 670;
                spacing: 20;
                ScrollBar.vertical: ScrollBar {}

                model: messageModel;
                delegate: MessageItem
                {
                    toReflect: model.toReflect;
                    positionX: model.positionX;
                    text: model.text;
                    avatar: model.avatar;
                }

                onCountChanged:
                {
                    highlightFollowsCurrentItem
                }

            }


            // Input Area
            Rectangle
            {
                y: 700;
                height: 80;
                width: 1295;
                color: "#1f2646";
            }
            TextInput
            {
                id: textInput;
                y: 700;
                height: 80;
                width: 1295;
                font.pixelSize: 32;
                color: "#626262";
                leftPadding: 30;
                rightPadding: 30;
                topPadding: 15;
                bottomPadding: 15;
                font.family: "Montserrat";
                text: "Enter the message: ";

                onAccepted:
                {
                    var answer = Event.chatConversation(textInput.text);

                    pushMessagesToChat(textInput.text, answer);

                    chat.positionViewAtEnd();

                    textInput.text = "";

                }
            }


            Button
            {
                x: 1215;
                y: 700;
                width: 80;
                height: 80;
                palette { button: "#1f2646"; }

                Image
                {
                    width: 80;
                    height: 80;
                    source: "res/images/microphone.ico";
                }

                onClicked:
                {
                    Event.setVoice(true);

                    var userInput = Event.voiceInput();
                    var answer = Event.chatConversation(userInput);

                    pushMessagesToChat(userInput, answer);

                    chat.positionViewAtEnd();

                    Event.setVoice(false);

                }
            }
        }
    }
}




/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.5;height:480;width:640}
}
##^##*/
