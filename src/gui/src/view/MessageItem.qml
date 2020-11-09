import QtQuick 2.12
import QtQuick.Shapes 1.12


Item
{
    FontLoader { id: fontMontserrat; source: "qrc:///resource/fonts/Montserrat.ttf" }

    id: messageItem;

    property alias text: message.text;
    property alias avatar: avatar.source;
    property alias toReflect: mirror.xScale;
    property alias positionX: messageItem.x;

    Scale{ id: mirror; xScale: 1 }
    transform: mirror;


    width: 640;
    height: 135;

    Rectangle
    {
        id: avatar_circle;
        transform: mirror;
        y: 0;
        x:
        {
            if(toReflect == 1)
            {

                avatar_circle.x = 0;
            }
            else
                avatar_circle.x = 80;
        }
        width: 86
        height: 86
        radius: 400;
        Image
        {
            id: avatar;
            x: 0;
            y: 0;
            width: 86;
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
            height: message.height;
            color: "#32406f";

            Text
            {
                id: message
                transform: mirror;
                x:{
                    if(toReflect == 1)
                    {

                        message.x = 0;
                    }
                    else
                        message.x = 537;
                }
                width: 537;
                padding: 10;
                font.pixelSize: 15;
                font.family: fontMontserrat.name;
                color: "#c5c5c5"
                wrapMode: Text.Wrap;
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.8999999761581421}
}
##^##*/
