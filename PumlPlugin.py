import sublime
import sublime_plugin
import subprocess
import os

class PumlCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    file = self.view.file_name()
    foo, ext = os.path.splitext(file)
    if ext == ".pu":
      # ret = subprocess.check_output(["ls", '-l', './Puml/plantuml.jar'])
      ret = subprocess.Popen([
        'java',
        '-Djava.awt.headless=true',
        '-DPLANTUML_LIMIT_SIZE=50000',
        '-jar',
        './Puml/plantuml.jar',
        '-v',
        file
      ])
      sublime.active_window().open_file(foo + ".png")
    # ret.terminate()
    # ret = os.system("ls 2>&1")
    # self.view.insert(edit, 0, "" + ret)
    # print('pwd:', ret.decode("utf-8"))

