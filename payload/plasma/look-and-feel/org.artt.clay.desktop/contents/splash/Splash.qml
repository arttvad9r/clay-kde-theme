import QtQuick

Rectangle {
    id: root
    color: "#F0ECE5"

    property int stage: 0

    Rectangle {
        width: parent.width * 0.38
        height: parent.height * 0.30
        radius: Math.min(width, height) * 0.28
        color: "#E18A66"
        opacity: 0.46
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: -width * 0.08
        anchors.topMargin: -height * 0.34
        rotation: -6
    }

    Rectangle {
        width: parent.width * 0.42
        height: parent.height * 0.27
        radius: Math.min(width, height) * 0.32
        color: "#D4C6B9"
        opacity: 0.72
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.leftMargin: -width * 0.13
        anchors.bottomMargin: -height * 0.24
        rotation: 4
    }

    Column {
        anchors.centerIn: parent
        spacing: 20

        Image {
            id: mark
            width: 88
            height: 88
            anchors.horizontalCenter: parent.horizontalCenter
            source: "images/clay-mark.svg"
            fillMode: Image.PreserveAspectFit
            opacity: root.stage >= 5 ? 0 : 1

            Behavior on opacity {
                NumberAnimation { duration: 220; easing.type: Easing.InOutQuad }
            }
        }

        Rectangle {
            id: track
            width: 84
            height: 3
            radius: 1.5
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#D7CFC5"

            Rectangle {
                id: indicator
                width: 24
                height: parent.height
                radius: parent.radius
                color: "#E66F43"
                x: 0

                SequentialAnimation on x {
                    running: root.stage < 5
                    loops: Animation.Infinite
                    NumberAnimation {
                        from: 0
                        to: track.width - indicator.width
                        duration: 760
                        easing.type: Easing.InOutQuad
                    }
                    NumberAnimation {
                        from: track.width - indicator.width
                        to: 0
                        duration: 760
                        easing.type: Easing.InOutQuad
                    }
                }
            }
        }
    }

    opacity: stage >= 5 ? 0 : 1
    Behavior on opacity {
        NumberAnimation { duration: 240; easing.type: Easing.InOutQuad }
    }
}
