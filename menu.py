from PyQt5.QtWidgets import *

def menu():
    window = QDialog()
    main_line = QVBoxLayout()

    quest_lbl = QLabel("Запитання")
    quest_ledt = QLineEdit()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_ledt)
    main_line.addLayout(h1)


    right_lbl = QLabel("Правильна відповідь")
    right_ledt = QLineEdit()

    h2 = QHBoxLayout()
    h2.addWidget(rignt_lbl)
    h2.addWidget(rignt_ledit)
    main_line.addLayout(h2)


    false1_lbl = QLabel("Не правильна відповідь")
    felse1_ledt = QLineEdit()

    h3 = QHBoxLayout()
    h3.addWidget(rignt_lbl)
    h3.addWidget(rignt_ledit)
    main_line.addLayout(h2)

    false2_lbl = QLabel("Не правильна відповідь")
    felse2_ledt = QLineEdit()

    h4 = QHBoxLayout()
    h4addWidget(rignt_lbl)
    h4.addWidget(rignt_ledit)
    main_line.addLayout(h2)


    false3_lbl = QLabel("Не правильна відповідь")
    felse3_ledt = QLineEdit()

    h5 = QHBoxLayout()
    h5.addWidget(rignt_lbl)
    h5.addWidget(rignt_ledit)
    main_line.addLayout(h2)



    window.setLayout(main_line)
    window.exec()
