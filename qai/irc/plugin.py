# -*- coding: utf-8 -*-
import asyncio

import irc3
from irc3.plugins.command import command


@irc3.plugin
class Plugin:
    """A plugin is a class which takes QAI as argument
    """

    def __init__(self, bot):
        self.bot = bot

    @irc3.event(irc3.rfc.CONNECTED)
    def on_connect(self, *args, **kwargs):
        """Authenticate to the server
        """
        pass
        # self.bot.privmsg('nickserv', 'identify %s' % self.bot.config['nickserv_password'])

    @irc3.event(irc3.rfc.JOIN)
    def on_join(self, channel, mask):
        """A user is joining or has joined
        """
        pass

    @irc3.event(irc3.rfc.PRIVMSG)
    @asyncio.coroutine
    def on_private_message(self, *args, **kwargs):
        pass

    @command(permission='admin', name='taunt')
    @asyncio.coroutine
    def command_taunt(self, mask, target, args):
        """Send a taunt

            %%taunt
            %%taunt <person>
        """
        pass

    @command(permission='admin', name='explode')
    @asyncio.coroutine
    def command_explode(self, mask, target, args):
        """Explode

            %%explode
        """
        pass

    @command(permission='admin', name='someone')
    @asyncio.coroutine
    def command_hug(self, mask, target, args):
        """Hug someone

            %%hug
            %%hug <someone>
        """
        pass

    @command(permission='admin', name='flip')
    @asyncio.coroutine
    def command_flip(self, mask, target, args):
        """Flip table

            %%flip
        """
        pass

    @command(permission='admin', name='slap')
    @asyncio.coroutine
    def command_slap(self, mask, target, args):
        """Slap this guy

            %%slap <guy>
        """
        pass

    @command(permission='admin', public=False, name='hidden')
    @asyncio.coroutine
    def command_hidden(self, mask, target, args):
        """Actually shows hidden commands

            %%hidden
        """
        pass

    @command(permission='admin', show_in_help_list=False, name='join')
    @asyncio.coroutine
    def command_join(self, mask, target, args):
        """Overtake the given channel

            %%join <channel>
        """
        pass

    @command(permission='admin', show_in_help_list=False, name='leave')
    @asyncio.coroutine
    def command_leave(self, mask, target, args):
        """Leave the given channel

            %%leave
            %%leave <channel>
        """
        pass

    @command(permission='admin', public=False, show_in_help_list=False, name='puppet')
    @asyncio.coroutine
    def command_puppet(self, mask, target, args):
        """Puppet

            %%puppet <target> WORDS ...
        """
        pass

    @command(permission='admin', public=False, show_in_help_list=False, name='mode')
    @asyncio.coroutine
    def command_mode(self, mask, target, args):
        """mode

            %%mode <channel> <mode> <nick>
        """
        pass

    @command(permission='admin', public=False, show_in_help_list=False, name='reload')
    @asyncio.coroutine
    def command_reload(self, mask, target, args):
        """Reboot the mainframe

            %%reload
        """
        pass

    @command(permission='admin', public=False, show_in_help_list=False, name='groupmanage')
    @asyncio.coroutine
    def command_group_manage(self, mask, target, args):
        """Allows admins to manage groups

            %%groupmanage get
            %%groupmanage add <groupname> TEXT ...
            %%groupmanage del <groupname>
            %%groupmanage join <groupname> <playername>
            %%groupmanage leave <groupname> <playername>
        """
        pass

    @command(permission='admin', public=False, show_in_help_list=False, name='blacklist')
    @asyncio.coroutine
    def command_blacklist(self, mask, target, args):
        """Blacklist given channel/user from !casts, !streams

            %%blacklist get
            %%blacklist add USER ...
            %%blacklist del USER ...
        """
        pass

    @command(permission='admin', public=False, show_in_help_list=False, name='badwords')
    @asyncio.coroutine
    def command_bad_words(self, mask, target, args):
        """Adds/removes a given keyword from the checklist

            %%badwords get
            %%badwords add <word> <gravity>
            %%badwords del <word>
        """
        pass

    @command(permission='admin', public=False, show_in_help_list=False, name='reactionwords')
    @asyncio.coroutine
    def command_reaction_words_admin(self, mask, target, args):
        """Adds/removes a given keyword from the checklist.
        "{sender}" in the reply text will be replaced by the name of the person who triggered the response.

            %%reactionwords get
            %%reactionwords add <word> REPLY ...
            %%reactionwords del <word>
        """
        pass

    @command(permission='admin', public=False, show_in_help_list=False, name='repeat')
    @asyncio.coroutine
    def command_repeat(self, mask, target, args):
        """Makes QAI repeat WORDS in <channel> each <seconds>. Use <ID> to remove them again.

            %%repeat get
            %%repeat add <ID> <seconds> <channel> WORDS ...
            %%repeat del <ID>
        """
        pass

    @command(name='gullible')
    def command_gullible(self, mask, target, args):
        """Display additional commands

            %%gullible
        """
        pass

    @command(name='link')
    def command_link(self, mask, target, args):
        """Link to a website

            %%link
            %%link <argument>
            %%link <argument> WORDS...
        """
        pass

    @command(name='wiki')
    def command_wiki(self, mask, target, args):
        """Link to a wiki page

            %%wiki
            %%wiki <argument>
            %%wiki <argument> WORDS...
        """
        pass

    @command(name='streams')
    @asyncio.coroutine
    def command_streams(self, mask, target, args):
        """List current live streams

            %%streams
        """
        pass

    @command(name='groupping')
    @asyncio.coroutine
    def command_group_ping(self, mask, target, args):
        """Pings people in this group

            %%groupping <groupname>
        """
        pass

    @command(name='reactions')
    @asyncio.coroutine
    def command_reaction_words(self, mask, target, args):
        """Prints the list of checked reaction words

            %%rwords
        """
        pass

    @command(name='tournaments')
    @asyncio.coroutine
    def command_tournaments(self, mask, target, args):
        """Check tourneys

            %%tournaments
        """
        pass

    @command(name='google')
    def command_google(self, mask, target, args):
        """google

            %%google WORDS ...
        """
        pass

    @command(name='name')
    def command_name(self, mask, target, args):
        """name

            %%name
            %%name <username>
            %%name <username> WORDS ...
        """
        pass

    # TODO: Change to only message and do not send if @person is online
    @command(public=False, name='offlinemessage')
    @asyncio.coroutine
    def command_offline_message(self, mask, target, args):
        """Store an offline message, it is delivered once the person logs on

            %%offlinemessage <playername> WORDS ...
        """
        pass

    @command(public=False, name='group')
    @asyncio.coroutine
    def command_group(self, mask, target, args):
        """Allows joining and leaving ping groups

            %%group get
            %%group join <groupname>
            %%group leave <groupname>
        """
        pass

    # TODO: Check meaning and check against @command_tournaments
    @command(show_in_help_list=False, name='tourneys')
    @asyncio.coroutine
    def command_tourneys(self, mask, target, args):
        """Check tourneys

            %%tourneys
        """
        pass

    @command(permission='chatlist', show_in_help_list=False, name='move')
    @asyncio.coroutine
    def command_move(self, mask, target, args):
        """Move nick into channel

            %%move <nick> <channel>
        """
        pass

    @command(permission='chatlist', show_in_help_list=False, name='chatlist')
    @asyncio.coroutine
    def command_chat_list(self, mask, target, args):
        """Chat lists

            %%chatlist
            %%chatlist <channel>
            %%chatlist add <channel> <user>
            %%chatlist del <channel> <user>
        """
        pass

    @staticmethod
    def start():
        """Static start function
        """
        config = irc3.utils.parse_config('bot', 'irc.config.ini')
        bot = irc3.IrcBot.from_config(config)

        bot.run(forever=True)
