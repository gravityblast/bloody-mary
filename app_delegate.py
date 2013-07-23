from Foundation import *
from AppKit import *
from session import Session

class AppDelegate(NSObject):
  def applicationDidFinishLaunching_(self, app):
    self.session = None
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
    self.menu_item_start = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Start', 'start:', '')
    self.menu.addItem_(self.menu_item_start)
    menu_item_quit = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit', 'terminate:', '')
    self.menu.addItem_(menu_item_quit)
    self.status_item.setMenu_(self.menu)

  def start_(self, notification):
    if self.session != None:
      self.session.stop()
    self.session = Session()
    self.session.start()

