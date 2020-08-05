import json
from uk_covid19 import Cov19API

swindon = [
    "areaType=ltla",
	"areaName=swindon"
]

cases = {
	"date":"date",
	"areaName":"areaName",
	"newCasesBySpecimenDate":"newCasesBySpecimenDate",
	"cumCasesBySpecimenDate":"cumCasesBySpecimenDate"
}

def lambda_handler(event, context):
    api = Cov19API(filters=swindon, structure=cases)
    data = api.get_csv()

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/csv',
            'Content-disposition': 'attachment; filename=swindon.csv'
        },
        'body': data
    }
