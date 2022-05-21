# API Yatube

## Yatube ���������� ���� ��� ���������� ������ ���������

Yatube ���������� ���� ��� ���������� ������, � ������������ �������������� ����� ������ ���������� � ����� ������������� �� �������.

## ����������� API Yatube

- ��������� API Yatube �������� ���� ������������� ��� ������ ������ � ������������ � ���.
- API Yatube ������������� ����������� ��� ����� ������������������� ������������� ����� �������������� ���������� Token.
- ����������� ����������� �� ������ ������� ���� ������ � ������������������� �������������.
- ������������������� ������������� ������������� ����������� ������������� ���� �������� � ������� ����� ��� ������������ ������.
- ����������� ����� ����� ����� ������ ������������������� ������������.
- �������� ��� ������� ����� � ���������� ����� ������ ����� ��������.

## ��������� API Yatube

### ��� ��������� ������

- ����������� ����������� � ������� � ���� � ��������� ������:

```
git clone git@github.com:InsaraOK/api_final_yatube.git
```

```
cd api_final_yatube
```

- C������ � ������������ ����������� ���������:

```
py -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

- ���������� ����������� �� ����� requirements.txt:

```
pip install -r requirements.txt
```

- ��������� ��������:

```
python manage.py migrate
```

- ��������� ������:

```
python manage.py runserver
```

## �������

### ��������� ������� �������� � API Yatube

- ��������� ����������:
�������� ������ ���� ���������� Get-��������:

```
http://127.0.0.1:8000/api/v1/posts/
```

��� �������� � ������� ���������� limit (����� �����) - ���������� ���������� �� �������� � offset (����� �����) - ����� �������� ����� ������� �������� ������ GET-������ ������ ��� �������, � �������� �� ��������� ��� �� �������.

```
http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2 
```

- �������� JWT-�����:

```
http://127.0.0.1:8000/api/v1/jwt/create/
```

POST- ������ ������ 2 ������ ��� ����� ������ ����� � ������ � ���� �������:
"refresh": ��� �������������� ����������� ������
"access": �������� �����.

- �������� �� ������:

```
http://127.0.0.1:8000/api/v1/follow/
```

�������� ������������ �� ����� �������� ������ ������ �� ������������ ����������� � ���� �������. POST - ������� ���������� ������� � ���� ������� ���� "following": "��� ������"
> Note: ��� ������ ������ ����� ��������� � ��������� �� ��� ��������.
