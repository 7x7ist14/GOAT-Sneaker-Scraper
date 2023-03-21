import discord
import datetime
import main
from discord.ext import commands
from config import TOKEN, CHANNEL_NAME, COMMAND_PREFIX

product_title = main.product_title_goat
product_img = main.product_img_goat
product_url = main.product_url_goat
product_sizes = main.product_sizes_goat
product_url_stockX = main.stockx_url
product_url_hypeboost = main.product_url_hypeboost
product_url_restocks = main.restocks_url
product_url_sneakit = main.sneakit_product_url

if not TOKEN:
    raise ValueError("The Bot-Token was not included in the config.py file")

if not CHANNEL_NAME:
    raise ValueError("The Channel-Name was not included in the config.py file")

if not COMMAND_PREFIX:
    raise ValueError("The Command-Prefix was not included in the config.py file")

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Scraping! (GOAT)'))
    print("Bot logged in!")


@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  message_content = message.content.lower()

  if message.channel.name == CHANNEL_NAME:
    if message.content.startswith(COMMAND_PREFIX):
      await message.channel.send("Scraping...")

      if COMMAND_PREFIX in message_content:
          SKU_raw = message_content.replace(COMMAND_PREFIX, '')
          SKU = SKU_raw.replace(" ", "")
          product_title_output = product_title(SKU)
          product_img_output = product_img(SKU)
          product_url_output = product_url(SKU)
          product_sizes_output = product_sizes(SKU)
          product_url_stockX_output = product_url_stockX(SKU)
          product_url_hypeboost_output = product_url_stockX(SKU)
          product_url_restocks_output = product_url_restocks(SKU)
          product_url_sneakit_output = product_url_sneakit(SKU)

          embed = discord.Embed(
            title=product_title_output,
            url=product_url_output,
            color=0x607d8b
          )
          embed.set_author(
            name="GOAT Scraper",
            url="https://twitter.com/jakobaio",
            icon_url= "https://play-lh.googleusercontent.com/XSe2IZfyHjzRL0qSqTOuA4zgr-Ha6oiCMGcOlOvPqcKVaeLIhBNmU3BoUzyIfEISUZQ=w240-h480-rw"
            )
          embed.set_thumbnail(
            url=product_img_output
          )
          embed.add_field(
            name="Prices:",
            value=product_sizes_output
          )
          embed.set_footer(
            text="Developed by Jakob.AIO"
          )
          embed.add_field(
            name="Open Product on:",
            value=f"[[StockX]]({product_url_stockX_output})      " f"[[GOAT]]({product_url_output})      " f"[[Restocks]]({product_url_restocks_output})      " f"[[Hypeboost]]({product_url_hypeboost_output})      " f"[[Sneakit]]({product_url_sneakit_output})      ",
            inline=False
          )
          embed.set_footer(
            text=f"Developed by JakobAIO      |      GOAT-Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
          )

          await message.channel.send(embed=embed)
          print('Scraping Successful!')


bot.run(TOKEN)
