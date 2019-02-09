# REST API using python 3.7 and SQLite3
## Setup

* Edit the settings.py file to suit your database needs.
* Run pip to install the required python modules from the requirements.txt.
* change the path in app.wsgi to comply woth your server
* Deploy the web server using apache2 and mod_wsgi (link to app.wsgi).

***
## Documentation
***
### Standard return
***Definition***

Every request has a standard JSON return. every return follows the format below:

```JSON {
    "Return": "OK",
    "Content": {
        "ID": 1,
        "name": "John Doe",
        "email": "John.Doe@company.com",
        "phone": "555-555-555",
    }
}
```
***
### GET requests
#### Retrieve all
***Definition***

A GET request to the endpoints '/' or '/retrieve' will return a list of all data stored in the database.

***Response***

```JSON {
    "Return": "OK",
    "Content": [
        {
            "ID": 1,
            "name": "John Doe",
            "email": "John.Doe@company.com",
            "phone": "555-555-555"
        },
        {
            "ID": 1,
            "name": "John Doe",
            "email": "John.Doe@company.com",
            "phone": "555-555-555"
        }
    ]
}
```

#### Retrieve one
***Definition***

A GET request to the endpoint '/<int: id>' or '/retrieve/<int: id>' will return the data stored in the database at that ID.

***Response***

```JSON {
    "Return": "OK",
    "Content": 
        {
            "ID": 1,
            "name": "John Doe",
            "email": "John.Doe@company.com",
            "phone": "555-555-555"
        }
}
```

***
### POST requests
***Definition***

A POST request to the endpoints '/' or '/post' will store the data in the request body in the database. The request data needs to be in the JSON format, otherwise an error will occur. The API responds by echoing the stored data.

***Response***

```JSON {
    "Return": "CREATED",
    "Content": 
        {
            "ID": 1,
            "name": "John Doe",
            "email": "John.Doe@company.com",
            "phone": "555-555-555"
        }
}
```

***
### PUT requests
***Definition***

A PUT request to the endpoints '/<int: id>' or '/post/<int: id>' will update the table data at that ID. The API responds by echoing the new data in the table.

***Response***

```JSON {
    "Return": "UPDATED",
    "Content": 
        {
            "ID": 1,
            "name": "John Doe",
            "email": "John.Doe@company.com",
            "phone": "555-555-555"
        }
}
```

***
### DELETE requests
#### Reset table
***Definition***

A DELETE request to the endpoint '/reset' will reset the entire table, all data will be deleted.

*THIS IS IRREVERSIBLE!*

Be careful using this request.

***Response***

```JSON {
    "Return": "RESET",
    "Content": []
}
```

#### Delete one entry
***Definition***

A DELETE request to the endpoints '/<int: id>' or '/delete/<int: id>' will delete the entry at the ID. The API responds by issuing a JSON response.

***Response***

```JSON {
    "Return": "DELETED",
    "Content": {}
}
```

***
## Author
Tijmen Verhoef,

https://www.tverhoef.com