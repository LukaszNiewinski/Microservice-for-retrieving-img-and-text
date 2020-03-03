# Service for collecting images and text data.

Application allows to retrieve images and text data from given website. 
Text is being stored in a database(local postgres db might be changed to remote server).
Retrieved images are being stored in AWS bucket with it's paths being stored in a db. 
Application can be started easily with one command. AWS access credentials needs to be changed.
Future work includes adding handling asynchronous requests(adding job queue) and adding tests.

## Usage 

To run: 
```docker-compose up -d --build```

Home page address: `http://localhost:5000/`





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
In process.. 


Requests examples to test api:

POST `http://localhost:5000/api/webpages`
```json
[
{"url_path": "https://pl.wikipedia.org/wiki/Lizbona",
"retrieved_text": "true",
"retrieved_img": "true"}
]
```


GET `http://localhost:5000/api/webpages`

GET `http://localhost:5000/api/text?Identifier=1 `

