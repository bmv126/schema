Simple Flask app which validates the json data provided by user.

GET Method: Retrieves the schema.

curl -X GET http://localhost:5000/api/v1/
```json
{
  "$id": "http://example.com/root.json", 
  "$schema": "http://json-schema.org/draft-07/schema#", 
  "definitions": {}, 
  "properties": {
    "key1": {
      "$id": "#/properties/abcd", 
      "default": 0, 
      "examples": [
        1
      ], 
      "title": "The Key1 Schema", 
      "type": "integer"
    }, 
    "key2": {
      "$id": "#/properties/def", 
      "default": 0, 
      "examples": [
        2
      ], 
      "title": "The Key2 Schema", 
      "type": "integer"
    }
  }, 
  "required": [
    "key1", 
    "key2"
  ], 
  "title": "The Root Schema", 
  "type": "object"
}
```

Post Method:

curl -d '{"key1":10, "key2":20}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/v1/
```json
{
  "InputJson": "valid"
}
```

curl -d '{"key":10, "key2":20}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/v1/
```json
{
  "InputJson": "Invalid"
}
```


