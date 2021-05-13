from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import urllib.request
import json
from datetime import date

class History(BotPlugin):
    """Return events from day in history"""

    @arg_botcmd('-d', type=str, dest='day', default='na')
    @arg_botcmd('-m', type=str, dest='month', default='na')
    @arg_botcmd('-y', type=str, dest='year', default='na')
    @arg_botcmd('-i', type=str, dest='index', default='na')
    def day_in_history(self, msg, month, day, index, year):
        current_date = date.today()
        url = 'https://apizen.date/api/'
        if day == 'na':
            day = str(current_date.day)
        if month == 'na':
            month = str(current_date.month)

        page = urllib.request.Request(url+month+'/'+day)
        response = json.loads(urllib.request.urlopen(page).read().decode('utf-8'))
        last_index = len(response['data']['Events'])-1
        if index == 'na':
            index = last_index
        if int(index) > last_index:
            return 'Too large index: '+index+'. Last index is '+str(last_index)
        if year != 'na':
            index = 0
            counter = 0
            for event in response['data']['Events']:
                counter = counter + 1
                if year in event:
                    index = counter
            return response['data']['Events'][index]['text']
        return response['data']['Events'][int(index)]['text']
