#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Fri Sep 12 19:50:05 2014
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from cd1 import cd1

class DunamisApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        cd1_frame = cd1(None, wx.ID_ANY, "")
        self.SetTopWindow(cd1_frame)
        cd1_frame.Show()
        return 1

# end of class DunamisApp

if __name__ == "__main__":
    gettext.install("MainDunamis") # replace with the appropriate catalog name

    MainDunamis = DunamisApp(0)
    MainDunamis.MainLoop()