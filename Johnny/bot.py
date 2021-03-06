import asyncio
import os

import discord
from discord.ext import commands

from Johnny.utils.logger import Logger


class Johnny(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="?",
            help_command=None,
            description="평범하게 음악을 재생하는 디스코드 봇",
            intents=discord.Intents.all(),
            activity=discord.Game("?help | 나를 불러 내 이름을 불러"),
        )

        self.logger = Logger.defaultLogger("Johnny")
        self.discord = Logger.discordLogger()

    async def on_ready(self):
        self.logger.info("Lil 5ex!")


def auto_load_cogs(bot: Johnny):
    cmdlist = os.listdir("Johnny/cogs/")

    for i in cmdlist:
        if i.endswith(".py") and not i.startswith("__"):
            cmdname = f"Johnny.cogs.{i.replace('.py', '')}"

            try:
                bot.load_extension(cmdname)

            except Exception as error:
                bot.logger.error(f"{cmdname} failed to load: {error}")

    bot.load_extension("jishaku")


bot = Johnny()
