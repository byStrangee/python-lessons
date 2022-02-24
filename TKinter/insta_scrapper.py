import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'fazl.ulloh74')

#print("Username: ", profile.username)
#print("User ID: ", profile.userid)
#print("Number of Posts: ", profile.mediacount)
#print("Followers: ", profile.followers)
#print("Followees: ", profile.followees)
#print("Bio: ", profile.biography,profile.external_url)

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")