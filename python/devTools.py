import PyChromeDevTools

# chrome = PyChromeDevTools.ChromeInterface()
chrome = PyChromeDevTools.ChromeInterface(host="0.0.0.0",port=9222)
chrome.Network.enable()
chrome.Page.enable()

chrome.Page.navigate(url="http://www.zhihu.com")
event,messages=chrome.wait_event("Page.frameStoppedLoading", timeout=60)

for m in messages:
    if "method" in m and m["method"] == "Network.responseReceived":
        try:
            url=m["params"]["response"]["url"]
            print (url)
        except:
            pass