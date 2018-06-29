import requests

class wake_on_lan(object):
    id = ''
    passwd = ''
    cookies = None
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    def login(self):
        login_url = 'http://"your iptime domain"/sess-bin/login_handler.cgi'
        data = {
            'init_status' : '1',
            'captcha_on' : '0',
            'captcha_file' : '',
            'username' : self.id,
            'passwd' : self.passwd,
            'captcha_code' : ''
        }


        loginreq = requests.post(url=login_url, data=data, headers=self.header)

        self.cookies = {
            'efm_session_id' : self.parseCookie(loginreq.text)
        }
        print('-------------------------------------------------------------------------------------------------')


    def wakeup(self):
        wolurl = 'http://"your iptime domain"/sess-bin/timepro.cgi'
        data = {
            'tmenu' : 'iframe',
            'smenu' : 'expertconfwollist',
            'nomore' : '0',
            'wakeupchk' : '', # target MAC address
            'act' : 'wake'
        }
        wakereq = requests.post(url=wolurl, data=data, headers=self.header, cookies=self.cookies)
        if wakereq.text.find('session_timeout') != -1:
            print('[ session timeout ] Wake on lan failed.')
            return


    def parseCookie(self, text):
        startindex = text.find("('") + 2
        lastindex = text.find("')")
        return text[startindex:lastindex]


obj = wake_on_lan()
obj.login()
obj.wakeup()
