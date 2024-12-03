print('lllllllllllllllllllllllllllllllllllllllllll')

import json
class Employee:
    def __init__(self,emp_id,name,designation):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation


## Each one of the function has SINGLE RESPONSIBILITY
## You can write extension to this code example like formats


class RecordSerializer:
    def serialize(self,emp_rec,formatt):
        serializer = self._get_serializer(formatt)
        return serializer(emp_rec)

    def _get_serializer(self,formatt): ## Factory Method which initializes the Serializer Method
        if formatt == "JSON":
            return self._serialize_to_json
        elif formatt == "CSV":
            return self._serialize_to_csv
        else:
            raise ValueError(formatt)
    
    def _serialize_to_json(self,emp_rec):
        emp_info = {
            'empid':emp_rec.emp_id,
            'name':emp_rec.name,
            'designation':emp_rec.designation
        }
        return json.dumps(emp_info)
    
    def _serialize_to_csv(self,emp_rec):
        return [emp_rec.emp_id,emp_rec.name,emp_rec.designation]
    



if __name__ == '__main__':

    emp1 = Employee('20522421','Karnika Srinath','Sr.Software Dev')
    print(emp1)
    emp2 = Employee('20522422','Karnika Srikanth','Sr.Software Dev')
    print(emp2)


    rec_ser = RecordSerializer()
    rec_ser.serialize(emp1,"JSON")
    rec_ser.serialize(emp2,"CSV")