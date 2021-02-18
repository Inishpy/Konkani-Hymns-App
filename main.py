#I import all the modules that i need, from kivy and kivymd packages
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, ShaderTransition, SwapTransition
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image, AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.core.text import LabelBase
from kivy.uix.label import  Label
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.navigationdrawer import NavigationLayout, MDNavigationDrawer
from kivymd.uix.list import TwoLineIconListItem,IRightBodyTouch,MDIconButton, IconLeftWidget,IconRightWidget, MDList,TwoLineIconListItem, MDCheckbox
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.button import MDFloatingActionButton

# text module has a  dictionary with key as hyms number and value is string which is nothing but hymn itself
    #its copyrighted so I cant upload it here
from text import A # you better comment out this .

#I am using sqlite3  package for the database to  save the hymn data
import sqlite3 

# this module is for directing to my social media handles
import webbrowser  as wb



#I need to register the konkani font used in the app
LabelBase.register(name="kannada_mallige", fn_regular='Nudi 01 e.ttf', fn_bold='Nudi 01 e b.ttf')

X = {"A": 79,  "B": 27, "C": 80, "D": 92, "E": 43, "F": 18, "G": 2, "H": 42, "I": 12,"J": 29, "K": 9, "L": 13, "M": 11, "N": 12, "O": 70, "P": 33, "Q": 10, "R": 40, "S": 26, "T": 6, "U": 47, "V": 13}

#I could have used the loop to this list, infact I did use it and copied the output here, I forget the reason
labels = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30', 'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A50', 'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57', 'A58', 'A59', 'A60', 'A61', 'A62', 'A63', 'A64', 'A65', 'A66', 'A67', 'A68', 'A69', 'A70', 'A71', 'A72', 'A73', 'A74', 'A75', 'A76', 'A77', 'A78', 'A79', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64', 'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73', 'C74', 'C75', 'C76', 'C77', 'C78', 'C79', 'C80', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37', 'D38', 'D39', 'D40', 'D41', 'D42', 'D43', 'D44', 'D45', 'D46', 'D47', 'D48', 'D49', 'D50', 'D51', 'D52', 'D53', 'D54', 'D55', 'D56', 'D57', 'D58', 'D59', 'D60', 'D61', 'D62', 'D63', 'D64', 'D65', 'D66', 'D67', 'D68', 'D69', 'D70', 'D71', 'D72', 'D73', 'D74', 'D75', 'D76', 'D77', 'D78', 'D79', 'D80', 'D81', 'D82', 'D83', 'D84', 'D85', 'D86', 'D87', 'D88', 'D89', 'D90', 'D91', 'D92', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27', 'E28', 'E29', 'E30', 'E31', 'E32', 'E33', 'E34', 'E35', 'E36', 'E37', 'E38', 'E39', 'E40', 'E41', 'E42', 'E43', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'G1', 'G2', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23', 'H24', 'H25', 'H26', 'H27', 'H28', 'H29', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'H36', 'H37', 'H38', 'H39', 'H40', 'H41', 'H42', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20', 'J21', 'J22', 'J23', 'J24', 'J25', 'J26', 'J27', 'J28', 'J29', 'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11', 'O12', 'O13', 'O14', 'O15', 'O16', 'O17', 'O18', 'O19', 'O20', 'O21', 'O22', 'O23', 'O24', 'O25', 'O26', 'O27', 'O28', 'O29', 'O30', 'O31', 'O32', 'O33', 'O34', 'O35', 'O36', 'O37', 'O38', 'O39', 'O40', 'O41', 'O42', 'O43', 'O44', 'O45', 'O46', 'O47', 'O48', 'O49', 'O50', 'O51', 'O52', 'O53', 'O54', 'O55', 'O56', 'O57', 'O58', 'O59', 'O60', 'O61', 'O62', 'O63', 'O64', 'O65', 'O66', 'O67', 'O68', 'O69', 'O70', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19', 'R20', 'R21', 'R22', 'R23', 'R24', 'R25', 'R26', 'R27', 'R28', 'R29', 'R30', 'R31', 'R32', 'R33', 'R34', 'R35', 'R36', 'R37', 'R38', 'R39', 'R40', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9', 'U10', 'U11', 'U12', 'U13', 'U14', 'U15', 'U16', 'U17', 'U18', 'U19', 'U20', 'U21', 'U22', 'U23', 'U24', 'U25', 'U26', 'U27', 'U28', 'U29', 'U30', 'U31', 'U32', 'U33', 'U34', 'U35', 'U36', 'U37', 'U38', 'U39', 'U40', 'U41', 'U42', 'U43', 'U44', 'U45', 'U46', 'U47', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13']


