from bot import Bot


class ReplyBot(Bot):
    def action(self, username, msg):
        self.chat("@{} ok".format(username))


bot = ReplyBot(channel="#ecletic_player")
bot.run()
