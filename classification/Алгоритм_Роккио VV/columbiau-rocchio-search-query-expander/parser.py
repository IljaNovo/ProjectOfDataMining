import json

class Parser:
    '''
    classdocs
    '''


    def __init__(self, rawJSON):
        
        self.rawJSON = rawJSON
        self.DocumentsList = []
        
    def parser(self):
     
       results = self.rawJSON
     
       resultLength = len(results)
    
       #generate list of dictionaries one for each doc
       self.DocumentsList = [{'Description': results[k]['Description'], 'Title': results[k]['Title'], \
                         'Url': results[k]['Url'], 'IsRelevant': None, 'Body': None, 'URLBody': None} for k in range(resultLength)]
    
    def getDocList(self):
        
        if self.DocumentsList == None:
            print ('Document List Empty!')
            return   
        return self.DocumentsList
    
    