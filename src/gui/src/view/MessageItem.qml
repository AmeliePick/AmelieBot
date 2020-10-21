import QtQuick 2.12
import QtQuick.Shapes 1.12


Item
{
    id: messageItem;

    property alias text: message.text;
    property alias avatar: avatar.source;
    property alias mirror: mirrorMatrix.matrix;

    Matrix4x4
    {
        id: mirrorMatrix;
        matrix: Qt.matrix4x4(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    }

    transform: mirrorMatrix;

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
            x: -6
            y: 14
            width: 82
            height: 68

            ShapePath
            {
                  strokeWidth: 1
                  strokeColor: "#32406f"
                  fillColor: "#32406f";
                  startX: 0; startY: 0;
                  PathLine { x: 90; y: 40;  }
                  PathLine { x: 30; y: 40 ;}
              }
          }

        Rectangle
        {
            x: 11;
            y: 23;
            width: 537;
            height: 67;
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

/*##^##
Designer {
    D{i:0;formeditorZoom:1.100000023841858}
}
##^##*/
