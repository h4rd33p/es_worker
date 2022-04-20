
#Note: Prior use this file, “elasticsearch.yml” need to be updated to add path for snapshots repository as path.repo: ["path/to/folder"]
import arrow

def es_backup(client):

    snapshot_body = {
    "type": "fs",
    "settings": {
            "location":  "/usr/share/elasticsearch/snapshot"
        }
    }
    ts=arrow.now().strftime("%Y%b%d_%H%M%S")
    snapshot_name=(ts+'_snapshot').lower()
    #create snapshot repository 
    #client.snapshot.create_repository( name='snapshot', repository='/usr/share/elasticsearch/snapshot', body=snapshot_body)
    
    #create a snapshot
    try:
        client.snapshot.create(repository='snapshot', snapshot=snapshot_name)
    except Exception as e:
        print(e) 
    
    #show snapshot reposioties
    #print (client.snapshot.get_repository()) 