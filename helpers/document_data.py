import datetime

from config import (MTT_ACCOUNT, MTT_ADDRESS, MTT_BANK, MTT_BIK, MTT_COMPANY,
                    MTT_CORR_ACCOUNT, MTT_DOV_DATE, MTT_DOV_NUMBER, MTT_EMAIL,
                    MTT_EXOLVE, MTT_EXOLVE_URL_EN, MTT_EXOLVE_URL_RU, MTT_FIO,
                    MTT_INN, MTT_KPP, MTT_OGRN, MTT_PHONE, MTT_SHORT,
                    MTT_ZIPCODE)
from helpers.customer_gw.enum_helper import personal_doc_type_int
from helpers.generate_data import generate_date_today

documents_type = {personal_doc_type_int["PERSONAL_DOC_TYPE_PASSPORT_RF"]: "Паспорт"}


def contract_physical(email, doc_num, firstname, middlename, lastname, phone, birthdate, doc_type, number,
                      series, doc_date, issuer, factual_zipcode, factual_country, factual_address, factual_house,
                      factual_flat, factual_building, factual_frame, postal_zipcode, postal_country,
                      postal_address, postal_house, postal_flat, postal_building, postal_frame, signed=False
                      ):
    birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%dT%H:%M:%SZ").strftime("%d.%m.%Y")
    doc_date = datetime.datetime.strptime(doc_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%d.%m.%Y")
    doc_type = documents_type[doc_type]
    return f"Договор № {doc_num} от{' ' + generate_date_today()} г. Москва Сведения об {MTT_SHORT}:" \
           f" {MTT_COMPANY} " \
           f"Адрес и место нахождения: {MTT_ADDRESS} {MTT_ZIPCODE} ОГРН {MTT_OGRN} ; ИНН {MTT_INN} ; КПП {MTT_KPP} " \
           f"Банковские реквизиты: Р/с {MTT_ACCOUNT} в {MTT_BANK}, г. МОСКВА; К/с {MTT_CORR_ACCOUNT} ; БИК {MTT_BIK} " \
           f"Телефон/факс: {MTT_PHONE} ; Сведения о Пользователе - физическом лице: {lastname} {firstname} " \
           f"{middlename} Дата рождения: {birthdate} Документ удостоверяющий личность: {doc_type} Номер: {number} " \
           f"Серия: {series} Выдан: {doc_date} Кем: {issuer} Место жительства: {factual_zipcode}, {factual_country}, " \
           f"{factual_address}, д. {factual_house}, к. {factual_frame}, стр.{factual_building}, кв./ " \
           f"оф.{factual_flat}, " \
           f"Почтовый адрес (в том числе для предоставления счетов): {postal_zipcode}, {postal_country}, " \
           f"{postal_address}, д. {postal_house}, к. {postal_frame}, стр.{postal_building}, кв./ оф.{postal_flat}, " \
           f"Email (в том числе для предоставления счетов): {email} Конт.Тел.: {phone} " \
           f"ПРЕДМЕТ ДОГОВОРА: {MTT_SHORT} обязуется предоставить Пользователю право использования Платформы " \
           f"{MTT_EXOLVE} (далее - Платформа), а также Сервисов, размещенных на Платформе, путем предоставления " \
           f"удаленного доступа к ним, включая обновления и дополнительные функциональные возможности, через " \
           f"информационно- телекоммуникационную сеть, в том числе через сеть «Интернет», а также оказывать иные " \
           f"услуги, предусмотренные настоящим Договором, а Пользователь обязуется оплачивать предоставленное " \
           f"{MTT_SHORT} право и оказанные услуги в соответствии с тарифным планом, выбранным Пользователем. " \
           f"Настоящим Пользователь подтверждает, что он до заключения настоящего Договора ознакомлен и согласен со " \
           f"всеми условиями Договора, Условиями использования Платформы , Условиями оказания услуг связи {MTT_SHORT}" \
           f" , всеми приложениями к настоящему Договору, а также иными документами размещенными по адресу сайтов в " \
           f"сети «Интернет» {MTT_EXOLVE_URL_EN} и {MTT_EXOLVE_URL_RU} (далее совместно – Сайт), являющимися " \
           f"неотъемлемой частью Договора, а также то, что до него в понятной и доступной форме доведены сведения об " \
           f"основных потребительских свойствах и технических характеристиках предоставляемого права использования и " \
           f"оказываемых услуг, цены на предоставляемое право и услуги, условия использования Платформы, условия " \
           f"оказания услуг связи {MTT_SHORT}, информация об {MTT_SHORT} и территории обслуживания. " \
           f"Настоящим Пользователь выражает свое согласие на: " \
           f"- предоставление доступа к Платформе через информационно-телекоммуникационную сеть, в том числе через " \
           f"сеть «Интернет». Если не согласен - □ " \
           f"- предоставление права использования Платформы и всех Сервисов, размещенных на Платформе, оказание " \
           f"услуг. Если не согласен - □ " \
           f"- использование сведений о Пользователе для оказания справочных и иных информационных услуг {MTT_SHORT} " \
           f"или третьими лицами. Если не согласен - □ " \
           f"- передачу и поручение обработки персональных данных Пользователя (сведений о нем) третьим лицам в " \
           f"соответствии с разделом 8 Условий использования Платформы {MTT_EXOLVE}, п. 3.2 и разделом 8 Условий " \
           f"оказания услуг связи {MTT_SHORT}. Если не согласен - □ " \
           f"- возможность получения рекламной информации, распространяемой по сетям связи. Если не согласен - □ " \
           f"Тарифный план: Базовый. Условия тарифного плана указаны на Сайте. Система оплаты определяется тарифным " \
           f"планом. Форма и возможные способы оплаты указаны на Сайте. Порядок и сроки оплаты определяются тарифным " \
           f"планом, Условиями использования Платформы, Условиями оказания услуг связи {MTT_SHORT}. " \
           f"Способ доставки счетов: Личный кабинет и/или e-mail (при наличии) " \
           f"Срок обеспечения доступа к Платформе: дата заключения договора/иное. " \
           f"Способ предоставления сведений о заключенных договорах об оказании услуг: {MTT_EMAIL} " \
           f"Соответствие внесенных данных представленному документу подтверждаю. {MTT_SHORT}: / {MTT_FIO} / " \
           f"И.О.Фамилия " \
           f"{f'/ Подписано электронной подписью ' if signed else ''}" \
           f"по дов. № {MTT_DOV_NUMBER} от {MTT_DOV_DATE} М.П. " \
           f"Пользователь: / {firstname[0]}.{middlename[0]}. {lastname} / И.О.Фамилия" \
           f"{f' / Подписано электронной подписью' if signed else ''}"


def contract_entrepreneur(doc_num, firstname, middlename, lastname, birthdate, doc_type, number, series, doc_date,
                          issuer, factual_zipcode, factual_country, factual_address, factual_house, factual_flat,
                          factual_building, factual_frame, postal_zipcode, postal_country, postal_address, postal_house,
                          postal_flat, postal_building, postal_frame, contact_email, phone, ogrnip, inn, bank_name,
                          account, corr_account, bik, signer_firstname, signer_middlename, signer_lastname,
                          signed=False):
    birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%dT%H:%M:%SZ").strftime("%d.%m.%Y")
    doc_date = datetime.datetime.strptime(doc_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%d.%m.%Y")
    doc_type = documents_type[doc_type]
    return f"М.П. М.П. Договор № {doc_num} от{' ' + generate_date_today()} г. Москва Сведения об " \
           f"{MTT_SHORT}: {MTT_COMPANY} " \
           f"Адрес и место нахождения: {MTT_ADDRESS} {MTT_ZIPCODE} ОГРН {MTT_OGRN} ; ИНН {MTT_INN} ; КПП {MTT_KPP} " \
           f"Банковские реквизиты: Р/с {MTT_ACCOUNT} в {MTT_BANK}, г. МОСКВА; К/с {MTT_CORR_ACCOUNT} ; БИК {MTT_BIK} " \
           f"Телефон/факс: {MTT_PHONE} ; " \
           f"Сведения о Пользователе - индивидуальном предпринимателе: {lastname} {firstname} {middlename} Дата " \
           f"рождения: {birthdate} Документ удостоверяющий личность: {doc_type} Номер: {number} Серия: {series} " \
           f"Выдан: {doc_date} Кем: {issuer} " \
           f"Место жительства: {factual_zipcode}, {factual_country}, {factual_address}, д. {factual_house}, " \
           f"к. {factual_frame}, стр.{factual_building}, кв./ оф.{factual_flat}, " \
           f"Почтовый адрес (в том числе для предоставления счетов): {postal_zipcode}, {postal_country}, " \
           f"{postal_address}, д. {postal_house}, к. {postal_frame}, стр.{postal_building}, кв./ оф.{postal_flat}, " \
           f"Email (в том числе для предоставления счетов): {contact_email} Конт.Тел.: {phone} ОГРНИП: {ogrnip} " \
           f"ИНН: {inn} Банковские реквизиты: Банк: {bank_name} ; Р/с: {account} ; К/с: {corr_account} ; БИК: {bik} " \
           f"ПРЕДМЕТ ДОГОВОРА: {MTT_SHORT} обязуется предоставить Пользователю право использования Платформы " \
           f"{MTT_EXOLVE} (далее - Платформа), а также Сервисов, размещенных на Платформе, путем предоставления " \
           f"удаленного доступа к ним, включая обновления и дополнительные функциональные возможности, через " \
           f"информационно- телекоммуникационную сеть, в том числе через сеть «Интернет», а также оказывать иные " \
           f"услуги, предусмотренные настоящим Договором, а Пользователь обязуется оплачивать предоставленное " \
           f"{MTT_SHORT} право и оказанные услуги в соответствии с тарифным планом, выбранным Пользователем. " \
           f"Настоящим Пользователь подтверждает, что он до заключения настоящего Договора ознакомлен и согласен со " \
           f"всеми условиями Договора, Условиями использования Платформы , Условиями оказания услуг связи {MTT_SHORT}" \
           f" , всеми приложениями к настоящему Договору, а также иными документами размещенными по адресу сайтов в " \
           f"сети «Интернет» {MTT_EXOLVE_URL_EN} и {MTT_EXOLVE_URL_RU} (далее совместно – Сайт), являющимися " \
           f"неотъемлемой частью Договора, а также то, что до него в понятной и доступной форме доведены сведения об " \
           f"основных потребительских свойствах и технических характеристиках предоставляемого права использования и " \
           f"оказываемых услуг, цены на предоставляемое право и услуги, условия использования Платформы, условия " \
           f"оказания услуг связи {MTT_SHORT}, информация об {MTT_SHORT} и территории обслуживания. " \
           f"Настоящим Пользователь выражает свое согласие на: " \
           f"- предоставление доступа к Платформе через информационно-телекоммуникационную сеть, в том числе через " \
           f"сеть «Интернет». Если не согласен - □ " \
           f"- предоставление права использования Платформы и всех Сервисов, размещенных на Платформе, оказание " \
           f"услуг. Если не согласен - □ " \
           f"- использование сведений о Пользователе для оказания справочных и иных информационных услуг {MTT_SHORT} " \
           f"или третьими лицами. Если не согласен - □ " \
           f"- передачу и поручение обработки персональных данных Пользователя (сведений о нем) третьим лицам в " \
           f"соответствии с разделом 8 Условий использования Платформы {MTT_EXOLVE}, п. 3.2 и разделом 8 Условий " \
           f"оказания услуг связи {MTT_SHORT}. Если не согласен - □ " \
           f"- возможность получения рекламной информации, распространяемой по сетям связи. Если не согласен - □ " \
           f"Тарифный план: Базовый. Условия тарифного плана указаны на Сайте. Система оплаты определяется тарифным " \
           f"планом. Форма и возможные способы оплаты указаны на Сайте. Порядок и сроки оплаты определяются тарифным " \
           f"планом, Условиями использования Платформы, Условиями оказания услуг связи {MTT_SHORT}. " \
           f"Способ доставки счетов: Личный кабинет и/или e-mail (при наличии) " \
           f"Срок обеспечения доступа к Платформе: дата заключения договора/иное. " \
           f"Способ предоставления сведений о заключенных договорах об оказании услуг: {MTT_EMAIL} " \
           f"Соответствие внесенных данных представленному документу подтверждаю. {MTT_SHORT}: / {MTT_FIO} / " \
           f"И.О.Фамилия " \
           f"{f'/ Подписано электронной подписью ' if signed else ''}" \
           f"по дов. № {MTT_DOV_NUMBER} от {MTT_DOV_DATE} " \
           f"Пользователь: / " \
           f"{signer_firstname[0]}.{signer_middlename[0]}. {signer_lastname} / И.О.Фамилия" \
           f"{f' / Подписано электронной подписью' if signed else ''}"


def contract_juridical(doc_num, company_name, factual_zipcode, factual_country, factual_address, factual_house,
                       factual_flat, factual_building, factual_frame, postal_zipcode, postal_country, postal_address,
                       postal_house, postal_flat, postal_building, postal_frame, contact_email, phone, ogrn, inn, kpp,
                       bank_name, account, corr_account, bik, signer_firstname, signer_middlename, signer_lastname,
                       signed=False):
    return f"М.П. М.П. Договор № {doc_num} от{' ' + generate_date_today()} г. Москва Сведения об " \
           f"{MTT_SHORT}: {MTT_COMPANY} " \
           f"Адрес и место нахождения: {MTT_ADDRESS} {MTT_ZIPCODE} ОГРН {MTT_OGRN} ; ИНН {MTT_INN} ; КПП {MTT_KPP} " \
           f"Банковские реквизиты: Р/с {MTT_ACCOUNT} в {MTT_BANK}, г. МОСКВА; К/с {MTT_CORR_ACCOUNT} ; БИК {MTT_BIK} " \
           f"Телефон/факс: {MTT_PHONE} ; " \
           f"Сведения о Пользователе - юридическом лице: " \
           f"Сокращенное наименование {company_name} " \
           f"Место нахождения: {factual_zipcode}, {factual_country}, {factual_address}, д. {factual_house}, " \
           f"к. {factual_frame}, стр.{factual_building}, кв./ оф.{factual_flat}, " \
           f"Почтовый адрес (в том числе для предоставления счетов): {postal_zipcode}, {postal_country}, " \
           f"{postal_address}, д. {postal_house}, к. {postal_frame}, стр.{postal_building}, кв./ оф.{postal_flat}, " \
           f"Email (в том числе для предоставления счетов): {contact_email} Конт.Тел.: {phone} " \
           f"ОГРН: {ogrn} ИНН: {inn} КПП: {kpp} " \
           f"Банковские реквизиты: " \
           f"Р/с: {account} " \
           f"в {bank_name} " \
           f"К/с: {corr_account} ; БИК: {bik} " \
           f"ПРЕДМЕТ ДОГОВОРА: {MTT_SHORT} обязуется предоставить Пользователю право использования Платформы " \
           f"{MTT_EXOLVE} (далее - Платформа), а также Сервисов, размещенных на Платформе, путем предоставления " \
           f"удаленного доступа к ним, включая обновления и дополнительные функциональные возможности, через " \
           f"информационно- телекоммуникационную сеть, в том числе через сеть «Интернет», а также оказывать иные " \
           f"услуги, предусмотренные настоящим Договором, а Пользователь обязуется оплачивать предоставленное " \
           f"{MTT_SHORT} право и оказанные услуги в соответствии с тарифным планом, выбранным Пользователем. " \
           f"Настоящим Пользователь подтверждает, что он до заключения настоящего Договора ознакомлен и согласен со " \
           f"всеми условиями Договора, Условиями использования Платформы , Условиями оказания услуг связи {MTT_SHORT}" \
           f" , всеми приложениями к настоящему Договору, а также иными документами размещенными по адресу сайтов в " \
           f"сети «Интернет» {MTT_EXOLVE_URL_EN} и {MTT_EXOLVE_URL_RU} (далее совместно - Сайт), являющимися " \
           f"неотъемлемой частью Договора, а также то, что до него в понятной и доступной форме доведены сведения об " \
           f"основных потребительских свойствах и технических характеристиках предоставляемого права использования и " \
           f"оказываемых услуг, цены на предоставляемое право и услуги, условия использования Платформы, условия " \
           f"оказания услуг связи {MTT_SHORT}, информация об {MTT_SHORT} и территории обслуживания. " \
           f"Настоящим Пользователь выражает свое согласие на: " \
           f"- предоставление доступа к Платформе через информационно-телекоммуникационную сеть, в том числе через " \
           f"сеть «Интернет». Если не согласен — □ " \
           f"- предоставление права использования Платформы и всех Сервисов, размещенных на Платформе, оказание " \
           f"услуг. Если не согласен - □ " \
           f"- использование сведений о Пользователе для оказания справочных и иных информационных услуг {MTT_SHORT} " \
           f"или третьими лицами. Если не согласен - □ " \
           f"- передачу и поручение обработки персональных данных Пользователя (сведений о нем) третьим лицам в " \
           f"соответствии с разделом 8 Условий использования Платформы {MTT_EXOLVE}, п. 3.2 и разделом 8 Условий " \
           f"оказания услуг связи {MTT_SHORT}. Если не согласен - □ " \
           f"- возможность получения рекламной информации, распространяемой по сетям связи. Если не согласен - □ " \
           f"Тарифный план: Базовый. Условия тарифного плана указаны на Сайте. Система оплаты определяется тарифным " \
           f"планом. Форма и возможные способы оплаты указаны на Сайте. Порядок и сроки оплаты определяются тарифным " \
           f"планом, Условиями использования Платформы, Условиями оказания услуг связи {MTT_SHORT}. " \
           f"Способ доставки счетов: Личный кабинет и/или e-mail (при наличии) " \
           f"Срок обеспечения доступа к Платформе: дата заключения договора/иное. " \
           f"Способ предоставления сведений о заключенных договорах об оказании услуг: {MTT_EMAIL} " \
           f"Соответствие внесенных данных представленному документу подтверждаю. {MTT_SHORT}: {MTT_FIO} / / " \
           f"И.О.Фамилия" \
           f"{f' / Подписано электронной подписью ' if signed else ''}" \
           f"по дов. № {MTT_DOV_NUMBER} от {MTT_DOV_DATE} " \
           f"Пользователь: {signer_firstname[0]}.{signer_middlename[0]}. {signer_lastname} / И.О.Фамилия" \
           f"{f' / Подписано электронной подписью' if signed else ''}"
