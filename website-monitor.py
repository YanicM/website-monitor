from urllib.error import URLError, HTTPError
import urllib.request
import datetime
import time
import string
import difflib

class WebsiteToMonitor:

    def __init__(self, url):
        self.filename = self.create_filename(url)
        self.url = url
        # Create the initial copy of the website.
        new_site = self.download_site(self.url)
        self.save_site(new_site, self.filename)

    def create_filename(self, url):
        filename = "".join([i.replace(i, "") if i not in string.ascii_letters else i for i in url])
        current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        filename = f"{filename}_{current_time}.html"
        return filename

    def download_site(self, url):
        try:
            response = urllib.request.urlopen(url)
            web_content = response.read().decode("utf-8")
            return web_content
        except HTTPError:
            return "HTTPError"
        except URLError:
            return "URLError"

    def save_site(self, content, filename):
        f = open(filename, mode="w", encoding="utf-8")
        f.write(content)
        f.close()
        pass

    def show_difference(self, old, new):
        s = difflib.SequenceMatcher(None, old, new)
        for block in s.get_matching_blocks():
            print(block)
        pass

    def compare_site(self):
        new_content = self.download_site(self.url)
        old_content = open(self.filename, mode="r", encoding="utf-8").read()
        try:
            if new_content.split("</head>")[1] != old_content.split("</head>")[1] or new_content.split("</HEAD>")[1] \
                    != old_content.split("</HEAD>")[1]:
                print("The website has been updated!")
                self.show_difference(old_content, new_content)
                # As there was an update, the filename needs to be updated.
                self.filename = self.create_filename(self.url)
                self.save_site(new_content, self.filename)
                pass
        except IndexError:
            print("The header could not be read.")
            pass


if __name__ == "__main__":
    test_monitor = WebsiteToMonitor("https://news.ycombinator.com/")
    while True:
        time.sleep(60)
        test_monitor.compare_site()
