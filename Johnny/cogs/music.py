from discord.ext import commands
from Johnny.bot import Johnny
from Johnny.utils.logger import Logger


class Music(commands.Cog):
    patching = True

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Logger.cogLogger(self)


def setup(bot: Johnny):

    if not Music.patching:
        bot.add_cog(Music(bot))

    elif Music.patching:
        return bot.logger.warn(f"Core is in patching status.")
