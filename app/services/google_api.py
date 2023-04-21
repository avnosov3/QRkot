from datetime import datetime
from typing import List

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.models.charity_project import CharityProject

FORMAT = "%Y/%m/%d %H:%M:%S"

OUTUPUT_DATE = 'Отчёт на {}'
LOCAL = 'ru_RU'
SHEET_VERSION = 'v4'
SHEET_TYPE = 'GRID'
SHEET_TITLE = 'Закрытые поректы'
ROW_COUNT = 10
COLUMN_COUNT = 3

DRIVE_VERSION = 'v3'
DRIVE_TYPE = 'user'
DRIVE_ROLE = 'writer'
EMAIL = settings.email


async def spreadsheets_create(wrapper_services: Aiogoogle):
    service = await wrapper_services.discover('sheets', SHEET_VERSION)
    body = {
        'properties': {
            'title': OUTUPUT_DATE.format(
                datetime.now().strftime(FORMAT)
            ),
            'locale': LOCAL
        },
        'sheets': [{
            'properties': {
                'sheetType': SHEET_TYPE,
                'sheetId': 0,
                'title': SHEET_TITLE,
                'gridProperties': {
                    'rowCount': ROW_COUNT,
                    'columnCount': COLUMN_COUNT
                }
            }
        }]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=body)
    )
    return response['spreadsheetId']


async def set_user_permissions(
    spreadsheet_id: str,
    wrapper_services: Aiogoogle
):
    body = {
        'type': DRIVE_TYPE,
        'role': DRIVE_ROLE,
        'emailAddress': EMAIL
    }
    service = await wrapper_services.discover('drive', DRIVE_VERSION)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=body,
            fields='id',
            sendNotificationEmail=False
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str,
    chatiry_projects: List[CharityProject],
    wrapper_services: Aiogoogle
):
    service = await wrapper_services.discover('sheets', SHEET_VERSION)
    table_values = [
        ['Отчет от ', datetime.now().strftime(FORMAT)],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    for project in chatiry_projects:
        row = [
            str(project.name),
            str(project.close_date - project.create_date),
            str(project.description),
        ]
        table_values.append(row)
    body = {
        'majorDimension': 'ROWS',
        'values': table_values,
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=body,
        )
    )
