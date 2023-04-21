from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"
OUTUPUT_DATE = 'Отчёт на {}'
LOCAL = 'ru_RU'
SHEET_TITLE = 'Закрытые поректы'


async def spreadsheets_create(wrapper_services: Aiogoogle):
    now = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    body = {
        'properties': {
            'title': OUTUPUT_DATE.format(now),
            'locale': LOCAL
        },
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': SHEET_TITLE,
                'gridProperties': {
                    'rowCount': 100,
                    'columnCount': 11
                }
            }
        }]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=body)
    )
    spreadsheet_id = response['spreadsheetId']
    print('https://docs.google.com/spreadsheets/d/' + spreadsheet_id)
    return spreadsheet_id
