import random

import bs4
import requests
from bs4 import BeautifulSoup

class Kakuyomu:
    book_id: int = None

    def __init__(self, book_id: int = None):
        if not book_id is None:
            self.book_id = book_id
        self.userAgents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Android 10; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0",
            "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        ]
        return

    def download(self, book_id: int = None):
        bookId = None
        if self.book_id is None and book_id is None: # 両方無い
            print("[Error] Please input Kakuyomu book_id. code : All none")
            return
        elif self.book_id is not None and book_id is not None: # 両方ある
            print("[Error] Please input Kakuyomu book_id. code : All set")
            return
        elif self.book_id is None and not(book_id is None): # selfがない
            bookId = book_id
            pass
        else:
            bookId = self.book_id
            pass

        kakuyomu_url = "https://kakuyomu.jp"
        base_url = "{}/works/{}".format(kakuyomu_url, bookId)

        # Get first episode url
        userAgent = random.choice(self.userAgents)

        headers = {
            'User-Agent': userAgent
        }

        try:
            response = requests.get(base_url, headers=headers)
        except Exception as e:
            print("[Error] Please input Kakuyomu book_id.")
            return

        profile_html = bs4.BeautifulSoup(response.text, "html.parser")

        while True:
            try:
                title = profile_html.select(
                    "#app > div.DefaultTemplate_fixed__DLjCr.DefaultTemplate_isWeb__QRPlB.DefaultTemplate_fixedGlobalFooter___dZog > div > div > main > div.NewBox_box__45ont.NewBox_padding-px-4l__Kx_xT.NewBox_padding-pt-7l__Czm59 > div > div.Gap_size-2l__HWqrr.Gap_direction-y__Ee6Qv > div.Gap_size-3s__fjxCP.Gap_direction-y__Ee6Qv > h1 > span > a"
                )[0].text
                break
            except Exception as e:
                print("[Error] Try select again. get title")
        print("[Info] Title: {}".format(title))

        while True:
            try:
                all_no_text = profile_html.select(
                    "#app > div.DefaultTemplate_fixed__DLjCr.DefaultTemplate_isWeb__QRPlB.DefaultTemplate_fixedGlobalFooter___dZog > div > div > main > div:nth-child(4) > div.NewBox_box__45ont.NewBox_padding-pb-7l__WeU_U > div.Gap_size-7l__TyUOV.Gap_direction-y__Ee6Qv > div:nth-child(1) > div:nth-child(2) > div > div.NewBox_box__45ont.NewBox_padding-pt-2l__k25C7.NewBox_borderStyle-solid__F7tjp.NewBox_borderColor-defaultGray__NGE9f > div > div > ul:nth-child(2) > li:nth-child(1) > div"
                )[0].text
                break
            except Exception as e:
                print("[Error] Try select again. all_no_text")


        arrow_words = []
        for i in range(10):
            arrow_words.append(str(i))

        all_no = ""

        for w in all_no_text:
            if w in arrow_words:
                all_no += w

        print("[INFO] book general_all_no: {}".format(all_no))

        url = kakuyomu_url + profile_html.select(
            "#app > div.DefaultTemplate_fixed__DLjCr.DefaultTemplate_isWeb__QRPlB.DefaultTemplate_fixedGlobalFooter___dZog > div > div > main > div.NewBox_box__45ont.NewBox_padding-px-4l__Kx_xT.NewBox_padding-pt-7l__Czm59 > div > div.Gap_size-2l__HWqrr.Gap_direction-y__Ee6Qv > div.Gap_size-m__thYv4.Gap_direction-y__Ee6Qv > div > a"
        )[0].get("href")

        print("[INFO] First url: {}".format(url))

        # Download
        book_text = ""
        episode_no = 0

        headers = {
            'User-Agent': userAgent
        }

        while True:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                episode_no += 1

                print("[LOG] {} Downloading... Episode: {}/{}".format(url, episode_no, all_no))

                html = bs4.BeautifulSoup(response.text, "html.parser")
                text = html.select(
                    ".widget-episodeBody.js-episode-body"
                )[0].text

                book_text += "-- Episode: {} --\n\n".format(episode_no) + text

                try:
                    url = kakuyomu_url + html.select(
                        "#contentMain-readNextEpisode"
                    )[0].get("href")
                except:
                    print("[LOG] INFO END Download.")
                    return {
                        "title": title,
                        "text": book_text
                    }
                pass

            else:
                print("[Error] Book response is not 200")
                return