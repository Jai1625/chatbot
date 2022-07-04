# if __name__ == '__main__':
#     import requests
#
#     url = 'https://dev-kfdw-040.app.zingworks.com/role/2/Ac5EkN1bPfKD/count'
#     headers = {
#         'X-Access-Key-Id': 'Ak05e720dd-729d-4152-aca6-99a384a46dbb',
#         'X-Access-Key-Secret': '3oG-iINrsUqmtcR04ETmKzhVTga5KZSGxg0ib41--Ztz1zJ07YmvyS8JsCI-izJTTysC8h0yV28HitwaoREJw'
#     }
#     data = requests.get(url, headers=headers)
#     print(data.json())

import requests
import asyncio
from timeit import default_timer
from concurrent.futures import ThreadPoolExecutor

START_TIME = default_timer()

key_100 = "form/Appointment_Request_Form_1/import/Attach_1so0yopmI/100 rows spreadsheet - Sheet1.csv"
key_1000 = "form/Appointment_Request_Form_1/import/Attach_YMbgKZH2e/1000 rows spreadsheet - Sheet1.csv"
key_5000 = "form/Appointment_Request_Form_1/import/Attach_2YPN3gFOB/5000 rows spreadsheet - Sheet1.csv"

json = {
    "fields_configured": [
        {
            "csv_key": "Title",
            "mapped_field": "Title",
            "type": "Select"
        },
        {
            "csv_key": "FirstName",
            "mapped_field": "First_name",
            "type": "Text"
        },
        {
            "csv_key": "MobNumber",
            "mapped_field": "Mobile_number",
            "type": "Number"
        },
        {
            "csv_key": "LastName",
            "mapped_field": "Last_name",
            "type": "Text"
        },
        {
            "csv_key": "Email",
            "mapped_field": "Email_1",
            "type": "Email"
        },
        {
            "csv_key": "Address line 1",
            "mapped_field": "Address_line_1",
            "type": "Text"
        },
        {
            "csv_key": "Address line 2",
            "mapped_field": "Address_line_2_1",
            "type": "Text"
        },
        {
            "csv_key": "City",
            "mapped_field": "City",
            "type": "Text"
        },
        {
            "csv_key": "PostalCode",
            "mapped_field": "Postal__Zip_code_1",
            "type": "Text"
        },
        {
            "csv_key": "State",
            "mapped_field": "State__Province",
            "type": "Text"
        }
    ],
    "abort_on_error": False,
    "insert_only": True,
    "delete_missing": False,
    "csv_file": {
        "uploaded": 100,
        "name": "1000 rows spreadsheet - Sheet1.csv",
        "id": "Attach_YMbgKZH2e",
        "key": "Ac5EkN1bPfKD/form/Appointment_Request_Form_1/import/Attach_YMbgKZH2e/1000 rows spreadsheet - Sheet1.csv",
        "size": 7892,
        "fileExtension": "csv"
    }
}

headers = {
    'X-Access-Key-Id': 'Ak05e720dd-729d-4152-aca6-99a384a46dbb',
    'X-Access-Key-Secret': '3oG-iINrsUqmtcR04ETmKzhVTga5KZSGxg0ib41--Ztz1zJ07YmvyS8JsCI-izJTTysC8h0yV28HitwaoREJw'
}


def request(session, i):
    url = "https://dev-kfdw-040.app.zingworks.com/form/2/Ac5EkN1bPfKD/Appointment_Request_Form_{form_number}/import?_application_id=load_test_application".format(
        form_number=str(i))
    with session.post(url=url, headers=headers, json=json) as response:
        data = response.text

        if response.status_code != 200:
            print("FAILURE::{0}".format(url))

        elapsed_time = default_timer() - START_TIME
        completed_at = "{:5.2f}s".format(elapsed_time)
        print("{0:<30} {1:>20}".format(i, completed_at))
        return data


async def start_async_process():
    print("{0:<30} {1:>20}".format("No", "Completed at"))
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            START_TIME = default_timer()
            tasks = [
                loop.run_in_executor(
                    executor,
                    request,
                    *(session, i)
                )
                for i in range(12, 17)
            ]
            for response in await asyncio.gather(*tasks):
                pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(start_async_process())
    loop.run_until_complete(future)