#this class can be used for customising the screen manager class, I did not customise here anything
class AppScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)




#this is the class for Main_navigation_screen
class Mainnavscreen(Screen):
    def __init__(self, **kwargs):
        super(Mainnavscreen, self).__init__(**kwargs)
        
        global Mdnavigationdrawer
        navigationLayout = NavigationLayout()
        Containor = ScreenManager()
        Containor.add_widget(Main())
        navigationLayout.add_widget(Containor)
        
        Mdnavigationdrawer = MDNavigationDrawer()
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(background_normal="Pictures/banner.webp",size_hint=(1, None), size=(0, Window.height*0.5)))
        Drawer_list = {"star":"Starred","settings": "Settings","bookmark":"Rate & Share"} 
        for i,j in Drawer_list.items():
            Item = TwoLineIconListItem(text=str(j))
            Item.add_widget(IconLeftWidget(icon=str(i)))
            Item.bind(on_release=self.list_action)
            box.add_widget(Item)
        box.add_widget(ScrollView())
        Mdnavigationdrawer.add_widget(box)
        
        navigationLayout.add_widget(Mdnavigationdrawer)
        
        self.add_widget(navigationLayout)
    def list_action(self, obj):
        if obj.text == "Starred":
            Containor.add_widget(Starred(name="starred"))
            Containor.current = "starred"
                                                    
        elif obj.text == "Settings":
            Containor.add_widget(setting(name="settings"))
            Containor.current = "settings"

        elif obj.text == "Index":
            snack_bar_index().show()




        
##database to store the starred  hymns                                 
conn = sqlite3.connect('star.db')
c = conn.cursor()

c.execute('''Create TABLE if not exists star('list')''')
Star= []
c.execute("SELECT * FROM star")
rows = c.fetchall()
for row in rows:
    #print(row)
    Star.append(str(row[0]))
conn.close()
def star():
    
    conn = sqlite3.connect('star.db')
    c = conn.cursor()
    c.execute("DELETE FROM star")
    for i in Star:
        c.execute("INSERT INTO star(list) VALUES(?)", [i])
    conn.commit()
    conn.close()
##databse code end






