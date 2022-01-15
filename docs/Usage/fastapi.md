# FastAPI

```python
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from discord_oauth2 import DiscordAuth

client_id = "id"
client_secret = "secret"
callback_url = "url"

discord_auth = DiscordAuth(client_id, client_secret, callback_url)


app = FastAPI()

@app.get('/')
def home():
    return {"message": "api"}

@app.get('/login', response_class=RedirectResponse)
def home():
    login_url = discord_auth.login()
    return login_url

@app.get('/callback')
def callback(code: str):
    tokens = discord_auth.get_tokens(code)
    return tokens


class RefreshToken(BaseModel):
    refresh_token: str

@app.post('/refresh_token')
def refresh_token(refresh_token: RefreshToken):
    token = discord_auth.refresh_token(refresh_token.refresh_token)
    return token

class AccessToken(BaseModel):
    access_token: str

@app.post('/user')
def user(access_token: AccessToken):
    user_data = discord_auth.get_user_data_from_token(access_token.access_token)
    return user_data

```
