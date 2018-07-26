import praw
import time
import requests
import ctypes as c
import cgi

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

subName = "wallpapers"
timeFrame = "day"
postNum = 1

def get_img(subName, timeFrame, postNum):
    for submission in reddit.subreddit(subName).top(timeFrame, limit=postNum):
        url = submission.url
        title = submission.title
        score = submission.score
        date = time.strftime("%d-%m-%Y")
        path = './path/' + date + '.png'
        img_ext = ('jpg', 'jpeg', 'png')
        if url.endswith(img_ext):
            print("\n" + title + "\n" + url + "\n" + str(score) + "\n" + date)
            img_data = requests.get(url).content
            with open(path, 'wb') as handler:
                handler.write(img_data)
        image = date + '.png'
        return image

get_img(subName, timeFrame, postNum)

def setWP():
    SPI = 20
    SPIF = 2
    date = time.strftime("%d-%m-%Y")
    path = 'C:/../../../../path/to/image/'+date+'.png'
    c.windll.user32.SystemParametersInfoA(SPI, 0, path.encode("us-ascii"), SPIF)

if __name__ == "__main__":
    setWP()