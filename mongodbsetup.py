import pymongo;
import loggin as lo;
loger=lo.loggin()
doimanFile=loger.writingInfile();
domainConsole=loger.writeInConsolo();

class createMongoConnectionObject:
    def __init__(self,name='dheeraj',pass0='1234@api'):
        # self.url=f"mongodb+srv://{name}:{pass0}.2hdzl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
        # self.url='mongodb+srv://root:api123@dheerajcluster.ochnr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        self.url='mongodb+srv://root:api1234@pymo.h6ifa.mongodb.net/pymo?retryWrites=true&w=majority'
        domainConsole.info('Mongo url given')
        
    def sendMongoConnection(self):
        try:
            domainConsole.info('trying for mongo connection')
            client =    pymongo.MongoClient(self.url)
        except Exception as e:
            print('CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCConet error')
            doimanFile.error(f'Mongo Connection error {e}')
            return e;
        return client;    
    
    def insertingError(err,result):
        domainConsole.info('inserted Doc');
        doimanFile.error(result)