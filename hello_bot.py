from bot import Bot


class HelloBot(Bot):

    def run(self):
        self.chat("Hello, i'm not a bot, ok!")


bot = HelloBot(channel="#ecletic_player")
bot.run()
