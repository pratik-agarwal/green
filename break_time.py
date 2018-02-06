#open browser with some content at regular interval

import webbrowser
import time

count=0
while (count<3):
        time.sleep(3)
        webbrowser.open("http://www.google.com")
        count = count+1


