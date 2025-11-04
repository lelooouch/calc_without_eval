from datetime import datetime, date
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

gooods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': date(2023, 7, 15)},
        {'amount': Decimal('2'), 'expiration_date': date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}


def add(title, amount, expiration_date=None):
    if title not in gooods:
        gooods[title] = []
    gooods[title].append({
        'amount': amount,
        'expiration_date': expiration_date
    })
    print(gooods)


def add_by_note(note):
    parts = note.split()
    if not parts:
        print('Элементов нет.')
        return


    expiration_date = None
    if len(parts) >= 2:
        try:
            expiration_date = datetime.strptime(parts[-1], DATE_FORMAT).date()
            parts = parts[:-1]
        except ValueError:
            pass

    if len(parts) < 2:
        raise ValueError("Недостаточно данных для добавления продукта")
    try:
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])
    except:
        raise ValueError("Неверный формат")
    add(title, amount, expiration_date)


def find(name):
    name = name.lower()
    result = []
    for title in gooods:
        if name in title.lower():
            result.append(title)
    return result


def amount(title):
    titles = find(title)
    total = Decimal('0')
    for t in titles:
        for batch in goods[t]:
            total += batch['amount']
    return total

