# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LDMPDownload
                                 A QGIS plugin
 This plugin supports monitoring and reporting of land degradation to the UNCCD and in support of the SDG Land Degradation Neutrality (LDN) target
                             -------------------
        begin                : 2017-05-23
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Conservation International
        email                : GEF-LDMP@conservation.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic

from .ui.ui_DlgDownload import Ui_DlgDownload as UiDialog

class DlgDownload(QtGui.QDialog, UiDialog):
    def __init__(self, parent=None):
        """Constructor."""
        super(DlgDownload, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
