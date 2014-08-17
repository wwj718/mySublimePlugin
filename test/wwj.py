#coding=utf-8
import sublime, sublime_plugin
import sys,os

# request-dists is the folder in our plugin
sys.path.append(os.path.join(os.path.dirname(__file__)))
import mySublimePlugin
class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		feed_url = "http://wwj718.github.com/feeds/all.rss.xml"
		#类比vim,self.view.insert(edit,self.view.sel()[0].begin(), "Hello, World!\n") 类似buffer.append，注意\n 。 ok模拟append搞定
		#汉语使用u"你好"
		self.view.insert(edit, self.view.sel()[0].begin(), "Hello, World!"+"\n")
