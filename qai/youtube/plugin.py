import asyncio
import configparser
import json
from typing import Dict, Union, Any

import aiohttp
import async_timeout


class Plugin:
    search_url: str = None
    config: configparser = None
    live_streams: Dict[str, Union[str, Any]] = None
    loop: asyncio.events = None

    def __init__(self, config: configparser):
        self.config = config
        self.live_streams = []
        try:
            youtube = self.config['youtube']
            self.search_url = youtube['search_template'].format(youtube['api_key'])
        except KeyError as ex:
            print('Missing value for key "{0}" in config for plugin {1}.'.format(ex, 'qai.youtube'))
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.do_search())

    async def do_search(self)-> Dict[str, Union[str, Any]]:
        """

        :rtype: Dict[str, Union[str, Any]]
        :return:
        """
        async with aiohttp.ClientSession() as session:
            async with async_timeout.timeout(10):
                async with session.get(self.search_url) as response:
                    data = await response.text()
                    try:
                        self.live_streams.clear()
                        for stream in json.loads(data)['items']:
                            t = stream["snippet"].get("publishedAt", "T0")
                            date = t.split("T")
                            hour = date[1].replace("Z", "")
                            hour = (hour.split("."))[0]
                            self.live_streams['channel'] = stream["snippet"]["channelTitle"]
                            self.live_streams['text'] = "{0} - {1} - {2} since {3} ".format(
                                    stream["snippet"]["channelTitle"],
                                    stream["snippet"]["title"],
                                    "https://gaming.youtube.com/watch?v={0}".format(stream["id"]["videoId"]),
                                    hour)
                        return self.live_streams
                    except (KeyError, ValueError):
                        return []
