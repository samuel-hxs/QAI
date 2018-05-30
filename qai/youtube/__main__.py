from qai.config.plugin import Config
from qai.youtube.plugin import Plugin

import asyncio

if __name__ == '__main__':
    config: Config = Config('./qai.config.ini')
    youtube: Plugin = Plugin(config.config)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(youtube.do_search())
