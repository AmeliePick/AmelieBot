import QtQuick 2.12
import QtQuick.Window 2.12
import QtCanvas3D 1.1


Window
{
    color: "#0c1128"
    visible: true

    minimumHeight: 780
    maximumHeight: 780
    minimumWidth: 1600
    maximumWidth: 1600

    title: qsTr("Amelie Bot")

    Grid {
        width: 1600
        height: 780
        columns: 3


        // Left menu
        Rectangle
        {
            width: 300;  height: 780; color: "#0c1128";

            // Left top line
            Rectangle
            {
                y: 100; width: 300;  height: 5; color: "#545454";
            }

            Text {
                width: 300
                height: 100
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                color: "#9382dc";
                font.pixelSize: 32;
                font.family: "Magneto"
                text: qsTr("Amelie Bot");

            }


            // Left bottom line
            Rectangle
            {
                y: 700; width: 300;  height: 5; color: "#545454";
            }

            Text {
                y: 700;
                width: 300
                height: 80
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                color: "#9382dc";
                font.pixelSize: 20;
                font.family: "Magneto"
                text: qsTr("AmeliePick ©");

            }
        }


        // Menu border line
        Rectangle { width: 5;    height: 780; color: "#545454"; }


        // Chat window
        Rectangle
        {
            width: 1295; height: 780; color: "#0c1128";


            // Input Area
            Rectangle
            {
                y: 700;
                height: 80
                width: 1295
                color: "#1f2646";
            }
            TextInput
            {
                y: 700;
                height: 80
                width: 1295;
                font.pixelSize: 32;
                color: "#626262";
                leftPadding: 30
                topPadding: 15
                bottomPadding: 15;
                font.family: "Montserrat";
                text: "Enter the message: ";
            }

        }
    }
}
