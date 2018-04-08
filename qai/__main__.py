# -*- coding: utf-8 -*-
import irc3
from qai.irc.plugin import Plugin

if __name__ == '__main__':
    config = dict(
        nick='QAI', autojoins=['#QAI'],
        host='localhost', port=6667, ssl=False,
        includes=[
            'irc3.plugins.core',
            'irc3.plugins.command',
            'irc3.plugins.human',
            __name__,  # this register the plugin
        ]
    )
    bot = irc3.IrcBot.from_config(config)
    irc = Plugin(bot)

    try:
        bot.run(forever=True)
    except ConnectionRefusedError as ex:
        print(ex)
    except LookupError as ex:
        print(ex)
    exit(0)
