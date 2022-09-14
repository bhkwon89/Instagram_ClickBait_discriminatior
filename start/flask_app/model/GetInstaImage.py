from random import randint
import instaloader
from time import sleep



def DownInstaImage(url, dir):

    #print(post_url)

    L = instaloader.Instaloader()
    L.login('인스타 계정','비밀번호')



    posts = instaloader.Post.from_shortcode(L.context, url)
    L.download_post(posts, "static")


#DownInstaImage('https://www.instagram.com/p/CibXeTwhwVe/')