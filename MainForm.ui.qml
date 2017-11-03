import QtQuick 2.6

Rectangle {
    property alias mouseArea: mouseArea

    width: 800
    height: 480

    MouseArea {
        id: mouseArea
        width: 800
        height: 480
        anchors.fill: parent

        Image {
            id: image
            x: 0
            y: 0
            width: 800
            height: 480
            source: "../../Images/zonnebloem.jpg"

            Text {
                id: datum
                x: 23
                y: 430
                color: "#ffffff"
                text: qsTr("3 November 2017")
                style: Text.Outline
                styleColor: "#4c000000"
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                textFormat: Text.RichText
                renderType: Text.NativeRendering
                fontSizeMode: Text.Fit
                font.pixelSize: 27
            }

            Text {
                id: welkom
                x: 191
                y: 15
                color: "#ffffff"
                text: qsTr("Goedemorgen Peter")
                font.strikeout: false
                font.wordSpacing: 5
                padding: 12
                textFormat: Text.RichText
                renderType: Text.NativeRendering
                fontSizeMode: Text.Fit
                styleColor: "#994a4a4a"
                font.italic: false
                font.family: "Verdana"
                verticalAlignment: Text.AlignVCenter
                style: Text.Outline
                horizontalAlignment: Text.AlignHCenter
                font.weight: Font.ExtraBold
                font.bold: false
                font.pixelSize: 40
            }

            Text {
                id: tijd
                x: 16
                y: 350
                color: "#ffffff"
                text: qsTr("10:51")
                styleColor: "#4c000000"
                style: Text.Outline
                font.bold: true
                font.pixelSize: 81
            }
        }
    }
}
