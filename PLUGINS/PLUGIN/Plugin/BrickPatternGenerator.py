from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QSpinBox, QPushButton
import pymxs
import sys

rt = pymxs.runtime


if QApplication.instance():
    app = QApplication.instance()
    app.quit()
else:
    app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Brick Pattern Generator")
layout = QVBoxLayout()

label = QLabel("Choose your pattern")
layout.addWidget(label)


normal_pattern_radio = QRadioButton("Normal Pattern")
alt_pattern_radio = QRadioButton("Alternative Pattern")
normal_pattern_radio.setChecked(True)  # Set the default selection

# Group the radio buttons
pattern_group = QButtonGroup()
pattern_group.addButton(normal_pattern_radio)
pattern_group.addButton(alt_pattern_radio)

layout.addWidget(normal_pattern_radio)
layout.addWidget(alt_pattern_radio)

x_size_label = QLabel("Distance Between 2 Bricks in X axis")
x_size_spinbox = QSpinBox()
x_size_spinbox.setRange(0, 10)
x_size_spinbox.setValue(4)
layout.addWidget(x_size_label)
layout.addWidget(x_size_spinbox)

z_size_label = QLabel("Distance Between 2 Bricks in Z axis")
z_size_spinbox = QSpinBox()
z_size_spinbox.setRange(0, 10)
z_size_spinbox.setValue(2)
layout.addWidget(z_size_label)
layout.addWidget(z_size_spinbox)

x_box_label = QLabel("Number of Bricks in X Axis")
x_box_spinbox = QSpinBox()
x_box_spinbox.setRange(0, 10)
x_box_spinbox.setValue(5)
layout.addWidget(x_box_label)
layout.addWidget(x_box_spinbox)

z_box_label = QLabel("Number of Bricks in Z Axis")
z_box_spinbox = QSpinBox()
z_box_spinbox.setRange(0, 10)
z_box_spinbox.setValue(5)
layout.addWidget(z_box_label)
layout.addWidget(z_box_spinbox)

execute_button = QPushButton("Execute!")
layout.addWidget(execute_button)

window.setLayout(layout)

def execute_normal_pattern():
    x_size = x_size_spinbox.value()
    z_size = z_size_spinbox.value()
    x_box = x_box_spinbox.value() - 1
    z_box = z_box_spinbox.value() - 1
    
    rt.delete(rt.objects)
    
    for x in range(x_box + 1):
        for z in range(z_box + 1):
            pos = rt.point3(x * x_size, 0, z * z_size)
            brick = rt.box(length=2, width=4, height=1.5, pos=pos)
            chamfer_mod = rt.Chamfer(amount=0.15)
            rt.addModifier(brick, chamfer_mod)
            
            
            rt.convertToPoly(brick)

def execute_alternative_pattern():
    x_size = x_size_spinbox.value()
    z_size = z_size_spinbox.value()
    x_box = x_box_spinbox.value() - 1
    z_box = z_box_spinbox.value() - 1
    
    rt.delete(rt.objects)
    
    for x in range(x_box + 1):
        for z in range(z_box + 1):
            if z % 2 == 0:
                offset = 0
            else:
                offset = x_size / 2
            pos = rt.point3(x * x_size + offset, 0, z * z_size)
            brick = rt.box(length=2, width=4, height=1.5, pos=pos)
            chamfer_mod = rt.Chamfer(amount=0.15)
            rt.addModifier(brick, chamfer_mod)
            
            
            rt.convertToPoly(brick)

def on_execute():
    if normal_pattern_radio.isChecked():
        execute_normal_pattern()
    elif alt_pattern_radio.isChecked():
        execute_alternative_pattern()

execute_button.clicked.connect(on_execute)

window.show()

app.exec_()


app.quit()
