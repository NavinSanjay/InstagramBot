from instabot import Bot
bot = Bot()
from user_config import USERNAME, PASSWORD

bot.login(username=USERNAME , password=PASSWORD)

#user = input("Enter the artist's username: ")

followers = bot.get_user_followers("doggboi.834")

file = open("all_followers.txt", "w")

for follower in followers:
    names = bot.get_username_from_user_id(follower)

    file.write(names + "\n")

file.close()

