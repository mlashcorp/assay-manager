import pysftp
import io

NODES = ['farm-001.local','farm-002.local','farm-003.local','farm-004.local']
NODE_CONNECTION = []
WORKLOAD_PER_NODE = []
WORKLOAD_PATH = "/home/biosurfit/workloads"

def establish_connection_to_nodes():
  for node in NODES:
    NODE_CONNECTION.append(pysftp.Connection(node,username="biosurfit",password="biosurfit"))

def disable_connection_to_nodes():
  for connection in NODE_CONNECTION:
    connection.close()
  NODE_CONNECTION = []

def generate_workload_files(workloads):
  index = 0
  file_list = []
  for load in workloads:
    io.write_list_to_file(load,"workload-"+str(index)+".csv")
    file_list.append("workload-"+str(index)+".csv")
    index += 1

    return file_list
  
def deploy_workload(experiments_list,sw_list):
  #distribute workload per node
  experiments_per_node = len(experiments_list)/len(NODES)
  
  start = 0
  for node in NODES[:-1]:
    WORKLOAD_PER_NODE.append(experiments_list[start:start+experiments_per_node])
    start += experiments_per_node
  WORKLOAD_PER_NODE.append(experiments_list[start:])
  
  workload_files = generate_workload_files(WORKLOAD_PER_NODE)
  
  for index in len(NODE_CONNECTION):
    copy_file_to_node(NODE_CONNECTION[index],workload_files[index],SERVER_WORKLOAD_PATH)
    
    
def copy_file_to_node(node_connection,input_path,target_path):
    try:
      #copy file to server
      node_connection.put(input_path,target_path)
    except:
      print "Error copying file "+str(input_path)+ " to node", sys.exc_info()[0] 
        