import instaloader

mydata = instaloader.Instaloader()

name = input("enter the profilename :")

pic = mydata.download_profile(name,profile_pic_only = True)
