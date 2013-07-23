from Foundation import *
from AppKit import *

class AppDelegate(NSObject):
  def applicationDidFinishLaunching_(self, app):
    pass
    # print 'applicationDidFinishLaunching'

  def applicationWillFinishLaunching_(self, app):
    pass
    # print 'applicationWillFinishLaunching'


class App:
  def __init__(self):
    self.app = NSApplication.sharedApplication()
    self.app_delegate = AppDelegate.alloc().init()
    self.app.setDelegate_(self.app_delegate)
    self.init_status_bar()
    self.init_menu()

  def init_status_bar(self):
    self.status_bar = NSStatusBar.systemStatusBar()
    self.status_item = self.status_bar.statusItemWithLength_(NSVariableStatusItemLength)
    self.status_item.setHighlightMode_(1)

    icon = NSImage.alloc().initWithContentsOfFile_('icon.png')
    self.status_item.setImage_(icon)

  def init_menu(self):
    self.menu = NSMenu.alloc().init()
    menu_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Start', 'start:', '')
    self.menu.addItem_(menu_item)
    menu_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit', 'terminate:', '')
    self.menu.addItem_(menu_item)
    self.status_item.setMenu_(self.menu)

  def start_(self, notification):
    print 'Start'

  def run(self):
    self.app.run()

if __name__ == '__main__':
  app = App()
  app.run()
