import json
import uuid


SUBJECT_LIST = {
    "SubjectUUID": "",
    "SubjectID": "",
    "SubjectName": "",
    "SubjectDescription": "",
}


# TODOs
#  * UUID uuid lib
#  * SubjectID used Based on some prefix
#  * Name, self-defined

SBList = ["Algorithm A", "Algorithm B", "Operating System A",
          "Operating System B", "Data Structure A", "Data Structure B"]

SUBJECT_LIST = [{"SubjectUUID": "", "SubjectID": "201-1", "SubjectName": "Algorithm A", "SubjectDescription": "Algorithm A Description"}, {"SubjectUUID": "", "SubjectID": "201-2", "SubjectName": "Algorithm A", "SubjectDescription": "Algorithm B Description", }, {"SubjectUUID": "", "SubjectID": "202-1", "SubjectName": "Operating System A", "SubjectDescription": "Operating System A Description"},
                {"SubjectUUID": "", "SubjectID": "202-2", "SubjectName": "Operating System B", "SubjectDescription": "Operating System B Description"}, {"SubjectUUID": "", "SubjectID": "203-1", "SubjectName": "Data Structure A", "SubjectDescription": "Data Structure A Description"}, {"SubjectUUID": "", "SubjectID": "203-2", "SubjectName": "Data Structure B", "SubjectDescription": "Data Structure B Description"}]
if __name__ == '__main__':
    uuildlist = []
    for i in range(6):
        uuildlist.append(str(uuid.uuid4()))
    
    file = open("uuidlist.txt",'w+')
    
    for i in uuildlist:
        file.write(i+"\n")
    file.close