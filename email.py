import datetime

# 1. Создайте словарь email
email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
}

# 2. Добавьте дату отправки
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

# 3. Нормализуйте e-mail адреса
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

# 4. Извлеките логин и домен отправителя
login, domain = email["from"].split("@")

# 5. Создайте сокращённую версию текста
email["short_body"] = email["body"][0:10] + "..."

# 6. Списки доменов
personal_domains = {
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
}
corporate_domains = {
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
}

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений
no_domain_overlap = not (personal_domains & corporate_domains)

# 8. Проверьте «корпоративность» отправителя
is_corporate = domain in corporate_domains

# 9. Соберите «чистый» текст сообщения
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. Сформируйте текст отправленного письма
email["sent_text"] = f"""Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}, дата {email["date"]} 
{email["clean_body"]}"""

# 11. Рассчитайте количество страниц печати
pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверьте пустоту темы и тела письма
is_subject_empty = not bool(email["subject"].strip())
is_body_empty = not bool(email["body"].strip())

# 13. Создайте «маску» e-mail отправителя
email["masked_from"] = login[:2] + "***@" + domain

# 14. Удалите из списка личных доменов
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

print(f"1. Создайте словарь email:\n{email}")
print(f"2. Добавьте дату отправки: {email["date"]}")
print(f"3. Нормализуйте e-mail адреса: {email["from"]}, {email["to"]}")
print(f"4. Извлеките логин и домен отправителя: {login}, {domain}")
print(f"5. Создайте сокращённую версию текста: {email["short_body"]}")
print(f"7. Проверьте что в списке личных и корпоративных доменов нет пересечений: {no_domain_overlap}")
print(f"8. Проверьте «корпоративность» отправителя: {is_corporate}")
print(f"9. Соберите «чистый» текст сообщения:\n{email["clean_body"]}")
print(f"10. Сформируйте текст отправленного письма:\n{email["sent_text"]}")
print(f"11. Рассчитайте количество страниц печати: {pages}")
print(f"12. Проверьте пустоту темы и тела письма: {is_subject_empty}, {is_body_empty}")
print(f"13. Создайте «маску» e-mail отправителя: {email["masked_from"]}")
print(f"14. Удалите из списка личных доменов: {personal_domains}")
