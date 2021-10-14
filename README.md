# Random JSON Key:Value Pair Generator

This simple script take an engish dictionary of words and and makes random key value pairs.  The dictionary has approx 270k words.

## Usage:

Just run python generate.py followed by the number of key:value pairs you want to produce.


```sh
$ python generate.py 10 | jq
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

## Install

Mac:
* Requires python
* Clone repo
* run `pipenv shell && pipenv install`