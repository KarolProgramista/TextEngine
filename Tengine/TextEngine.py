import tkinter as tk
import time

root = tk.Tk()
bgLabel = tk.Label(root, bg='#693c1e')
textLabel = tk.Label(root, bg='Gray', font=("Veranda", 16), anchor='nw')
inputBox = tk.Entry(root, bg='#595959')
enterButton = tk.Button(root, bg="#595959", text='ENTER')

class EmptyScene(Exception):
	pass

class SceneReturnedNone(Exception):
	pass

class Scene(object):
	def render(self):
		print("This scene has not been projected yet")
		raise EmptyScene()

	def WaitForInput(self):
		while True:
			if enterButton['state'] == 'active':
				enterButton['state'] = 'normal'
				break
			root.update()

		return inputBox.get()
	def RenderText(self, in_text: str):
		i = 0
		buffer = ''
		text = ''
		in_text = in_text.replace('\n', '').replace('\r', '').replace('~', '\n')

		for char in in_text:
			buffer += char

			if len(buffer) > 50:
				buffer+='\n'
				text+=buffer
				buffer=''
				i += 1

			if i > 19:
				text+=buffer
				text += 'Click enter button to continue'
				textLabel['text'] = text
				self.WaitForInput()
				i = 0
				text = ''
				buffer = ''

		text+=buffer

		textLabel['text'] = text

class Map(object):
	def __init__(self):
		self.scens = {

		}

		self.first_scene: str = None
		self.last_scene: str = None
		self.current_scene = None

	def AddScene(self, scene: Scene, name: str):
		self.scens[name] = scene

	def SetFirstScene(self, name: str):
		self.first_scene = name

	def SetLastScene(self, name: str):
		self.last_scene = name

	def start(self):
		self.current_scene = self.scens[self.first_scene].render()
		while(self.current_scene != self.last_scene):
			self.current_scene = self.scens[self.current_scene].render()
			if self.current_scene == None:
				raise SceneReturnedNone()

			root.update()

		self.scens[self.last_scene].render()

class Engine(object):
	def __init__(self, _map: Map):
		self._map = _map
		self.title = 'title'
		

		root.resizable(False, False)
		root.title('Example')
		root.geometry('800x600')
		bgLabel.place(relwidth=1, relheight=1)
		textLabel.place(relx=0.1, rely=0, relwidth=0.8, relheight=1)
		inputBox.place(relx=0.1, rely=0.9, relwidth=0.7, relheight=0.05)
		enterButton.place(relx=0.8, rely=0.9, relwidth=0.1, relheight=0.05)
		root.update()

	def Start(self):
		self._map.start()