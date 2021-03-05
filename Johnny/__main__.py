from Johnny.bot import auto_load_cogs, bot
from Johnny.utils.getenv import getenv

auto_load_cogs(bot)
bot.run(getenv("TOKEN"))
