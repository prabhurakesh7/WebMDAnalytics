cd __author__ = 'Rakesh'

from mysolr import Solr
import lucene
class LuceneFileGenerator(object):

    def __init__(self):
        print('ss')

    def createDictList(self):
        dList=[]
        d=dict()
        d['data1']='someData1'
        d['data2']='someData2'
        d['data3']='someData3'
        d['data4']='someData4'
        d['data5']='someData5'
        d['data6']='someData6'
        d1=dict()
        d1['data1']='someData11'
        d1['data2']='someData21'
        d1['data3']='someData31'
        d1['data4']='someData41'
        d1['data5']='someData51'
        d1['data6']='someData61'
        dList.append(d1.copy())
        return dList

    def addDoc(self,dList):
        solr=Solr()
        solr.update(dList, 'json', commit=False)
        solr.commit()

    def getAllDoc(self):
        solr = Solr()
        # Search for all documents
        response = solr.search(q='*:*')
        # Get documents
        documents = response.documents
        for data in documents:
            print(" %s /n ",data)


obj=LuceneFileGenerator()
obj.addDoc(obj.createDictList())
obj.getAllDoc()


