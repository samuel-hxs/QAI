# -*- coding: utf-8 -*-
import irc3
from irc3 import rfc
from irc3.plugins.command import command


@irc3.plugin
class Plugin:
    """A plugin is a class which take the IrcBot as argument
        """

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

    @command(permission='view', public=True, show_in_help_list=False, name='pings')
    def ping(self, mask, target, args):
        """Echo

            %%echo <message>...
        """
        print(' '.join(args['<words>']))
        self.privmsg(mask.nick, ' '.join(args['<words>']))

    @irc3.event(rfc.ERR_NOSUCHSERVER)
    def myevent(self, srv=None, me=None, server=None, data=None):
        pass

    @staticmethod
    def start():
        config = irc3.utils.parse_config('bot', 'irc.config.ini')
        bot = irc3.IrcBot.from_config(config)
        # bot.config.update(config)
        # irc = Plugin(bot)

        bot.run(forever=True)
