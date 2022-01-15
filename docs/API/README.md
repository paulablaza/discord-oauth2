---
icon: code-review
---

# API

List of the classes and functions inside the package.

<hr />

## DiscordAuth()

```py
DiscordAuth(client_id, client_secret, callback_url)
```

#### Usage:

```py
# It is recommended to use a variable so we can reuse it.
discord_auth = DiscordAuth(client_id, client_secret, callback_url)
```

<hr />

### login()

```py
DiscordAuth(client_id, client_secret, callback_url).login()
```

Returns a discord auth link, please manually redirect the user. It redirects to the callback url with the query parameter "code" (example: https://callbackurl/?code=isfd78f2UIRFerf) to get the code to use a function called getTokens().

#### Usage:

```py
discord_auth.login()
```

<hr />

### getTokens()

```py
DiscordAuth(client_id, client_secret, callback_url).getTokens(code)
```

Gets the access token and refresh token from the given code (code can only be used once please refer to discord's api documentation).

#### Usage:

```py
discord_auth.getTokens(code)
```

<hr />

### refresh_token()

```py
DiscordAuth(client_id, client_secret, callback_url).refresh_token(refresh_token)
```

Refreshes access token and access tokens and will return a new set of tokens

#### Usage:

```py
rtoken = g87a0l14098sdf
discord_auth.refresh_token(rtoken)
```

<hr />

### get_user_data_from_token()

```py
DiscordAuth(client_id, client_secret, callback_url).refresh_token(refresh_token)
```

Gets the user data from an access_token. I use it for authorization.

```py
access_token = 982be0dsy90a1kh9
discord_auth.get_user_data_from_token(access_token)
```
