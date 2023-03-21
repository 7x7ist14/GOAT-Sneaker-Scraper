# GOAT-Sneaker-Scraper
A scraper for all prices of all listed sizes of a sneaker listed on goat.
The Scraper will scrape all price informations for all listed sizes on GOAT and returnyou a list of them in your discord server.
The message also includes the GOAT product URL, Hypeboost product URL, StockX product URL and Restocks product URL for the Scraped Product.
A product Photo is also added to the return message.

# How to use:

1. Requirements:

Check if you have all the needed Python libraries.

-->To install all needed libraries just do this:
+ open the folder that contains all files (the folder name should be "GOAT-Sneaker-Scraper") in your file Explorer.
+ click on the path and write "cmd" --> now press enter
+ you should now see a cmd window, you just have to type "pip install -r requirements.txt" 
+ all needed libraries should now be installed and your good to go :)


2. Open the "Config" file and input your Discord Bot Token and the name of the channel were you want to use the scraper in.


3. Open and run the "discord_embed" file. (best for this is VS-Code in my opinion)

4. Write the keyword ($goat) + SKU in your discord server (you have to write the message in the same channel that you added to the config file!)
   format: $goat SKU --> (example: $goat CW1590-100)
   --> the command is also changeable in the config file if you want to change it


The Scraper will now send you all listed sizes and their prices in the discord channel.
Also the GOAT Product URL is in the blue title.
At the bottom of the discord message you can also find the StockX, Hypeboost and Restocks product URL to the scraped product.





# Return Message Example:
The return message looks like this:

![image](https://user-images.githubusercontent.com/103487648/226734060-70c3568a-4bfe-4b29-a7f9-c32ac950c43a.png)

