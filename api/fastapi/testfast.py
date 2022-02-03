""" Test FastAPI using OAuth2 """
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()): # pylint:disable=redefined-outer-name
    """ post token """
    return {'access_token' : form_data.username + 'token'}

@app.get('/')
async def index(token: str = Depends(oauth2_scheme)): # pylint:disable=redefined-outer-name
    """ display token """
    return {'the_token' : token}
