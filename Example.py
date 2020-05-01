import Tengine.TextEngine as te

class SomeScene(te.Scene):
	def render(self):
		self.RenderText('aaaa~aaa')
		rc = self.WaitForInput()
		if rc == '1':
			return 'hello2'
		else:
			return 'hello'

class SomeScene2(te.Scene):
	def render(self):
		self.RenderText('a'*50*25)
		self.WaitForInput()
		return 'finish'

class EndScene(te.Scene):
	def render(self):
		self.RenderText('This is end')
		self.WaitForInput()

_map = te.Map()
_map.AddScene(SomeScene(), 'hello')
_map.AddScene(SomeScene2(), 'hello2')
_map.AddScene(EndScene(), 'finish')
_map.SetFirstScene('hello')
_map.SetLastScene('finish')
engine = te.Engine(_map)
engine.title = 'Example'
engine.Start()