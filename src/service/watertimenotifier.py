from win10toast import ToastNotifier
import json
from service import LangNotAvailableError
from service import IntervalInvalidError
from service import IntervalNotSetError
from time import sleep
from datetime import datetime

class WaterTimeNotifier:
    def __init__(self, lang: str, duration=10, icon_path="./images/glass-of-water.ico", lang_file='./lang/messages.json'):
        self._toast = ToastNotifier()
        self._interval = None
        self._duration = duration
        self._icon_path = icon_path
        self._lang = lang.upper()
        self._lang_file = lang_file
    
    def set_interval(self, interval):
        if not isinstance(interval, int) and interval <= 0:
            IntervalInvalidError(f'Interval set is not valid: {interval}')
        self._interval = int(interval)
        
    def set_interval_minutes(self, interval):
        if not isinstance(interval, int) and interval <= 0:
            IntervalInvalidError(f'Interval set is not valid: {interval}')
        self._interval = interval * 60
        
    def set_interval_hours(self, interval):
        if not isinstance(interval, int) and interval <= 0:
            IntervalInvalidError(f'Interval set is not valid: {interval}')
        self._interval = interval * 3600
        
    def _load_lang_file(self):
        json_data = None
        with open(self._lang_file, 'rb') as f:
            json_data = json.load(f)
            f.close()
            
        return json_data
        
    def get_avaliable_langs(self):
        json_data = self._load_lang_file()
        langs = [x["lang"] for x in json_data]
        info = {
            "lang_set": self._lang, 
            "available_langs": langs,
            "is_available": self._lang in langs
            }
        
        return info
        
    def _load_msg(self):
        json_data = self._load_lang_file()
        results = self.get_avaliable_langs()
        
        if not results["is_available"]:
            msg = f"Language '{self._lang}' is not available in config file messages.json"
            raise LangNotAvailableError(msg)
        
        lang_set = [x for x in json_data if x['lang'] == self._lang][0]
        title = lang_set['title']
        message = lang_set['message']
        
        return title, message

    def notify(self):
        title, message = self._load_msg()
        
        self._toast.show_toast(
            title,
            message,
            duration=self._duration,
            icon_path=self._icon_path,
            threaded=False
        )
        
    def keep_notify(self, start_at: str=None, end_at: str=None):
        if not self._interval:
            raise IntervalNotSetError('Please, set an interval')
        
        none_check = [x for x in (start_at, end_at) if x is None]
        
        if len(none_check) == 1:
            raise AttributeError('Specify both start_at/end_at or neither')
        
        elif len(none_check) == 0:
            if start_at > end_at:
                raise AttributeError('start_at is greather than end_at')
            
            elif start_at == end_at:
                raise ArithmeticError('start_at and end_at are equals')
        
        while True:
            try:
                sleep(self._interval)
                now = datetime.now().strftime('%H:%M')
                if not start_at is None and not end_at is None: 
                    if now <= start_at:
                        continue
                    
                    elif now >= end_at:
                        continue   
                
                self.notify()
                
            except KeyboardInterrupt:
                return
        