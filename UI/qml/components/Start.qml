import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import "." as Comp

RowLayout {
    //anchors.fill: parent
    spacing: 4

    Rectangle {
        Layout.preferredWidth: 200
        Layout.fillHeight: true

        Rectangle {
            anchors.fill: parent

            Image {
                sourceSize: Qt.size(parent.width, parent.height)
                source: "../../images/img102.jpg"
                fillMode: Image.PreserveAspectCrop
            }

        }

    }

    Rectangle {
        Layout.fillWidth: true
        Layout.fillHeight: true

        ColumnLayout {
            anchors.fill: parent
            spacing: 0

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 48

                TabBar {
                    width: parent.width
                    height: parent.height

                    TabButton {
                        text: qsTr("Welcome")
                    }

                    TabButton {
                        text: qsTr("Location")
                    }

                    TabButton {
                        text: qsTr("Finish")
                    }

                }

            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true

                StackView {
                    anchors.fill: parent
                    initialItem: welcomeComp

                    Component.onCompleted: {
                        stack = this
                    }

                }
            }

        }

    }

}
