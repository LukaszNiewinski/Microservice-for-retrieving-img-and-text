# Small project for recruitment process for Semantive company.

## Usage 

Most of the responses have format:

```json
{
    "status": "success",
    "data": [
        {
            "keys": "values"
        }
    ]
}
```

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
    "status": "success",
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
    "status": "successfully created",
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

## Get retrieved text

`GET /api/text?Identifier=<identifier>`

- `identifier` is a unique id given while doing extraction(auto-incremented integer)
- `404 Not Found` if the website does not exists or failure
- `200 OK` on success

```json

[
{
    "status": "success",
    "data":   {
        "identifier": 1,
        "text": "long text..",
        "id": 1
    }
}
]
```


## Get retrieved website img

`GET /api/img?Identifier=<identifier>`

- `404 Not Found` if the text does not exists
- `200 OK` on success

[TO DO]
allows to download images?..
