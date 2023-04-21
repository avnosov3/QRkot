from copy import deepcopy
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
ROW_COUNT = 50
COLUMN_COUNT = 10

SHEET_BODY = dict(
    properties=dict(
        title='',
        locale=LOCAL,
    ),
    sheets=[dict(properties=dict(
        sheetType=SHEET_TYPE,
        sheetId=0,
        title=SHEET_TITLE,
        gridProperties=dict(
            rowCount=ROW_COUNT,
            columnCount=COLUMN_COUNT,
        )
    ))]
)
SHEET_HEAD = [
    ['Отчет от ', ''],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]

DRIVE_VERSION = 'v3'
DRIVE_TYPE = 'user'
DRIVE_ROLE = 'writer'
EMAIL = settings.email

COLUMN_ERROR = (
    'Ожидается {} столбцов'
    'Вы передаёте "{}" столбцов'
)
ROW_ERROR = (
    'Ожидается {} строк'
    'Вы передаёте "{}" строк'
)


async def spreadsheets_create(wrapper_services: Aiogoogle):
    service = await wrapper_services.discover('sheets', SHEET_VERSION)
    body = deepcopy(SHEET_BODY)
    body['properties']['title'] = OUTUPUT_DATE.format(
        datetime.now().strftime(FORMAT)
    )
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
    head = deepcopy(SHEET_HEAD)
    head[0][1] = datetime.now().strftime(FORMAT)
    table_values = [
        *head,
        *[list(map(str, (
            project.name,
            project.close_date - project.create_date,
            project.description
        ))) for project in chatiry_projects]
    ]
    body = {
        'majorDimension': 'ROWS',
        'values': table_values,
    }
    rows = len(table_values)
    columns = max(len(row) for row in head)
    if rows > ROW_COUNT:
        raise ValueError(ROW_ERROR.format(
            ROW_COUNT, rows
        ))
    if columns > COLUMN_COUNT:
        raise ValueError(ROW_ERROR.format(
            COLUMN_COUNT, columns
        ))
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=f'R1C1:R{rows}C{columns}',
            valueInputOption='USER_ENTERED',
            json=body,
        )
    )
