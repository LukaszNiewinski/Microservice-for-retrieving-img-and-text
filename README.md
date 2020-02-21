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
{
    "status": "success, list of all the webpages",
    "data": [
        {
            "retrieved_text": true,
            "created_at": "2020-02-20T05:20:58.793149",
            "retrieved_img": true,
            "url_path": "www.google.com",
            "identifier": 1
        },
        {
            "retrieved_text": true,
            "created_at": "2020-02-20T05:21:46.474182",
            "retrieved_img": true,
            "url_path": "www.google.com",
            "identifier": 2
        }
    ]
}
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
    "status": "successfully created, data will be retrieved",
    "data": {
        "identifier": 1,
        "retrieved_text": true,
        "retrieved_img": true,
        "created_at": "2020-02-20T07:22:52.550194",
        "url_path": "http://google.com"
    }
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
    "identifier": 1,
    "url_path": "www.google.com",
    "retrieved_text": "True",
    "retrieved_img": "True"
  }
]
```

`"text_num": "number"` <-- number of words extracted

`"img_num": "number"` <-- number of img extracted

## Get retrieved website text

`GET /api/webpages_text/<identifier>`

- `404 Not Found` if the text does not exists
- `200 OK` on success

```json
[
  {
    "identifier": 1,
    "url_path": "www.google.com",
    "text": "array of words"
  }
]
```


## Get retrieved website img

`GET /api/webpages_img/<identifier>`

- `404 Not Found` if the text does not exists
- `200 OK` on success

[TO DO]
allows to download images?..
