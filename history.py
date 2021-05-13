from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import urllib.request
import json

class History(BotPlugin):
    """Return events from day in history"""

    @arg_botcmd('-d', type=str, dest='day', default='na')
    @arg_botcmd('-m', type=str, dest='month', default='na')
    def day_in_history(self, msg, month, day):
        url = 'https://apizen.date/api/'
        if day == 'na':
            day = '1'
        if month == 'na':
            month = '1'
        page = urllib.request.Request(url+month+'/'+day)
        response = json.loads(urllib.request.urlopen(page).read().decode('utf-8'))
        return response['data']['Events'][0]['text']