#this is the class for screen where you could find your starred hymns
class Starred(Screen):
    
    def __init__(self, **kwargs):
        super(Starred, self).__init__(**kwargs)
        
        view = ScrollView()
        layout = GridLayout(cols=1, padding=Window.height*0.01,spacing=Window.height*0.01, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        
        for i in Star:
            letter = i
            if len(letter) == 2:
                z = str(letter[0])+'.'+str(letter[1])
                y = str(letter[0])+'.'+str(int(letter[1])+1)
            elif len(letter) == 3:
                z = str(letter[0])+'.'+str(letter[1])+str(letter[2])
                y = str(letter[0])+'.'+str(int(str(letter[1])+str(letter[2]))+1)
            string = A.split(z)[1].split(y)[0]
            string1 = []
            for i in string:
                if i != '\t':
                    string1.append(i)   
            a = ''.join(string1)
            
            
            
            x = []
            for i in range(len(a)):
                if a[i].isdecimal() and a[i+1] != ')':
                    x.append('\n'+a[i])
                else:
                    x.append(a[i])
            x = ''.join(x)

            m = x.split('\n')
            x = '\n'.join(m[0:6])
            m = x.split('\n')
            n = []
            j = 0
            for i in m:
                if len(i) >= j:
                    j = len(i)

            size_y = Window.height*0.05*(len(m))
            size_x = j*Window.height*0.042/2.25
            if Window.width > size_x:
                size_x = Window.width
            btn = Button(id=letter, font_name="kannada_mallige",text="[font=Roboto-Bold][b][size="+str(int(Window.height*0.05))+']'+str(letter)+'. '+'[/size][/b][/font]'+x, size=(size_x, size_y), font_size=(Window.height*0.04),  text_size=(None, None),
                     markup=True,   background_color=(1,1,1,0), size_hint=(None, None), halign='left', valign = 'center', pos=(0, Window.height-100), color=(0,0,0,1))# valign = 'top')
            btn.bind(on_release=self.Screens_2)
            
            
            
            layout.add_widget(btn)
            

        
        view.add_widget(layout)

        box = BoxLayout(orientation='vertical')
        toolbar = TwoLineIconListItem(bg_color=(0, .588, .533,1))
        back_icon = IconLeftWidget(icon='arrow-left-thick')
        
        back_icon.bind(on_release=self.back)
        
        toolbar.add_widget(back_icon)
        
        box.add_widget(toolbar)
        
        box.add_widget(view)
        self.add_widget(box)

    def back(self, obj):
        Containor.current = Containor.screens[-2].name
        del Containor.screens[-1]
      

    def Screens_2(self, instant):
        Containor.add_widget(Main_2(letter = str(instant.id), name = str(instant.id)))
        Containor.current = str(instant.id)




#class for main screen Toolbar        
class Toolbar(MDToolbar):
    def __init__(self, **kwargs):
        super(Toolbar,self).__init__(**kwargs)
        self.pos = (0, Window.height-self.size[1])
        self.left_action_items = [["menu", self.drawer]]
        self.right_action_items = [["magnify", self.search]]
        self.elevation = 10
        
        
        

    def drawer(self, obj):
        Mdnavigationdrawer.set_state('open')

    def search(self, obj):
        if str(text_main.text.upper()) in labels:
            Containor.add_widget(Main_2(name = str(text_main.text.upper()),letter = str(text_main.text.upper())))
            Containor.current = str(text_main.text.upper())
        else:
            Snackbar(text="Invalid").show()



#variable to keep track wheather the textfield is focused or not
Focus = False





#class for main screen which will be added to screenManager            
class Main(Screen):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        
        view = ScrollView()
        layout = GridLayout(cols=2, padding=Window.height*0.015,spacing=Window.height*0.015, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        global Genre_buttons
        Genre_buttons = []
        for i in X.keys():
            
            button = Button(background_normal='Pictures/'+i+'.webp', size=(50, Window.height*0.3), size_hint=(1, None),text=str(i), color=(0,0,0,0))
            
            button.bind(on_release=self.snack_bar)
            Genre_buttons.append(button)
            layout.add_widget(button)

        
        view.add_widget(layout)
        

        box = BoxLayout(orientation='vertical', spacing=Window.height*0.01)
        T = Toolbar()
        box.add_widget(T)
        
        global text_main
        text_main = CTextInput(multiline=False, size=(0,Window.height*0.09), size_hint_x=1, size_hint_y=None, font_size=Window.height*0.08)
        text_main.bind(on_text_validate=self.on_text)
        
        
        box.add_widget(text_main)
        box.add_widget(view)
        self.add_widget(box)

    def on_text(self, obj):
    
        if str(text_main.text.upper()) in labels:
            Containor.add_widget(Main_2(name = str(text_main.text.upper()),letter = str(text_main.text.upper())))
            Containor.current = str(text_main.text.upper())
        else:
            Snackbar(text="Invalid").show()

    def search(self, obj):
        if str(obj.text.upper()) in labels:
            Containor.add_widget(Main_2(name = str(obj.text.upper()),letter = str(obj.text.upper())))
            
            
            Containor.current = str(obj.text.upper())
        else:
            Snackbar(text="Invalid").show()


    def snack_bar(self, obj):
        loading = snack_bar(Letter=obj.text)
        loading.show()




#customised snackbar
class snack_bar(Snackbar):
    def __init__(self, Letter, **kwargs):
        super(snack_bar, self).__init__(**kwargs)
        self.text = "Loading "
        self.padding = Window.height*0.1
        self.Letter = Letter
        Clock.schedule_once(self.Screens_1, 0.3)

    def Screens_1(self, dt):
        Containor.add_widget(Main_1(Letter=str(self.Letter), name =str(self.Letter)))
        Containor.current = str(self.Letter)


#customised button
class Cbutton(Button):
    def __init__(self, lts, **kwargs):
        super(Cbutton, self).__init__(**kwargs)
        self.lts = lts


#class for second screen where the Letters of the Index are shown in tile format
class Main_1(Screen):
    
    def __init__(self, Letter, **kwargs):
        super(Main_1, self).__init__(**kwargs)
        if line == False:
            lines = 1
            sp = 0.015
        elif line == True:
            lines = 3
            sp = 0.02
        view = ScrollView()
        layout = GridLayout(cols=1, padding=Window.height*sp,spacing=Window.height*sp, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        
        for i in range(X[str(Letter)]):
            no = i
            letter = Letter+str(i+1)
            if len(letter) == 2:
                z = str(letter[0])+'.'+str(letter[1])
                y = str(letter[0])+'.'+str(int(letter[1])+1)
            elif len(letter) == 3:
                z = str(letter[0])+'.'+str(letter[1])+str(letter[2])
                y = str(letter[0])+'.'+str(int(str(letter[1])+str(letter[2]))+1)
            string = A.split(z)[1].split(y)[0]
            string1 = []
            for i in string:
                if i != '\t':
                    string1.append(i)   
            x = ''.join(string1)
            
            
            
            
            
            m = x.split('\n')
            x = '\n'.join(m[0:lines])
            m = x.split('\n')
            n = []
            j = 0
            for i in m:
                if len(i) >= j:
                    j = len(i)
            
            size_y = Window.height*0.05*(len(m))
            size_x = j*Window.height*0.042/2.25
            if Window.width > size_x:
                size_x = Window.width
            btn = Cbutton(lts=letter, font_name="kannada_mallige",text="[font=Roboto-Bold][b][size="+str(int(Window.height*0.05))+']'+str(letter)+'. '+'[/size][/b][/font]'+x+"[font=Roboto-Bold][b][size="+str(int(Window.height*0.05))+']'+' '+'[/size][/b][/font]',
                    bold=True,  markup=True, size=(size_x,size_y ), font_size=(Window.height*0.04), background_color=(1,1,1,0),
                        size_hint=(None, None), halign='left', valign = 'center', pos=(0, Window.height-100), color=(0,0,0,1))
            btn.bind(on_release=self.Screens_2)
        
            
            
            layout.add_widget(btn)
            
        view.add_widget(layout)

        box = BoxLayout(orientation='vertical')
        toolbar = TwoLineIconListItem(bg_color=(0, .588, .533,1))
        back_icon = IconLeftWidget(icon='arrow-left-thick')
        
        back_icon.bind(on_release=self.back)
        
        toolbar.add_widget(back_icon)
        
        box.add_widget(toolbar)
        
        box.add_widget(view)
        self.add_widget(box)

        
    def back(self, obj):
        Containor.current = Containor.screens[-2].name
        del Containor.screens[-1]
     

    def Screens_2(self, instant):
        
        Containor.add_widget(Main_2(letter = str(instant.lts), name = str(instant.lts)))
        Containor.current = str(instant.lts)



#variable to keep track wheather the text is bold or not
bold = False






#class for the screen where the hymn is displayed
class Main_2(Screen):
    def __init__(self, letter,**kwargs):
        super(Main_2, self).__init__(**kwargs)
        
        if len(letter) == 2:
            z = str(letter[0])+'.'+str(letter[1])
            y = str(letter[0])+'.'+str(int(letter[1])+1)
        elif len(letter) == 3:
            z = str(letter[0])+'.'+str(letter[1])+str(letter[2])
            y = str(letter[0])+'.'+str(int(str(letter[1])+str(letter[2]))+1)
        string = A.split(z)[1].split(y)[0]
        string1 = []
        for i in string:
            if i != '\t':
                string1.append(i)   
        a = ''.join(string1)
        
        boldness = bold
        
        x = []
        for i in range(len(a)):
                if a[i].isdecimal() and a[i+1] != ')':
                    x.append('\n'+a[i])
                else:
                    x.append(a[i])
        
        x = ''.join(x)

        m = x.split('\n')
        n = []
        j = 0
        for i in m:
            if len(i) >= j:
                j = len(i)
        size_y = Window.height*0.043*(len(m)+5)
        size_x = j*Window.height*0.045/2.25
        if Window.width > size_x:
            size_x = Window.width
        btn = Label(font_name="kannada_mallige",text="[font=Roboto-Bold][b][size="+str(int(Window.height*0.05))+']'+str(letter)+'. '+'[/size][/b][/font]'+x,
          size=(size_x,size_y ), font_size=(Window.height*0.04),  text_size=(None, None),
             bold=boldness,   markup=True,   size_hint=(None, None), halign='left', valign = 'top', color=(0,0,0,1))
        
        root = ScrollView(size_hint=(1, 1))
        root.add_widget(btn)
        box = BoxLayout(orientation='vertical')
        toolbar = TwoLineIconListItem(bg_color=(0, .588, .533,1))
        back_icon = IconLeftWidget(icon='arrow-left-thick')
       
        back_icon.bind(on_release=self.back)
        
        toolbar.add_widget(back_icon)
        
        box.add_widget(toolbar)
        box.add_widget(root)
        self.add_widget(box)
        
        star = MDIconButton(icon="star-outline",pos_hint={'right':1,'top':1})
        star.bind(on_release=self.bookmark)
        self.add_widget(star)

        
    def back(self, obj):
        Containor.current = Containor.screens[-2].name
        del Containor.screens[-1]

    def bookmark(self, obj):
        if Containor.current_screen.name not in Star:
            Star.append(Containor.current_screen.name)
            star()
            Snackbar(text=str(Containor.current_screen.name)+' is starred').show()
        else:
            Star.remove(Containor.current_screen.name)
            star()
            Snackbar(text=str(Containor.current_screen.name)+' is unstarred').show()






#variable to check keep track of lines need to been shown in the index page of the hymns
line = False

#settings page
class setting(Screen):
    def __init__(self,**kwargs):
        super(setting, self).__init__(**kwargs)
        box = BoxLayout(orientation="vertical")
        
        toolbar = TwoLineIconListItem(bg_color=(0, .588, .533,1))
        back_icon = IconLeftWidget(icon='arrow-left-thick')
        
        back_icon.bind(on_release=self.back)
        
        toolbar.add_widget(back_icon)
        
        box.add_widget(toolbar)
        item = TwoLineIconListItem(text="Theme Style", secondary_text='Change the screen to Dark or light')
        item.add_widget(IconLeftWidget(icon="moon-waning-crescent"))
        item.bind(on_release=self.darkmode)
        box.add_widget(item)

        item1 = TwoLineIconListItem(text="Bold Format", secondary_text='Change the font to bold or normal')
        item1.add_widget(IconLeftWidget(icon="format-bold"))
        item1.bind(on_release=self.Bold)
        box.add_widget(item1)

        item2 = TwoLineIconListItem(text="Index lines", secondary_text='Change index lines to 3 or 1')
        item2.add_widget(IconLeftWidget(icon="layers"))
        item2.bind(on_release=self.Lines)
        box.add_widget(item2)
        box.add_widget(ScrollView())
        self.add_widget(box)

    def back(self, obj):
        Containor.current = Containor.screens[-2].name
        del Containor.screens[-1]
        
    def darkmode(self, obj):
        global dark
        if dark == False:
            dark = True
        else:
            dark = False

    def Bold(self, obj):
        global bold
        if bold == False:
            bold = True
            Snackbar(text="Bold Format Added").show()
        else:
            bold = False
            Snackbar(text="Bold Format Removed").show()

    def Lines(self, obj):
        global line
        if line == False:
            line = True
            Snackbar(text="Index lenght increased").show()
        else:
            line = False
            Snackbar(text="Index length decreased").show()





#customised snakbar for to show settings saved            
class snack_bar_index(Snackbar):
    def __init__(self, **kwargs):
        super(snack_bar_index, self).__init__(**kwargs)
        self.text = "Loading "
        self.padding = Window.height*0.1
        Clock.schedule_once(self.index, 0.3)

    def index(self, dt):
        Containor.add_widget(Index(name ="index"))
        Containor.current = "index"





#screen for index page
class Index(Screen):
    
    def __init__(self, **kwargs):
        super(Index, self).__init__(**kwargs)
        
        view = ScrollView()
        layout = GridLayout(cols=1, padding=Window.height*0.01,spacing=Window.height*0.05, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        
        for i in labels:
            s = i
            s_ = []
            for ss in range(len(s)):
                if ss == 1:
                    
                    s_.append('.'+s[ss])
                else:
                    s_.append(s[ss])
            s_ = ''.join(s_)
            

            A_ = A.split('\n')
            
            for m in A_:
                if s_ in m:
                    m = m.split(s_)[1]
                    j = len(m)
                    size_x = j*Window.height*0.042/2.25
                    if Window.width > size_x:
                        size_x = Window.width
                    btn = Cbutton(lts=i, font_name="kannada_mallige",text="[font=Roboto-Bold][b][size="+str(int(Window.height*0.05))+']'+str(i)+'. '+'[/size][/b][/font]'+m+"[font=Roboto-Bold][b][size="+str(int(Window.height*0.05))+']'+'.... '+'[/size][/b][/font]',
                            markup=True, size=(size_x,Window.height*0.06 ), font_size=(Window.height*0.04), background_color=(1,1,1,0),
                        size_hint=(None, None), halign='left', valign = 'center', pos=(0, Window.height-100), color=(0,0,0,1))
                    btn.bind(on_release=self.Screens_2)
                    layout.add_widget(btn)
                    break
            
            
            
            
            
        view.add_widget(layout)

        box = BoxLayout(orientation='vertical')
        toolbar = TwoLineIconListItem(bg_color=(0, .588, .533,1))
        back_icon = IconLeftWidget(icon='arrow-left-thick')
        
        back_icon.bind(on_release=self.back)
        
        toolbar.add_widget(back_icon)
        
        box.add_widget(toolbar)
        
        
        box.add_widget(view)
        self.add_widget(box)
    def back(self, obj):
        Containor.current = Containor.screens[-2].name
        del Containor.screens[-1]
     

    def Screens_2(self, instant):
        
        Containor.add_widget(Main_2(letter = str(instant.lts), name = str(instant.lts)))
        Containor.current = str(instant.lts)




#variable to keep track of the theme(dark or not )
dark = False


#Main app Class where all othe widgets are added 
class TestApp(MDApp):
    
    icon = 'icon.png'

    def build(self):
        global Containor
        #self.theme_cls.primary_palette = "Teal"
        Containor = AppScreenManager()
        Clock.schedule_interval(self.check_dark, 1.0/60.0)
        
        Containor.add_widget(Mainnavscreen(name="main"))
        return Containor
    
    def check_dark(self, dt):
        
        if dark == True:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.back)
     

    def back(self, window, key, *largs):
        
        if key == 27 and Containor.current_screen != Containor.screens[0]:
            
            
            def set_focus(dt):
                text_main.focus = True
            
            Containor.current = Containor.screens[-2].name
            del Containor.screens[-1]
            return True
        



#Entry screen, this class is not used(instantiated)
class EScreen(Screen):
    def __init__(self, **kwargs):
        super(EScreen, self).__init__(**kwargs)

        
        Clock.schedule_once(self.add_main, 0.1)
        Clock.schedule_once(self.main_invoke, 5)
        
        

    def add_main(self, dt):
        Containor.add_widget(Mainnavscreen(name="main"))
        
    def main_invoke(self, dt):
            
            Containor.current = "main"



#Customise text Input widget
class CTextInput(TextInput):

    def __init__(self, **kwargs):
        self.font_name = 'kannada_mallige'
        self.hint_text = "VÃvï ¸ÀASÉÆ"


        super(CTextInput, self).__init__(**kwargs)
        
        self.font_size = Window.height*0.07
        self.multiline = False
        Clock.schedule_interval(self.focus_check, 1.0/60.0)
        self.icon_right = "arrow-right"
        
        
    def focus_check(self, dt):
        if self.text != '':
            self.font_name = "Roboto"
        else:
            self.font_name =  "kannada_mallige"
        
        if Focus == True:
            self.focus = True
            self.font_name = "Roboto"
        def set_focus(dt):
            self.focus = True
        
    
    
if __name__ == '__main__':
    TestApp = TestApp()
    TestApp.run()
