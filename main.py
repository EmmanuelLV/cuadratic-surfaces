# -*- coding: utf-8 -*-
import wx
import wx.grid as gridlib
import os

########################################################################
class MainPane(wx.Panel):

#------------------------------Events----------------------------------------
    def on_click_paraboloid_hiperbolic(self,event):
        print("Presionaste Paraboloid_hiperbolic")
        frame.on_Change_screen(opt = 1)

    def on_click_paraboloid(self,event):
      print("Presionaste paraboloid")
      frame.on_Change_screen(opt = 2)

    def on_click_hiperboloid(self,event):
      print("Presionaste hiperboloid")
      frame.on_Change_screen(opt = 3)

    def on_click_ellipsoid(self,event):
      print("Presionaste ellipsoid")
      frame.on_Change_screen(opt = 4)

    def on_click_cone(self,event):
      print("Presionaste cone")
      frame.on_Change_screen(opt = 5)

    def on_click_acerca_de(self,event):
        print("About")
        frame.on_Change_screen(opt = 6)

#----------------------------------------------------------------------
    def __init__(self, parent):
#------------------------------panel----------------------------------------
        wx.Panel.__init__(self, parent=parent)
        #Button paraboloid_hiperbolic
        bmp = wx.Bitmap("imge\\paraboloid_hiperbolic.png", wx.BITMAP_TYPE_ANY)
        btnParaboloid_hiperbolic = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                               pos=wx.Point(10, 10),size=(bmp.GetWidth(), bmp.GetHeight()))
        btnParaboloid_hiperbolic.Bind(wx.EVT_BUTTON, self.on_click_paraboloid_hiperbolic)
        lblParaboloid_hiperbolic = wx.StaticText(self, id=wx.ID_ANY, label="Paraboloide hiperbolico", pos=wx.Point(12, 155),
                   style=0, name=wx.StaticTextNameStr)


       #Button paraboloid
        bmp = wx.Bitmap("imge\\paraboloid.png", wx.BITMAP_TYPE_ANY)
        btnParaboloid = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                                  pos=wx.Point(170, 10),size=(bmp.GetWidth(), bmp.GetHeight()+10))
        btnParaboloid.Bind(wx.EVT_BUTTON, self.on_click_paraboloid)
        lblparaboloid = wx.StaticText(self, id=wx.ID_ANY, label="Paraboloide", pos=wx.Point(175, 155),
                   style=0, name=wx.StaticTextNameStr)


       #Button hiperboloid
        bmp = wx.Bitmap("imge\\hiperboloid.png", wx.BITMAP_TYPE_ANY)
        btnHiperboloid = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                                  pos=wx.Point(330, 10),size=(bmp.GetWidth(), bmp.GetHeight()))
        btnHiperboloid.Bind(wx.EVT_BUTTON, self.on_click_hiperboloid)
        lblhiperboloid = wx.StaticText(self, id=wx.ID_ANY, label="Hiperboloide", pos=wx.Point(335, 155),
                   style=0, name=wx.StaticTextNameStr)


       #Button ellipsoid
        bmp = wx.Bitmap("imge\\ellipsoid.png", wx.BITMAP_TYPE_ANY)
        btnEllipsoid = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                                  pos=wx.Point(490, 10),size=(bmp.GetWidth(), bmp.GetHeight()+10))
        btnEllipsoid.Bind(wx.EVT_BUTTON, self.on_click_ellipsoid)
        lblEllipsoid = wx.StaticText(self, id=wx.ID_ANY, label="Elipsoide", pos=wx.Point(495, 155),
                   style=0, name=wx.StaticTextNameStr)


       #Button cone
        bmp = wx.Bitmap("imge\\cone.png", wx.BITMAP_TYPE_ANY)
        btnCone = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                                  pos=wx.Point(10, 190),size=(bmp.GetWidth(), bmp.GetHeight()))
        btnCone.Bind(wx.EVT_BUTTON, self.on_click_cone)
        lblCone = wx.StaticText(self, id=wx.ID_ANY, label="Cono", pos=wx.Point(15, 340),
                   style=0, name=wx.StaticTextNameStr)

        bmp = wx.Bitmap("imge\\icon-36.png", wx.BITMAP_TYPE_ANY)
        btnAcerca_de = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                                  pos=wx.Point(0, 425),size=(bmp.GetWidth(), bmp.GetHeight()))
        btnAcerca_de.Bind(wx.EVT_BUTTON, self.on_click_acerca_de)
        lblAcerca = wx.StaticText(self, id=wx.ID_ANY, label="Acerca de", pos=wx.Point(40, 435),
                   style=0, name=wx.StaticTextNameStr)

