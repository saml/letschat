
from twisted.words.protocols.jabber.jid import JID
from twisted.application import service
from wokkel.client import XMPPClient

import settings
import letschat

application = service.Application("MUC Client")

client = XMPPClient(JID(settings.EMAIL), settings.PASSWORD)
client.logTraffic = settings.LOG_TRAFFIC
client.setServiceParent(application)

mucHandler = letschat.MUCGreeter(JID(settings.ROOM), settings.NICK)
mucHandler.setHandlerParent(client)
