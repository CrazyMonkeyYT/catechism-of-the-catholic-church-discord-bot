import discord
import math
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#ccc bot
def cccLookUp(cccNum):
    file1 = open("ccc.txt","r")
    lineNum = 0
    while lineNum< cccNum :
        line = file1.readline()
      #  print(line)
        lineNum = lineNum + 1
    return line
    print("done")
    file1.close()


#file1.readline()!= None
def main():
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.startswith('ccc'):
            try:
                print("|"+message.content[3:]+"|")
                num =  int(message.content[3:])
                await message.channel.send(cccLookUp(num))
                main()

            except ValueError:
                await message.channel.send(message.content + "does not exist")
                main()
           

main()          
client.run('your bot key here')
