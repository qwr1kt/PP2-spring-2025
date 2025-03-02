import re
import json

with open('/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab5/row.txt', 'r', encoding='utf-8') as txt:
    txt = txt.read()

def convert(text):
    json_data = {
        "branch": "",
        "bin": "",
        "nds_series": "",
        "kassa": "",
        "smena": "",
        "sequence_number": "",
        "check_number": "",
        "kassir": "",
        "items": [],
        "bank_card": "",
        "all": "",
        "nds": "",
        "fiskal": "",
        "date": "",
        "operator": "",
        "ink_ofd": "",
        "rnm": "",
        "znm": "",
    }
    
    # Филиал
    br = re.search(r'Филиал\s+(.+)', text)
    if br:
        json_data["branch"] = br.group(1).strip()

    # БИН
    bin = re.search(r'БИН (\d{10,12})', text)
    if bin:
        json_data["bin"] = bin.group(1)

    # НДС Серия
    nds_s = re.search(r'НДС Серия (\d+)', text)
    if nds_s:
        json_data["nds_series"] = nds_s.group(1)

    # Касса
    kassa = re.search(r'Касса (\d{3}-\d{3})', text)
    if kassa:
        json_data["kassa"] = kassa.group(1)

    # Смена
    smena = re.search(r'Смена (\d+)', text)
    if smena:
        json_data["smena"] = smena.group(1)

    # Порядковый номер чека
    sequence = re.search(r'Порядковый номер чека (№\d+)', text)
    if sequence:
        json_data["sequence_number"] = sequence.group(1)

    # Чек
    check = re.search(r'Чек (№\d+)', text)
    if check:
        json_data["check_number"] = check.group(1)

    # Кассир
    kassir = re.search(r'Кассир (.+)', text)
    if kassir:
        json_data["kassir"] = kassir.group(1).strip()

    # Банковская карта
    bank_card = re.search(r'Банковская карта:\n([\d\s,]+)', text, re.DOTALL)
    if bank_card:
        json_data["bank_card"] = bank_card.group(1).replace(" ", "")

    # Итого
    all = re.search(r'ИТОГО:\n([\d\s,]+)', text, re.DOTALL)
    if all:
        json_data["all"] = all.group(1).replace(" ", "")

    # НДС
    nds = re.search(r'в т.ч. НДС 12%:\n([\d\s,]+)', text, re.DOTALL)
    if nds:
        json_data["nds"] = nds.group(1).replace(" ", "")

    # Фискальный признак
    fiskal = re.search(r'Фискальный признак:\n(\d{10})', text, re.DOTALL)
    if fiskal:
        json_data["fiskal"] = fiskal.group(1)

    # Дата и время
    date = re.search(r'Время: (\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', text)
    if date:
        json_data["date"] = date.group(1)

    # Оператор
    operator = re.search(r'Оператор фискальных данных: (.+)', text)
    if operator:
        json_data["operator"] = operator.group(1).strip()

    # ИНК ОФД
    ink_ofd = re.search(r'ИНК ОФД: (\d{6})', text)
    if ink_ofd:
        json_data["ink_ofd"] = ink_ofd.group(1)

    # РНМ
    rnm = re.search(r'Код ККМ КГД \(РНМ\): (\d{12})', text)
    if rnm:
        json_data["rnm"] = rnm.group(1)

    # ЗНМ
    znm = re.search(r'ЗНМ: (\S+)', text)
    if znm:
        json_data["znm"] = znm.group(1)

    # Поиск товаров
    items_pattern = re.findall(r'(\d+)\.\n(.+?)\n([\d\s,]+) x ([\d\s,]+)\n([\d\s,]+)', text)
    for item in items_pattern:
        json_data["items"].append({
            "id": item[0],
            "name": item[1].strip(),
            "price": item[2].replace(" ", ""),
            "quantity": item[3].replace(" ", ""),
            "sum": item[4].replace(" ", "")
        })

    return json.dumps(json_data, indent=4, ensure_ascii=False)


json_output = convert(txt)
print(json_output)