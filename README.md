# Random JSON Key:Value Pair Generator

This simple script take an engish dictionary of words and mand makes random key value pairs.  The dictionary is approx 270k.  

## Usage:

Just run python random_json_keypair_generator.py followed by the number of pairs you want to produce.


```sh
$ python random_json_keypair_generator.py 10 | jq                  
{
  "thundercrack": "quanted",
  "hongs": "atrophic",
  "overdrifted": "intombs",
  "earlike": "chlamydate",
  "toadpipes": "jonahs",
  "flagrantly": "infand",
  "kaliana": "nonserviceableness",
  "maidkin": "obeli",
  "beguiled": "rhetorically",
  "treponemas": "faradaic"
}
```

## Limitations

* Its does not check for duplicates.
* Its not pretty output. If you wan't it pretty pipe it to jq.
* We can't save to a file so pipe it '>' to a file if need be.