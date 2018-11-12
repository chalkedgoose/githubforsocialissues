# Project Pescadero

## Servers
---
### API Setup
- Requirements: Python >= 3.5 `python3 -V` and [MongoDB](https://www.mongodb.com/download-center).
- Install dependencies on a virtualenv `python3 -m pip install --user virtualenv`:

```sh
cd servers/api
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
### Run API Development Server
```sh
bash start-dev.sh
```

## Client
---
### Client Setup
- Requirements: Node >= 10.11 `node -v`

```sh
cd client
npm install
```
### Run Client Development Server
```sh
gatsby develop
```
