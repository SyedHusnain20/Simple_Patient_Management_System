from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

import json

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='Enter patient ID here ', examples=['P001'])]
    name:  Annotated[str, Field(..., description='Enter patient Name here ')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Enter patient Age here ')]
    city: Annotated[str, Field(..., description='Enter the city where patient is living ')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Enter height of the patient in meters')]
    weight: Annotated[float, Field(..., gt=0, description='Enter weight of the patient in Kgs')]

    @computed_field
    @property
    def bmi(self)->float:
        cal_bmi = round(self.weight/(self.height**2),2)
        return cal_bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'underweight'
        elif self.bmi < 30:
            return 'normal'
        else:
            return 'Obese'


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(gt=0, lt=120, default=None)]
    gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]

app = FastAPI()

def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)



@app.get("/")
def GET_Request():
    return {"message": "Patient Management System API"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/view/{patient_id}')
def patient(patient_id: str = Path(..., description = "Please Enter patient ID here ! ", examples = "P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code = 404, detail = "Patient not found")
    

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = "sort the patients on the basis of height, weight, or bmi"),
                  order: str = Query('asc', description = "sort in ascending or descending order ")
):
    
    valid_fields = ['height','weight','bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = "kindly select only between height, weight, or bmi")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = "kindly select only asc or desc")

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(),key= lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):

    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code = 400, detail= 'Patient ID already exist! Please enter another ID')
    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201, content={'message':'Patient added sucessfully'})
    

@app.put('/edit/{patient_id}')
def edit_patient(patient_id: str, patient_data: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found! please re-enter the correct ID')
    
    existing_data = data[patient_id]
    updated_data = patient_data.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        existing_data[key] = value

    existing_data['id'] = patient_id
    ed_pydantic_object = Patient(**existing_data)

    existing_data = ed_pydantic_object.model_dump(exclude='id')
    data[patient_id] = existing_data

    save_data(data)

    return JSONResponse(status_code= 201, content= {'message':'Patient Updated Successfully'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found! please re-enter the correct ID')
    
    del data[patient_id]

    save_data(data) 

    return JSONResponse(status_code=200, content={'message': 'Patient deleted Successfully'})