import QtQuick

Rectangle {
    id: root
    color: "#262624"

    property int stage: 0

    // Same artwork as the Clay wallpaper, so the fade-out lands on an
    // identical desktop instead of cutting between two compositions.
    Image {
        anchors.fill: parent
        source: "images/background.png"
        fillMode: Image.PreserveAspectCrop
        asynchronous: false
    }

    Column {
        id: content
        anchors.centerIn: parent
        spacing: 22
        opacity: 0
        scale: 0.94

        Component.onCompleted: intro.start()

        ParallelAnimation {
            id: intro
            NumberAnimation { target: content; property: "opacity"; to: 1; duration: 420; easing.type: Easing.OutCubic }
            NumberAnimation { target: content; property: "scale"; to: 1; duration: 520; easing.type: Easing.OutCubic }
        }

        Image {
            id: mark
            width: 88
            height: 88
            anchors.horizontalCenter: parent.horizontalCenter
            source: "images/clay-mark.svg"
            sourceSize: Qt.size(176, 176)
            fillMode: Image.PreserveAspectFit
        }

        Rectangle {
            id: track
            width: 84
            height: 3
            radius: 1.5
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#3D3D3A"

            Rectangle {
                id: indicator
                width: 24
                height: parent.height
                radius: parent.radius
                color: "#D97757"
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
        NumberAnimation { duration: 320; easing.type: Easing.InOutQuad }
    }
}
