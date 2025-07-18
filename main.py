from fastapi import FastAPI ,HTTPException,Query
import json

app = FastAPI()


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
def root():
    return {"message": "Patient data"}


@app.get("/app")
def app_info():
    return {"message": "Patient Management System"}


@app.get("/view")
def view_patients():
    data = load_data()  #Get entire data
    return data

@app.get("/patient/{patient_id}")
def ViewSpecificPatient(patient_id:str):
      data = load_data() 
      if patient_id in data:
        return data[patient_id]
      raise HTTPException(status_code=404,detail='Patient Not Found')



@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data