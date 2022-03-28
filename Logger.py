import requests, datetime


def log_event(event,
              status='testing',
              duration='test',
              collection = 'logs' ):
    
    host = 'localhost'
    port = 5000
    
    log_event = {
        "app":event,
        "status": status,
        "time":str( datetime.datetime.now() ),
        "duration":duration
        }
    

    req = requests.post('http://'+host+':'+str(port)+'/'+collection, data = log_event)
    print(type(req.json()))
    print(req.json())
    
    res_status = req.json()['_status']
    #eTag = req.json()['_etag']
    #res_id = req.json()['_id']
    if (res_status == 'OK'):
        return True
    
    else:
        print(res_status)
        return False
    
    
    
if __name__ == '__main__':
    log_event("test event")
    