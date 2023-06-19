# schema_methods.py - файл со схемами ответов для каждого метода

# Входные параметры
# Name	Type	Description	Required	Comment
# application_name	string	Название приложения	да

# application_description	string	Описание приложения	нет
# Выходные параметры
# Name	Type	Description
# application_uuid	string	Уникальный id приложения
# application_name	string	Название приложения
# application_description	string	Описание приложения
# application_token	array<ApplicationToken>
# ApplicationToken. Структура хранящая данные токена приложения. (API ключ с сайта Exolve)
#
# Name	Type	Description
# session_state	string	Уникальный идентификатор токена  (uuid)
# token	string	Токен приложения
# start	datetime in ISO 8601	Дата создания

schema_response_create_application = {
    "type": "object",
    "properties": {
        "application_uuid": {
            "type": "string"
        },
        "application_name": {
            "type": "string"
        },
        "application_description": {
            "type": "string"
        },
        "application_token": {
            "type": "object",
            "required": [
                "session_state",
                "token",
                "start"
            ]
        },
        "properties": {
            "session_state": {
                "type": "string"
            },
            "token": {
                "type": "string"
            },
            "start": {
                "type": "string"
            }
        }
    },
    "required": [
        "application_uuid",
        "application_name",
        "application_description",
        "application_token"
    ]
}


schema_response_get_application_token = {
    "type": "object",
    "required": [
        "application_tokens"
    ],
    "properties": {
        "application_tokens": {
            "type": "array",
            "required": [
                "session_state",
                "token",
                "start"
            ]
        },
        "properties": {
            "session_state": {
                "type": "string"
            },
            "token": {
                "type": "string"
            },
            "start": {
                "type": "string"
            }
        }
    }
}
# ApplicationToken. Структура хранящая данные токена приложения. (API ключ с сайта Exolve)
# Name	Type	Description
# session_state	string	Уникальный идентификатор токена  (uuid)
# token	string	Токен приложения
# start	datetime in ISO 8601	Дата создания

schema_response_renew_application_token = {
    "type": "object",
    "application_token": {
        "type": "array",
        "required": [
            "session_state",
            "token",
            "start"
        ]
    },
    "properties": {
        "session_state": {
            "type": "string"
        },
        "token": {
            "type": "string"
        },
        "start": {
            "type": "string"
        }
    }
}


schema_response_error = {
    "type": "object",
    "required": [
        "error"
    ],
    "properties": {
        "error": {
            "type": "string",
        }
    }
}
