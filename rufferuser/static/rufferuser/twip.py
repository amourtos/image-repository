from rufferuser.models import RufferUser
from image.models import Image


def twip_greeting(user):
    try:
        twip = RufferUser.objects.create_user(
            username="twip",
            password="1R4TyskRmCKjV05v"
        )
    except Exception:
        print(Exception)
        print("Twip is saying hello")
        twip = RufferUser.objects.get(username="twip")

        welcome = Image.objects.create(
            title="Welcome!",
            description=f"""
             Hello, @{user} , and thanks joining us! My name is Twip,
             and I'm here to help you get started. When a user tags you in a tweet,
             you will receive a notification. Be careful! When you refresh the page, or navigate to a new one, it refreshes your notifications so you can't see them anymore.
             """,
            image="twip.jpg",
            uploaded_by=twip
        )
        welcome.tags.add(user)
        welcome.save()
        twip_greeting = Image.objects.create(
            title="Listen!",
            description=f"""
             Hey @{user} ! Listen! You aren't going to start off with any followers, so press the search button with an empty search bar to see a list of everyone's images. Home page will only show posts from who you follow
            """,
            image="twip.jpg",
            uploaded_by=twip
        )
        twip_greeting.tags.add(user)
        twip_greeting.save()
    return twip
