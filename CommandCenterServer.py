
from eve import Eve

if __name__ == '__main__':

    app = Eve()
    app.run(host = '0.0.0.0')   #running on 0.0.0.0
                                #instead of 127.0.0.1 or localhost
                                #lets others on local network access