########################################################################
class paraboloid_hiperbolicPanel(wx.Panel):#paraboloid_hiperbolic
      #------------------------------Eventos---------------------------------------
    def on_click_graficar(self,event):
        os.system("python superficies/paraboloid_hiperbolic.py")

    def on_click_back(self,event):
        frame.SetSize(0,0,700,500)
        frame.on_Change_screen(opt = 7)
      #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        label = "El Paraboloide Hiperbólico también se lo conoce bajo los nombres \n silla de montar o paso de montaña por su conformación geométrica,\n es una superficie que en una dirección tiene las secciones en \n de parábola con los lados hacia arriba y, en la sección perpendicular,\n secciones son en forma de parábola con los lados hacia abajo.\n puede simplificar el concepto afirmando que es un plano alabeado. \nUn paraboloide será hiperbólico cuando los términos cuadráticos \nde su canónica sean de signo contrario:\n\n\t\t( (x/2)^2 ) - ( (y/b)^2 ) - z = 0"
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        lblParaboloid_hiperbolic = wx.StaticText(self, id=wx.ID_ANY, label=label, pos=wx.Point(15, 10),
                    style=0, name=wx.StaticTextNameStr)
        lblParaboloid_hiperbolic.SetFont(font)

        bmp = wx.Bitmap("imge\\paraboloid_hiperbolicinfo.png", wx.BITMAP_TYPE_ANY)
        btnEllipsoid = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                          pos=wx.Point(233, 280),size=(bmp.GetWidth(), bmp.GetHeight()))


        btnGraficar  = wx.Button(self, id=wx.ID_ANY, label="Graficar", pos= wx.Point(466, 300),
                size=wx.Size(100, 100), style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnGraficar.Bind(wx.EVT_BUTTON, self.on_click_graficar)

        btnback  = wx.Button(self, id=wx.ID_ANY, label="Regresar", pos=wx.Point(0, 430),
                size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnback.Bind(wx.EVT_BUTTON, self.on_click_back)

        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Despeje = "asdlasdlasmdkasdaskmdklasmdasda \n sadaskdioj"
        text=wx.StaticText(self, label=Despeje, pos=wx.Point(700, 10))
        text.SetFont(font)
        text.SetBackgroundColour((255,255,255)) # set text back color


########################################################################
class paraboloidPanel(wx.Panel):#paraboloid
    """"""
    def on_click_graficar(self,event):
        os.system("python superficies/paraboloide_eliptico.py")

    def on_click_back(self,event):
        frame.SetSize(0,0,700,500)
        frame.on_Change_screen(opt = 7)
      #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        label = "Paraboloide elíptico. Es la superficie que se ha creado al deslizar\nuna parábola vertical con la concavidad hacia abajo, a lo largo de\n la otra, perpendicular a la primera; las secciones horizontales son\nla otra, perpendicular a la primera; las secciones horizontales son\nelipses mientras que las verticales son parábolas\nSe denomina Paraboloide Elíptico a la superficie que en un sistema\nde coordenadas cartesianos se determina por la ecuación:\n\n\t\t( x^2/a^2 ) + ( y^2/b^2 ) = z"
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        lblParaboloid_hiperbolic = wx.StaticText(self, id=wx.ID_ANY, label=label, pos=wx.Point(15, 10),
                    style=0, name=wx.StaticTextNameStr)
        lblParaboloid_hiperbolic.SetFont(font)
        bmp = wx.Bitmap("imge\\Paraboloide_hiperbolico.jpg", wx.BITMAP_TYPE_ANY)
        btnEllipsoid = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                          pos=wx.Point(233, 280),size=(bmp.GetWidth(), bmp.GetHeight()))

        btnGraficar  = wx.Button(self, id=wx.ID_ANY, label="Graficar", pos= wx.Point(466, 300),
                size=wx.Size(100, 100), style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnGraficar.Bind(wx.EVT_BUTTON, self.on_click_graficar)

        btnback  = wx.Button(self, id=wx.ID_ANY, label="Regresar", pos=wx.Point(0, 430),
                size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnback.Bind(wx.EVT_BUTTON, self.on_click_back)

        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Despeje = "asdlasdlasmdkasdaskmdklasmdasda \n sadaskdioj"
        text=wx.StaticText(self, label=Despeje, pos=wx.Point(700, 10))
        text.SetFont(font)
        text.SetBackgroundColour((255,255,255)) # set text back color


########################################################################
class hiperboloidPanel(wx.Panel):#paraboloid
    """"""
    def on_click_graficar_una_hoja(self,event):
        os.system("python superficies/hiperbole.py")

    def on_click_graficar_dos_hojas(self,event):
        os.system("python superficies/hiperbole_two_sheet.py")

    def on_click_back(self,event):
        frame.SetSize(0,0,700,500)
        frame.on_Change_screen(opt = 7)
      #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)


        label = "La Hiperboloide es la superficie de revolución generada por la\nrotación de una hipérbola alrededor de uno de sus dos ejes de\nsimetría. Estas superficies son de dos clases: de una y de dos hojas\nEs la superficie que se engendra al deslizar un segmento inclinado\n sobre dos círculos horizontales y se expresa en un sistema \nde coordenadas cartesiano mediante la fórmula:\nHiperboloide de una hoja:\n\n\t\t( (x/a)^2 ) + ( (y/b)^2 ) - ( (z/c)^2 ) = 1\n\nHiperboloide de dos hojas:\n\n\t\t( (z/c)^2 ) - (x/a)^2 ) - ( (y/b)^2 ) = 1"

        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        lblParaboloid_hiperbolic = wx.StaticText(self, id=wx.ID_ANY, label=label, pos=wx.Point(15, 10),
                    style=0, name=wx.StaticTextNameStr)
        lblParaboloid_hiperbolic.SetFont(font)

        btnGraficar  = wx.Button(self, id=wx.ID_ANY, label="Graficar (una hoja)", pos= wx.Point(180, 380),
                size=wx.Size(120, 50), style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnGraficar.Bind(wx.EVT_BUTTON, self.on_click_graficar_una_hoja)

        btnGraficard  = wx.Button(self, id=wx.ID_ANY, label="Graficar (dos hojas)", pos= wx.Point(320, 380),
                size=wx.Size(120, 50), style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnGraficard.Bind(wx.EVT_BUTTON, self.on_click_graficar_dos_hojas)

        btnback  = wx.Button(self, id=wx.ID_ANY, label="Regresar", pos=wx.Point(0, 430),
                size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnback.Bind(wx.EVT_BUTTON, self.on_click_back)

        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Despeje = "asdlasdlasmdkasdaskmdklasmdasda \n sadaskdioj"
        text=wx.StaticText(self, label=Despeje, pos=wx.Point(700, 10))
        text.SetFont(font)
        text.SetBackgroundColour((255,255,255)) # set text back color



########################################################################
class ellipsoidPanel(wx.Panel):#paraboloid
    """"""
    def on_click_graficar(self,event):
        os.system("python superficies/ellipsoid.py")

    def on_click_back(self,event):
        frame.SetSize(0,0,700,500)
        frame.on_Change_screen(opt = 7)
      #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        label = "Elipsoide. Es una superficie curva cerrada cuyas tres secciones \nortogonales principales son elípticas, es decir, son originadas\npor planos que contienen dos ejes cartesianos.Formula general :\n\n\t\t(x/a)^2 - (y/b)^2  - (z/c)^2 = 1"
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        lblParaboloid_hiperbolic = wx.StaticText(self, id=wx.ID_ANY, label=label, pos=wx.Point(15, 10),
                    style=0, name=wx.StaticTextNameStr)
        lblParaboloid_hiperbolic.SetFont(font)
        bmp = wx.Bitmap("imge\\ellipsoid_info.png", wx.BITMAP_TYPE_ANY)
        btnEllipsoid = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                          pos=wx.Point(233, 280),size=(bmp.GetWidth(), bmp.GetHeight()))

        btnGraficar  = wx.Button(self, id=wx.ID_ANY, label="Graficar", pos= wx.Point(466, 300),
                size=wx.Size(100, 100), style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnGraficar.Bind(wx.EVT_BUTTON, self.on_click_graficar)

        btnback  = wx.Button(self, id=wx.ID_ANY, label="Regresar", pos=wx.Point(0, 430),
                size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnback.Bind(wx.EVT_BUTTON, self.on_click_back)

        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Despeje = "asdlasdlasmdkasdaskmdklasmdasda \n sadaskdioj"
        Despeje = "1)Igualar la forma general a 1 \n (x/a)^2 - (y/b)^2  - (z/c)^2 = 1\n2)Reducir términos\n3)Dar valor 0 a z(plano xy)\n(x/a)^2 - (y/b)^2 = 1\n4)Eliminamos x\n(x/a)^2 = 1\n*calcular valores posibles\n5)Similar al punto 4 ahora con y\n(y/b)^2 = 1\n*calcular valores posibles\n6)ahora con z\n(z/c)^2 = 1\n*calcular valores posibles"
        text=wx.StaticText(self, label=Despeje, pos=wx.Point(700, 10))
        text.SetFont(font)
        text.SetBackgroundColour((255,255,255)) # set text back color


########################################################################
class conePanel(wx.Panel):#paraboloid
    """"""
    def on_click_graficar(self,event):
        os.system("python superficies/cone.py")

    def on_click_back(self,event):
        frame.SetSize(0,0,700,500)
        frame.on_Change_screen(opt = 7)
      #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)


        label = "Un cono es una pirámide con una sección transveersal cicular.\n Un cono derecho es un cono con su vértice sobre el centro de su\nbase. La palabra cono significa doble cono, es decir dos conos\n colocados en el vértice del ápice, el doble cono es una\n superficie cuadática y cada cono individual se llama nappe"

        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        lblParaboloid_hiperbolic = wx.StaticText(self, id=wx.ID_ANY, label=label, pos=wx.Point(15, 10),
                    style=0, name=wx.StaticTextNameStr)
        lblParaboloid_hiperbolic.SetFont(font)
        bmp = wx.Bitmap("imge\\cone.png", wx.BITMAP_TYPE_ANY)
        btnEllipsoid = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                          pos=wx.Point(233, 280),size=(bmp.GetWidth(), bmp.GetHeight()))

        btnGraficar  = wx.Button(self, id=wx.ID_ANY, label="Graficar", pos= wx.Point(466, 300),
                size=wx.Size(100, 100), style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnGraficar.Bind(wx.EVT_BUTTON, self.on_click_graficar)

        btnback  = wx.Button(self, id=wx.ID_ANY, label="Regresar", pos=wx.Point(0, 430),
                size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnback.Bind(wx.EVT_BUTTON, self.on_click_back)

        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Despeje = "1)Forma general, igualar x a 0\n   ( (z/c)^2 ) = ( (y/b)^2 )\n2)Despejar z\n z=+- y\n3) ahora igualar z a 0\nx^2=y^2\n4)Despejamos y\n y^2=(a/b)x^2\n5)Igualamos y a 0\n ax^2+by^2=0\n6)Busar la forma general\n(x/a)^2+(y/b)^2=0\n7)Dar valor (arbitrario) a y\nax^2+cz^2=b(y^2)\nIgualar a 1 y calcular \nlos valores posibles"
        text=wx.StaticText(self, label=Despeje, pos=wx.Point(700, 10))
        text.SetFont(font)
        text.SetBackgroundColour((255,255,255)) # set text back color


########################################################################
class acerca_dePanel(wx.Panel):#paraboloid
    """"""
    def on_click_back(self,event):
        frame.SetSize(0,0,700,500)
        frame.on_Change_screen(opt = 7)
      #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.SetBackgroundColour((255,255,255))
        label = "\nSoftware desarrollado por:"
        font = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        lblParaboloid_hiperbolic = wx.StaticText(self, id=wx.ID_ANY, label=label, pos=wx.Point(15, 10),
                    style=0, name=wx.StaticTextNameStr)
        lblParaboloid_hiperbolic.SetFont(font)

        bmp = wx.Bitmap("imge\\Emma.png", wx.BITMAP_TYPE_ANY)
        btnEllipsoid = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                          pos=wx.Point(100, 100),size=(bmp.GetWidth(), bmp.GetHeight()))

        bmp = wx.Bitmap("imge\\Profile.jpg", wx.BITMAP_TYPE_ANY)
        btnYo = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp,
                          pos=wx.Point(240, 280),size=(bmp.GetWidth(), bmp.GetHeight()))

        btnback  = wx.Button(self, id=wx.ID_ANY, label="Regresar", pos=wx.Point(0, 430),
                size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,name=wx.ButtonNameStr)
        btnback.Bind(wx.EVT_BUTTON, self.on_click_back)

        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Despeje = "asdlasdlasmdkasdaskmdklasmdasda \n sadaskdioj"
        text=wx.StaticText(self, label=Despeje, pos=wx.Point(700, 10))
        text.SetFont(font)
        text.SetBackgroundColour((255,255,255)) # set text back color


########################################################################



class MyForm(wx.Frame):

#------------------------------panel----------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "Examen")
        self.SetSize(0,0,700,500)

        self.main_panel = MainPane(self)
        self.paraboloid_hiperbolicPanel = paraboloid_hiperbolicPanel(self)
        self.paraboloidPanel = paraboloidPanel(self)
        self.conePanel = conePanel(self)
        self.ellipsoidPanel = ellipsoidPanel(self)
        self.hiperboloidPanel = hiperboloidPanel(self)
        self.paraboloidPanel = paraboloidPanel(self)
        self.acerca_dePanel = acerca_dePanel(self)

        self.paraboloid_hiperbolicPanel.Hide()
        self.conePanel.Hide()
        self.ellipsoidPanel.Hide()
        self.hiperboloidPanel.Hide()
        self.paraboloidPanel.Hide()
        self.acerca_dePanel.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.main_panel, 1, wx.EXPAND)
        self.sizer.Add(self.paraboloid_hiperbolicPanel, 1, wx.EXPAND)
        self.sizer.Add(self.ellipsoidPanel, 1, wx.EXPAND)
        self.sizer.Add(self.hiperboloidPanel, 1, wx.EXPAND)
        self.sizer.Add(self.paraboloidPanel, 1, wx.EXPAND)
        self.sizer.Add(self.conePanel, 1, wx.EXPAND)
        self.sizer.Add(self.acerca_dePanel, 1, wx.EXPAND)

        self.SetSizer(self.sizer)

        #self.on_Change_screen(opt = 1)
       #-----------------------------Function-----------------------------------------
    def on_Change_screen(self,opt):
        """"""
        if opt == 1:
            print("IsShown")
            self.SetTitle("Paraboloide hiperbólico")
            self.main_panel.Hide()
            self.paraboloid_hiperbolicPanel.Show()
            frame.SetSize(0,0,1000,500)
        if opt == 2:
            print("IsShown")
            self.SetTitle("Paraboloide eliptico")
            self.main_panel.Hide()
            self.paraboloidPanel.Show()
            frame.SetSize(0,0,1000,500)
        if opt == 3:
            print("IsShown")
            self.SetTitle("Hiperboloide")
            self.main_panel.Hide()
            self.hiperboloidPanel.Show()
            frame.SetSize(0,0,1000,500)
        if opt == 4:
            print("IsShown")
            self.SetTitle("Elipsoide")
            self.main_panel.Hide()
            self.ellipsoidPanel.Show()
            frame.SetSize(0,0,1000,500)
        if opt == 5:
            print("IsShown")
            self.SetTitle("Cono")
            self.main_panel.Hide()
            self.conePanel.Show()
            frame.SetSize(0,0,1000,500)
        if opt == 6:
            print("IsShown")
            self.SetTitle("Acerca de")
            self.main_panel.Hide()
            self.acerca_dePanel.Show()
            frame.SetSize(0,0,700,500)

        if opt == 7:
            self.SetTitle("Supercies cuadráticas")
            self.main_panel.Show()
            self.paraboloid_hiperbolicPanel.Hide()
            self.conePanel.Hide()
            self.ellipsoidPanel.Hide()
            self.hiperboloidPanel.Hide()
            self.paraboloidPanel.Hide()
            frame.SetSize(0,0,700,500)
        self.Layout()

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
