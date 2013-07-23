from AppKit import *
from app_delegate import AppDelegate

class App:
  def __init__(self):
    self.app = NSApplication.sharedApplication()
    self.app_delegate = AppDelegate.alloc().init()
    self.app.setDelegate_(self.app_delegate)

  def run(self):
    self.app.run()

if __name__ == '__main__':
  app = App()
  app.run()
