# -*- coding: utf-8 -*-
import irc3
from qai.irc.plugin import Plugin

if __name__ == '__main__':
    config = irc3.utils.parse_config('bot', 'config.ini')

    bot = irc3.IrcBot().from_config(config)
    # bot.config.update(config)
    irc = Plugin(bot)

    bot.run(forever=True)

    exit(0)
