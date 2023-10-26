from service import WaterTimeNotifier
from service import IntervalNotSetError
import yaml


def read_config(config_path="config.yaml"):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        f.close()
    return config
    

def main():
    config = read_config()
    interval_type = config['type_interval'].upper()
    interval = config['interval']
    
    notifier = WaterTimeNotifier(
        lang=config['lang'],
        duration=config['message_duration'],
        icon_path=config['icon_path'],
        lang_file=config['config_path']
    )
    
    if interval_type in ['MINUTES', 'M', 'MIN']:
        notifier.set_interval_minutes(interval)
    
    elif interval_type in ['HOURS', 'H', 'HOUR']:
        notifier.set_interval_hours(interval)
        
    elif interval_type in ['S', 'SEC', 'SECONDS']:
        notifier.set_interval(interval)
    
    else:
        raise IntervalNotSetError('The interval type set is not valid') 
    
    start_at = config.get('start_at', None)
    start_at = None if start_at == "" else start_at
    
    end_at = config.get('end_at', None)
    end_at = None if end_at == "" else end_at
    
    # notifier.notify()
    notifier.keep_notify(start_at, end_at)
    

if __name__ == '__main__':
    main()