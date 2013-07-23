from AppKit import *

class Session:
  def __init__(self):
    self.timer = None

  def start(self):
    print 'Started'
    selector = objc.selector(self.handler, signature='v@:')
    self.timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(60 * 25, self, selector, None, False)

  def stop(self):
    print 'Stopped'
    if self.timer != None:
      print 'Invalidating current timer'
      self.timer.invalidate()

  def handler(self):
    print 'FINISH'
    notification = NSUserNotification.alloc().init()
    notification.setTitle_("Bloody Mary")
    notification.setInformativeText_("Session finished")
    notification.setSoundName_(NSUserNotificationDefaultSoundName)
    NSUserNotificationCenter.defaultUserNotificationCenter().deliverNotification_(notification)

