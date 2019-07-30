__module_name__ = "WebhookHighlights"
__module_version__ = "0.0.1"
__module_description__ = "Send a Webhook request when certain highlighted words are detected in incoming messages"


import hexchat
import requests
import json

STATUS_READ = "read"
STATUS_RECEIVED = "received"
current_status = ""

URL_RECEIVED = hexchat.get_pluginpref("URL_RECEIVED")
URL_READ = hexchat.get_pluginpref("URL_READ")
highlights = json.loads(hexchat.get_pluginpref("HIGHLIGHTS"))["highlights"]
alwaysNotifyForPrivate = True if hexchat.get_pluginpref("ALWAYS_TRIGGER_FOR_PRIVATE_MESSAGES") == 'True' else False


def triggerRead(w, we, u):
  callWebHookRead()

def triggerReceived(w, we, u):
  callWebHookReceived()

def callWebHookReceived():
  global current_status
  if current_status == STATUS_RECEIVED:
    return None
  current_status = STATUS_RECEIVED
  requests.post(url = URL_RECEIVED)

def callWebHookRead():
  global current_status
  if current_status == STATUS_READ:
    return None
  current_status = STATUS_READ
  requests.post(url = URL_READ)

def privateMessage(w, we, u):
  if alwaysNotifyForPrivate:
    callWebHookReceived()
  else:
    message(w,we,u)

def message(w, we, u):
  message = w[1]
  if any(word in message for word in  highlights):
    callWebHookReceived()
  
def windowFocus(w, we, u):
  callWebHookRead()


hexchat.hook_print("Private Message to Dialog", privateMessage)
hexchat.hook_print("Private Message", privateMessage)
hexchat.hook_print("Channel Message", message)
hexchat.hook_print("Focus Window", windowFocus)
hexchat.hook_print("Channel Msg Hilight", message)
hexchat.hook_command("trigger_received", triggerReceived)
hexchat.hook_command("trigger_read", triggerRead)

