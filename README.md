# Small project for recruitment process for Semantive company.

## Usage 

Application is built on the services:
- img_retrieve_service
- text_retrieve_service
- webpage_service 
- db(postgresql)

To run: 
```docker-compose build```
```docker-compose up```

### List all websites retrieved 

**Websites collection definition**

`GET /api/webpages`

**Response** 

- `200 OK` on success

```json
[
  {
    "identifier": "0",
    "url_path": "www.google.com",
    "retrieved_text": "Yes",
    "retrieved_img": "Yes"
  },
    {
    "identifier": "1",
    "url_path": "www.wp.pl",
    "retrieved_text": "Yes", 
    "retrieved_img": "No"
  }
]
```

### Add new website

**Add resource definition**

`POST /api/webpages`

**Arguments**

- `"url_path":string` - a globally unique identifier
- `"retrieved_text":bool` - flag that defines retrieving text
- `"retrieved_img":bool` - flag that defines retrieving text

**Response**

- `201 Created` on success

```json
[
  {
    "identifier": "0",
    "url_path": "www.google.com",
    "retrieved_text": "Yes",
    "retrieved_img": "Yes"
  }
]
```

## Get retrieved website details

`GET /api/webpages/<identifier>`

- `404 Not Found` if the website does not exists
- `200 OK` on success

```json
[
  {
    "identifier": "0",
    "url_path": "www.google.com",
    "retrieved_text": "Yes",
    "retrieved_img": "Yes",
    "text_num": "number",
    "img_num": "number" 
  }
]
```

`"text_num": "number"` <-- number of words extracted

`"img_num": "number"` <-- number of img extracted

## Get retrieved website text

`GET /api/webpages/<identifier>/text`

- `404 Not Found` if the text does not exists
- `200 OK` on success

```json
[
  {
    "identifier": "0",
    "url_path": "www.google.com",
    "text": "array of words"
  }
]
```


## Get retrieved website img

`GET /api/webpages/<identifier>/img`

- `404 Not Found` if the text does not exists
- `200 OK` on success

[TO DO]
allows to download images?..
