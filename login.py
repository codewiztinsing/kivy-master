from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginWindow(Screen):
    pass


class LandingWindow(Screen):
    pass



class AccordionWindow(Screen):
    pass


class CheckBoxWindow(Screen):
    pass

class PopWindow(Screen):
    pass




class WindowManager(ScreenManager):
    pass



class MyMainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('my.kv')


	def logger(self):
		# self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
	
		print("login")

	def clear(self):
		# self.root.ids.welcome_label.text = "WELCOME"		
		# self.root.ids.user.text = ""		
		# self.root.ids.password.text = ""
		print("clear")




if __name__ == "__main__":
    MyMainApp().run()



















# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivy.uix.screenmanager import Screen,ScreenManager



# class LoginScreen(Screen):
# 	pass


# class LandingScreen(Screen):
# 	pass


# class WindowManager(ScreenManager):
# 	pass

# kv = Builder.load_file("login.kv")


# class MainApp(MDApp):
# 	def build(self):
# 		self.theme_cls.theme_style = "Dark"
# 		self.theme_cls.primary_palette = "BlueGray"
# 		return kv


# MainApp().run()