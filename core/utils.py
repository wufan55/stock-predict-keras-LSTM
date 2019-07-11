# -*- coding: utf-8 -*- 

__author__ = 'Fan'
__license__ = 'SYSU'
__date__ = '2019.07.11'

import json
import datetime as dt
from Showapi.ShowapiRequest import ShowapiRequest


class DataCollect:
    """
    data collect utils, read detailed instructions in 'https://www.showapi.com/' then get start
    """

    def __init__(self, appId, appId_password):
        """
        use showapi to collect stock data
        visit 'https://www.showapi.com/' to get detailed instructions

        :param appId: type string, the appId you applied
        :param appId_password: type string, the password of your appId
        """

        self.request_url = "http://route.showapi.com/131-50"
        self.appId = appId
        self.appId_password = appId_password

    def data_collect(self, code, time, begin_day, type, data_file_path):
        """
        collect data from showapi and save in .json format
        visit 'https://www.showapi.com/' to get detailed instructions

        :param code: type string, stock code
        :param time: type string, data interval length
        :param begin_day: type string, data begin date
        :param type: type string
        :param data_file_path: type string, data json file path, if not exist, then create, else cover the old
        """

        r = ShowapiRequest(self.request_url, self.appId, self.appId_password)
        r.addBodyPara("code", code)
        r.addBodyPara("time", time)
        r.addBodyPara("beginDay", begin_day)
        r.addBodyPara("type", type)
        res = r.post()

        data = json.loads(res.text)
        with open(data_file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=4, ensure_ascii=False))
        print('Data successfully collect !\n')


class Timer:
    """
    time utils, calculate taken time from start to end in one step
    """

    def __init__(self):
        self.start_dt = None

    def start(self):
        self.start_dt = dt.datetime.now()

    def stop(self):
        end_dt = dt.datetime.now()
        print('Time taken: %s' % (end_dt - self.start_dt))
