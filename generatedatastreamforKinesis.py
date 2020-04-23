import boto3
import json
from datetime import datetime
import calendar
import random
import time

my_stream_name = 'kdg_datastream'

kinesis_client = boto3.client('kinesis')


def put_to_stream(vehiclenumber, vehicle_returned, kms_driven, rating, customer,vehicle_type):
    ridedetails = {
        'vehiclenumber': str(vehiclenumber),
        'vehicle_returned': str(vehicle_returned),
        'kms_driven': str(kms_driven),
        'rating': str(rating),
        'customer': str(customer),
        'vehicle_type': vehicle_type
    }

    print(ridedetails)

    put_response = kinesis_client.put_record(
        StreamName=my_stream_name,
        Data=json.dumps(ridedetails),
        PartitionKey=vehicle_type)


while True:
    vehiclenumber = random.randint(40, 120)
    vehicle_returned = calendar.timegm(datetime.utcnow().timetuple())
    kms_driven = random.randint(10, 200)
    rating_list = ['Good', 'Bad', 'Average']
    rating = random.choice(rating_list)
    customer_list = ["OLIVIA","RUBY",
                     "EMILY",
                     "GRACE",
                     "JESSIC",
                     "CHLOE",
                     "SOPHIE",
                     "LILY",
                     "AMELIA",
                     "EVIE",
                     "MIA",
                     "ELLA",
                     "CHARLO",
                     "LUCY",
                     "MEGAN",
                     "ELLIE",
                     "ISABEL",
                     "ISABEL",
                     "HANNAH",
                     "KATIE",
                     "AVA",
                     "HOLLY",
                     "SUMMER",
                     "MILLIE",
                     "DAISY",
                     "PHOEBE",
                     "FREYA",
                     "ABIGAI",
                     "POPPY",
                     "ERIN",
                     "EMMA",
                     "MOLLY",
                     "IMOGEN",
                     "AMY",
                     "JASMIN",
                     "ISLA",
                     "SCARLE",
                     "LEAH",
                     "SOPHIA",
                     "ELIZAB",
                     "EVA",
                     "BROOKE",
                     "MATILD",
                     "CAITLI",
                     "KEIRA",
                     "ALICE",
                     "LOLA",
                     "LILLY",
                     "AMBER",
                     "ISABEL",
                     "LAUREN",
                     "GEORGI",
                     "GRACIE",
                     "ELEANO",
                     "BETHAN",
                     "MADISO",
                     "AMELIE",
                     "ISOBEL",
                     "PAIGE",
                     "LACEY",
                     "SIENNA",
                     "LIBBY",
                     "MAISIE",
                     "ANNA",
                     "REBECC",
                     "ROSIE",
                     "TIA",
                     "LAYLA",
                     "MAYA",
                     "NIAMH",
                     "ZARA",
                     "SARAH",
                     "LEXI",
                     "MADDIS",
                     "ALISHA",
                     "SOFIA",
                     "SKYE",
                     "NICOLE",
                     "LEXIE",
                     "FAITH",
                     "MARTHA",
                     "HARRIE",
                     "ZOE",
                     "EVE",
                     "JULIA",
                     "AIMEE",
                     "HOLLIE",
                     "LYDIA",
                     "EVELYN",
                     "ALEXAN",
                     "MARIA",
                     "FRANCE",
                     "TILLY",
                     "FLOREN",
                     "ALICIA",
                     "ABBIE",
                     "EMILIA",
                     "COURTN",
                     "MARYAM",
                     "0ESME"]
    customer = [random.choice(customer_list)]
    vehicle_type = 'car'

    put_to_stream(vehiclenumber, vehicle_returned, kms_driven, rating , customer,vehicle_type)

    # wait for 5 second
    #time.sleep(1)
