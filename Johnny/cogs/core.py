from discord.ext import commands
from Johnny.bot import Johnny
from Johnny.utils.logger import Logger


class Core(commands.Cog):
    patching = True

    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Logger.cogLogger(self)


def setup(bot: Johnny):

    if not Core.patching:
        bot.add_cog(Core(bot))

    elif Core.patching:
        return bot.logger.warn(f"Core is in patching status.")
