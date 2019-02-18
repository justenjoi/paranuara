# Paranuara

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
- MongoDB
- Python3
```

### Installing
It is recommended that you setup a python3 virtual environment for the following;  
After cloning this repo, navigate to the directory with the `reqs.txt` file and run the following:

```
pip3 install -r reqs.txt
```

Now, open `localsettings.py` and if required, make any alterations to server addresses, ports etc to avoid port 
conflicts should you have other servers running.

Once that is done you will need to ingest the data from the JSON files into the Mongo database:  

```
python ingest_people.py

python ingest_companies.py
```

The above scripts well create the database, collections and populate all the docs as well as create whatever indexes are required.  

Now to kick off the tornado server:

```
python main.py
```

Now you should be able to make requests against the server.

## Endpoints
### Company Employees
```
/v1/company/employees
```

Params
```
- `company_name` : String of the `company` (name)
- `company_id` : Companies `index` 
```

Can send either/or

### Mutual Friends
```/v1/people/mutual_friends```

Params
```
- `people_ids` : String of people `_ids` delimited by '|'
```

### Fav fruit and veg
```/v1/people/food```

Params
```
- `person_id` : String of persons `_id`
```


### Eample requests in Postman
`http://localhost:3000/v1/company/employees?company_id=41`

`http://localhost:3000/v1/people/mutual_friends?people_ids=595eeb9b96d80a5bc7afb106|595eeb9bfa3a6e19be68df9e`

`http://localhost:3000/v1/people/food?person_id=595eeb9bfa3a6e19be68df9e`  


## Running the tests
In the directory witht he `tests.py` module;

```python -m tornado.test.runtests tests/tests.py```



## Built With

* [Tornadoweb](https://www.tornadoweb.org/en/stable/index.html)

## Potential further enhancement
* Redis caching
* Deploying with Nginx & load balancing
* Accepting fields to return as request params
* Logging & stats/metrics
