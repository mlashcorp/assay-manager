import sys
from datetime import datetime
from jc_data import JCResults

def get_results(file):
#Get master file ids in correct format
    results = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            #substr = re.findall(r"[\w-]+_\d\d?",line)
            splitted = line.split(',')
            jc_id = splitted[0]
            date = datetime.strptime(splitted[1], '%d-%m-%Y')
            assay_number1 = splitted[2]
            assay_number2 = splitted[3]
            results1 = splitted[4:10]
            results2 = splitted[10:]
            result = JCResults(jc_id,assay_number1,assay_number2,date,results1,results2)
            results.append(result)
    return results
	

