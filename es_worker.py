import pyinputplus as pyip

from es_client import es_client

client = es_client().es_client

try:
    client.info()
except Exception as e:
    print ("Connection Error:", e)
    exit()


choices='yes'
while 'yes' in choices:
    choices= pyip.inputMenu( ['create', 'backup','ingest', 'update', 'show'], numbered=True)
    
    if 'create' in choices:
        mappings_path=pyip.inputFilepath(prompt="\n Enter Mappings JSON file's Full-path:")
        import es_create
        es_create.es_mapping(client,mappings_path)
    elif 'backup' in choices:
         import es_backup
         es_backup.es_backup(client)
       
    
    elif 'ingest' in choices:
        confirm_ingest=pyip.inputYesNo(prompt="\n Confirmed ingest data will not duplicate?(y/n):")
        import es_ingest
        es_ingest.es_ingest(client)
    
    elif 'update' in choices:
        
              
        res = client.search( index='trade-demo', query={'match_all': {}}, size=10000, track_total_hits=True )
        for doc in res['hits']['hits']:
                try:
                    doc_id=doc['_id']
                    record_value=doc['_source']['trade_details']['price']
                    print (doc_id,record_value)
                    doc = { 
               
                    'trade_details' : {'price': int(record_value*1.30)}
                    }
                    
                    resp = client.update(index="trade-demo", id=doc_id, doc=doc)
                    
                    try:
                        print(resp['result'])
                        print ( doc_id,int(record_value*1.30))
                        client.indices.refresh()
                    except Exception as e:
                        print("Error updating:",e)
                except Exception as e:
                    print ("Error:", e)
                    
    elif 'show' in choices:
        
        show_by= pyip.inputMenu( ['All', 'single','containing'], numbered=True)
        
        res = client.search( index='trade-demo', query={'match_all': {}}, size=10000, track_total_hits=True )
        #print (res)
        
        if 'All' in show_by:
            for doc in res['hits']['hits']:
                print (doc['_id'], doc['_source'])
                
        elif 'single' in show_by:
            show_by_single=pyip.inputStr(prompt="\n Enter record name:")
            for doc in res['hits']['hits']:
                try:
                    print (doc['_id'], doc['_source'][show_by_single])
                except Exception as e:
                    print ("Error:", e)
                    
        elif 'containing' in show_by:
            show_by_containing_record=pyip.inputStr(prompt="\n Enter record name:")
            show_by_containing_record_value=pyip.inputStr(prompt="\n Enter record value:")
            
            res = client.search(index='trade-demo', query= {'match' : {show_by_containing_record: show_by_containing_record_value } }, size=10000, track_total_hits=True )
            
            for doc in res['hits']['hits']:
                try:
                    print ( doc['_source'])
                except Exception as e:
                    print ("Error:", e)   

    choices= pyip.inputYesNo(prompt="Continue (y/n)?")
    print ("Good bye!")