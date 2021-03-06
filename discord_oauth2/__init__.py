import requests

class DiscordAuth:
  def __init__(self, client_id, client_secret, callback_url):
    """ Usage: credentials(client_id, client_secret, callback_url) """
    self.client_id = client_id
    self.client_secret = client_secret
    self.callback_url = callback_url

  def login(self):
    """ 
    Returns a discord auth link, please manually redirect the user then it goes to the callback url with the query parameter "code" (example: https://callbackurl/?code=isfd78f2UIRFerf) to get the code to use a function called getTokens(). 
    
    The code can only be used on an active url (callback url) meaning you can only use the code once 
    """
    return f'https://discord.com/oauth2/authorize?client_id={self.client_id}&redirect_uri={self.callback_url}&scope=identify&response_type=code'

  def get_tokens(self, code):
    """ Gets the access token from the code given. The code can only be used on an active url (callback url) meaning you can only use the code once. """
    data = {
      'client_id': self.client_id,
      'client_secret': self.client_secret,
      'grant_type': 'authorization_code',
      'code': code,
      'redirect_uri': self.callback_url
    }

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    tokens = requests.post('https://discord.com/api/v8/oauth2/token', data=data, headers=headers)
    return tokens.json()


  def refresh_token(self, refresh_token):
    """ Refreshes access token and access tokens and will return a new set of tokens """
    data = {
      'client_id': self.client_id,
      'client_secret': self.client_secret,
      'grant_type': 'refresh_token',
      'refresh_token': refresh_token
    }

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
      
    tokens = requests.post('https://discord.com/api/v8/oauth2/token', data=data, headers=headers)
    return tokens.json()    


  def get_user_data_from_token(self, access_token):
    """ Gets the user data from an access_token """
    headers = {
      "Authorization": f'Bearer {access_token}'
    }

    user_data = requests.get('https://discordapp.com/api/users/@me', headers=headers)
    return user_data.json()
