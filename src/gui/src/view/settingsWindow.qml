import QtQuick 2.0
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

Window
{
    id: settingsWindow;
    color: "#0c1128";
    visible: true;

    minimumHeight: 390;
    maximumHeight: 390;
    minimumWidth: 800;
    maximumWidth: 800;


    Item
    {
        x: 70;
        y: 200;
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
            color: "#1f2646";
        }
    }


    Item
    {
        x: 70;
        y: 250;
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


        ListModel
        {
            id: languages;
        }

        ComboBox
        {
            id: applang;
            x: 184
            y: 0
            width: 316
            height: 50;

            model: languages;
        }
    }


    Item
    {
        id: item1
        x: 137
        y: 368
        width: 350;
        height: 100;
        anchors.horizontalCenter: parent.horizontalCenter

        Button
        {
            id: buttonApply;
            x: 75;
            y: 30;
            width: 80;
            height: 40;
            text: "Apply";

            contentItem: Text
            {
                color: "gray";
                font.family: "Montserrat";
                font.pixelSize: 20;
                text: buttonApply.text;
            }

            background: Rectangle
            {
                color: "#1f2646";
            }
        }


        Button
        {
            id: buttonCancel;
            x: 195;
            y: 30;
            width: 80;
            height: 40;
            text: "Cancel";

            contentItem: Text
            {
                color: "gray";
                font.family: "Montserrat";
                font.pixelSize: 20;
                text: buttonCancel.text;
            }

            background: Rectangle
            {
                color: "#1f2646";
            }
        }
    }





}



/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.659999966621399;height:480;width:640}
}
##^##*/
