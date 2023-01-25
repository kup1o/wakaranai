import config
import discord
from discord import utils
from discord.ext import commands

bot = discord.Client()
bot = commands.Bot(command_prefix="~~")

@bot.command()
async def embed(ctx):
  embed=discord.Embed(title="Choose your role!", url="https://google.com/", description="🎮 Player\n🖥️ Programmer", color=0x03fc7f)
  embed.set_thumbnail(url="")
  embed.set_footer(text="")
  await ctx.send(embed=embed)

bot.run(config.TOKEN)
