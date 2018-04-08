# -*- coding: utf-8 -*-
from irc3 import rfc
from irc3.plugins.command import command
import irc3


@irc3.plugin
class Plugin:
    """A plugin is a class which take the IrcBot as argument
        """

    requires = [
        'irc3.plugins.core',
        'irc3.plugins.userlist',
        'irc3.plugins.command',
        'irc3.plugins.human',
    ]

    def __init__(self, bot):
        self.bot = bot

    @irc3.event(irc3.rfc.JOIN)
    def say_hi(self, mask, channel, **kw):
        """Say hi when someone join a channel"""
        if mask.nick != self.bot.nick:
            self.bot.privmsg(channel, 'Hi %s!' % mask.nick)
        else:
            self.bot.privmsg(channel, 'Hi!')

    @command(permission='view', public=True)
    def echo(self, mask, target, args):
        """Echo

            %%echo <message>...
        """
        yield ' '.join(args['<message>'])

    @irc3.event(rfc.ERR_NOSUCHSERVER)
    def myevent(bot, srv=None, me=None, server=None, data=None):
        pass
