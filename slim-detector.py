from facebook_scraper import get_posts
import csv
import warnings
from datetime import datetime

now = datetime.now()
credentials = ['slim.collector.2021@gmail.com', 'BenEarnZo3']
header = ['page_name', 'timestamp', 'message', 'no_of_comments', 'no_of_likes', 'no_of_shares']
accounts = [
    'CheerLungThailand',
    'ทีมลุงตู่-517309701770358',
    'เรารักลุงตู่-fc-1978098262214274',
    'GoodStudent904',
    'WOMDP',
    'themettad',
    'CheerLung2',
    'satikaluk',
    'lungtumaleaw',
    'siamgreatwarriors',
    'ReformMyThai',
]

warnings.filterwarnings("ignore")
counter = 0

with open('facebook_support_gov_{}.csv'.format(now.strftime("%Y-%m-%d_%H-%M-%S")), 'w', encoding='UTF8',
          newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for account in accounts:
        result = get_posts(account, page_limit=150, timeout=150)
        for post in result:



            post_text = "" if post.get('post_text') is None else post.get('post_text').replace('\n', '')
            shared_text = "" if post.get('shared_text') is None else post.get('shared_text').replace('\n', '')
            if post_text == "" and shared_text == "":
                continue

            record = [
                post['username'],
                post['time'].strftime("%Y-%m-%d %H:%M:%S"),
                "{};{}".format(post_text, shared_text),
                post['comments'],
                post['likes'],
                post['shares']
            ]
            writer.writerow(record)
            print("{}, {}, {}".format(counter, account, post.get('post_url')))
            counter += 1
