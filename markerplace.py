#!/usr/bin/python
import pyxhook
import time
import os
 
class Marker():
    assigns = {}
    waiting_for_mark = False
    waiting_to_set   = False
        
    def keydown(self,event):
        print event.__dict__
        self.event = event
        key = str(event.Key)
        if (key in keymap):
            key = keymap[key]
        if (len(key) > 1):
            key = " [" + key + "] "
        print key
        print hm.ison["shift"]

    def keyup(self, event):
        key = str(event.Key)
        if (key == 'F2'):
            print ">> Waitint to SET"
            self.waiting_to_set = True
            return
        if (key == 'F3'):
            print ">> Waitint for MARK"
            self.waiting_for_mark = True
            return

        if (self.waiting_for_mark):
            self.waiting_for_mark = False
            print "Switching to window %s" % (self.assigns[key],)
            os.system("wmctrl -ia %s" % (self.assigns[key],))

        if (self.waiting_to_set):
            self.waiting_to_set = False
            win_id = str(event.Window)
            self.assigns[key] = win_id
            print("Added window: %s : %s" % (win_id, event.WindowProcName,))

marker = Marker()
hm = pyxhook.HookManager()
hm.HookKeyboard()
hm.KeyUp = marker.keyup
hm.start()
 
while True:
    time.sleep(1)
