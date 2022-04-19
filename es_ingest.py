import random
import datetime
def es_ingest(client):
    number_of_records=11
    while number_of_records>=1:
        trader_name=['Apple','Saudi Aramco','Microsoft','Alphabet (Google)','Gordon','Tesla','Berkshire Hathaway','Meta (Facebook)','NVIDIA','TSMC','UnitedHealth','Johnson & Johnson']
        instrument_name=['Battery','Breaks','Axle','Fuel Injector','Piston','A/C Compressor','Radiator','Engine Fan','Clutch','Jack','Transmission','Shock Absorbers','Air filter']

        number_of_records=number_of_records-1
        print(number_of_records,"number_of_records")
        trade_id = random.randrange(100,1000)
        instrument_id = random.randrange(10000,110000)
        quantity=random.randrange(50,50000)
        price=random.randrange(1000,400000)
        trading_datetime= datetime.datetime(random.randrange(1970,2022), random.randrange(1,12), random.randrange(1,28), random.randrange(00,23), random.randrange(00,59))
        trader_name=trader_name[number_of_records]
        instrument_name=instrument_name[number_of_records]
        
        
        data={ 
        'trade_id': trade_id,
        'trader_name': trader_name,
        'instrument_id': instrument_id,
        'instrument_name': instrument_name,
        'timestamps': {'trading_datetime':trading_datetime},
        'trade_details': {'quantity': quantity, 'price': price },
        }
        
        resp = client.index(index="trade-demo", document=data)
        try:
            print(resp['result'])
            client.indices.refresh()
        except Exception as e:
            print("Error ingesting data:",e)
        
            