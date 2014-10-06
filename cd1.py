# -*- coding: UTF-8 -*-
# Copyright 2014 ClockWorkJar <frinksdev@gmail.com,elduendedcm_02@hotmail.com>
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import wx

try:
    import wx
    import serial
    import time as tm
    from datetime import *
    import thread
    import gettext
    import matplotlib.pyplot as ptl
    from dateutil.parser import parse

except:
    print"Faltan librerias, puedes contactar a soporte <frinksdev@gmail.com>"

class cd1(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.ICONIZE | wx.CAPTION | wx.MINIMIZE | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Dunamis"))
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Iniciar Captura"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Detener Captura"))
        self.button_3 = wx.Button(self, wx.ID_ANY, _("Generar Grafica"))
        self.button_4 = wx.Button(self, wx.ID_ANY, _("Guardar Datos"))
        self.button_5 = wx.Button(self, wx.ID_ANY, _("Prender Bomba"))
        self.button_6 = wx.Button(self, wx.ID_ANY, _("Apagar Bomba"))
        self.arduino="o"
        self.bucle=False
        self.temp=[]
        self.humedad=[]

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_cap, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.on_det, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.on_gfx, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.on_data, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.on_bomb, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.on_dbomb, self.button_6)

    def __set_properties(self):
        self.SetTitle(_("Capturador Dunamis"))
        self.label_1.SetForegroundColour(wx.Colour(0, 255, 127))
        self.label_1.SetFont(wx.Font(72, wx.DEFAULT, wx.ITALIC, wx.BOLD, 0, ""))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.button_1, 0, 0, 0)
        sizer_2.Add(self.button_2, 0, 0, 0)
        sizer_2.Add(self.button_3, 0, 0, 0)
        sizer_2.Add(self.button_4, 0, 0, 0)
        sizer_2.Add(self.button_5, 0, 0, 0)
        sizer_2.Add(self.button_6, 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()

        box=wx.TextEntryDialog(None,"Ingresar Ubicacion de Dispositivo\n Copyright 2014 Francisco Ortega <frinksdev@gmail.com>\n Creado para Dunamis Empresarial","Dunamis","Ingrese Ubiacion de dispostivo")
        if box.ShowModal()==wx.ID_OK:
            self.arduino=box.GetValue()

        self.serial=serial.Serial(self.arduino,baudrate=9600,timeout=1.0)

    def captura(self):
        self.bucle=True
        while self.bucle!=False:
            #hora=str(datet ime.now().time())
            #if hora>="23:59:59.000000" or hora >="11:59:59.000000":
                dia=date.today()
                dia_n=dia.strftime("%Y-%m-%d")
                print dia_n
                self.serial.write('A')
                line1=float(self.serial.readline())
                print(line1)
                self.temp.append(line1)
                tm.sleep(5)
                self.serial.write('B')
                line2=float(self.serial.readline())
                print(line2)
                self.humedad.append(line2)
                tm.sleep(5)

    def bomba(self):
        self.bucle=True
        while self.bucle!=False:
            self.serial.write('I')

        self.serial.write('O')

    def on_cap(self, event):  
        t1=thread.start_new_thread(self.captura, ())

    def on_det(self, event):  
        self.bucle=False
        print self.temp, self.humedad

    def on_gfx(self, event):  
        ptl.ion
        ptl.figure('Grafica Dunamiss')
        ptl.suptitle('Temperatura     /     Humedad')
        ptl.subplot(1,2,1)
        ptl.plot(self.temp,'g*-')
        ptl.subplot(1,2,2)
        ptl.plot(self.humedad,'r--')
        ptl.show()

    def on_data(self, event):  
        dia=date.today()
        dia_n=dia.strftime("%Y-%m-%d")
        ptl.ion
        ptl.figure('Grafica Dunamiss')
        ptl.suptitle('Temperatura     /     Humedad')
        ptl.subplot(1,2,1)
        ptl.plot(self.temp,'g*-')
        ptl.subplot(1,2,2)
        ptl.plot(self.humedad,'r--')
        imgg=dia_n+'.png'
        str(imgg)
        ptl.savefig(imgg)

    def on_bomb(self, event):  
        tb=thread.start_new_thread(self.bomba, ())

    def on_dbomb(self, event):  
        self.bucle=False
        print "Bomba apagada"

