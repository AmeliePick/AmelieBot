import QtQuick 2.12
import QtQuick.Shapes 2.12


Item
{
    id: messageItem;

    property alias text: message.text;
    property alias avatar: avatar.source;

    width: 640;
    height: 135;

    Rectangle
    {
        id: avatar_circle;
        x: 0
        y: 0
        width: 86
        height: 86
        radius: 400;
        visible: !sentByMe;
        Image
        {
            id: avatar;
            x: 0
            y: 0;
            width: 86
            height: 86;
        }
    }


    // Message area
    Rectangle
    {
        x: 92;
        y: 45;
        width: 548;
        height: 90;
        color: Qt.rgba(0, 0, 0, 0);

        // Arrow
        Shape
        {
            x: 0;
            y: 0;
            width: 32;
            height: 32;

            ShapePath
            {
                  strokeWidth: 1
                  strokeColor: "#32406f"
                  fillColor: "#32406f";
                  startX: 0; startY: 0;
                  PathLine { x: 80; y: 80;  }
                  PathLine { x: 40; y: 100 ;}
              }
          }

        Rectangle
        {
            x: 11;
            y: 23;
            width: 537;
            height: 67;
            visible: !sentByMe;
            color: "#32406f";


            Text
            {
                id: message
                width: 537
                height: 67
                padding: 10;
                font.pixelSize: 15;
                font.family: "Montserrat";
                color: "#c5c5c5"
            }
        }
    }
}
