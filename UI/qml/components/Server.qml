import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Component {

    Rectangle {
        id: cont

        property int progress_percent: 0
        property string message: ""
        property bool done: true

        Component.onCompleted: {
            stage = 3;
            done = false;
            startServerInstallation()
        }

        ColumnLayout {
            anchors.fill: parent
            spacing: 0

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "black"

                Column {
                    anchors.top: parent.top
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 24
                    spacing: 16

                    Text {
                        text: qsTr("Uninstalling Server")
                        font.family: "Segoe UI Semilight"
                        font.pixelSize: 14
                        color: "white"
                    }

                    Rectangle {
                        width: parent.width
                        height: 8
                        border.color: Qt.rgba(255, 255, 255, 0.2)
                        color: "transparent"

                        Rectangle {
                            width: (parent.width / 100) * cont.progress_percent
                            height: parent.height
                            color: "dodgerblue"
                            clip: true
                        }

                    }

                    Text {
                        width: parent.width - 12
                        topPadding: -16
                        text: cont.message
                        elide: Text.ElideMiddle
                        font.family: "Segoe UI Semilight"
                        font.pixelSize: 12
                        color: "white"
                    }

                }

            }

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 56
                color: "black"

                Row {
                    anchors.centerIn: parent
                    spacing: 4

                    Button {
                        text: qsTr("Back")

                        onClicked: {
                            stopServerInstallation();
                        }

                    }

                    Button {
                        text: qsTr("Next")
                        enabled: done

                        onClicked: {
                            proceedAfterServerInstallation();
                        }

                    }

                }

            }

        }

    }

}

