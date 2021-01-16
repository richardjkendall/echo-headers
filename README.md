# echo-headers
Flask app which echos the request headers as JSON back to the client.

Very simple!

## To run

1. Clone the repo
2. Create a venv ``python3 -m venv .env`` and activate ``source .env/bin/activate``
3. Install dependencies ``pip install -r requirements.txt``
4. Run ``gunicorn -w 4 app:app``

## Via Docker

```bash
docker run --rm\
 -p 5000:5000 \
 -d \
 richardjkendall/echo-headers
```
