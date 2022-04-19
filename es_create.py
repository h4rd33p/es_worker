def es_mapping(client,mappings_path):
    
    with open (mappings_path, 'r') as reader:
        mappings=reader.read()
        
    resp = client.index(index="trade-demo", id=1, document=mappings)
    try:
        print(resp['result'])
    except Exception as e:
        print ("Error creating mappings:",e)
        