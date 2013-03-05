from twisted.python import log

from wokkel.muc import MUCClient

class MUCGreeter(MUCClient):
    """
    I join a room and respond to greetings.
    """

    def __init__(self, roomJID, nick):
        MUCClient.__init__(self)
        self.roomJID = roomJID
        self.nick = nick


    def connectionInitialized(self):
        """
        Once authorized, join the room.

        If the join action causes a new room to be created, the room will be
        locked until configured. Here we will just accept the default
        configuration by submitting an empty form using L{configure}, which
        usually results in a public non-persistent room.

        Alternatively, you would use L{getConfiguration} to retrieve the
        configuration form, and then submit the filled in form with the
        required settings using L{configure}, possibly after presenting it to
        an end-user.
        """
        def joinedRoom(room):
            if room.locked:
                # Just accept the default configuration. 
                return self.configure(room.roomJID, {})

        MUCClient.connectionInitialized(self)

        d = self.join(self.roomJID, self.nick)
        d.addCallback(joinedRoom)
        d.addCallback(lambda _: log.msg("Joined room"))
        d.addErrback(log.err, "Join failed")


    def receivedGroupChat(self, room, user, message):
        """
        Called when a groupchat message was received.

        Check if the message was addressed to my nick and if it said
        C{'hello'}. Respond by sending a message to the room addressed to
        the sender.
        """
        if message.body.startswith(self.nick + u":"):
            nick, text = message.body.split(':', 1)
            text = text.strip().lower()
            if text == u'hello':
                body = u"%s: Hi!" % (user.nick)
                self.groupChat(self.roomJID, body)

