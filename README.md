##参考
*  [API Reference](http://www.sublimetext.com/docs/2/api_reference.html)
  *  [中文版](http://baelabs.duapp.com/Sublime/api_reference.html)
  *  [中文版](http://mux.alimama.com/posts/549)
*  [初学sublime text 2扩展插件开发](http://www.cssforest.org/blog/index.php?id=207)
*  [如何开发Sublime Text2插件](http://www.welefen.com/how-to-develop-sublime-text-plugin.html)
*  [如何开发 Sublime Text 2 的插件](http://www.oschina.net/translate/how-to-create-a-sublime-text-2-plugin)

---

*  [Chage "Hello, World!" to insert at cursor position.](http://www.sublimetext.com/forum/viewtopic.php?f=6&p=45349)
*  [Plugin Examples](http://www.sublimetext.com/docs/plugin-examples)

##总结
*  Tools -> New Plugin...来打开一个初始化的插件编辑文件
*  Preferences -> Browse Packages，在该文件夹下建立个子文件夹，里边放插件
*  根据[如何开发Sublime Text2插件](http://www.welefen.com/how-to-develop-sublime-text-plugin.html)写插件是，class ExampleCommand 类命有命名规则
*  ctrl+`调出python控制台，view.run_command('example') 按照命名规则，example来自ExampleCommand
*  以上可知，需要注意命名规则。
*  先用控制台测试，最后绑定快捷键

##安装
直接git clone到Browse Packages里就行

##特性
sublime无法像vim一样直接引用python环境，估计是处于跨平台考虑

不如使用vim写插件舒服

适合直接处理当前文本
