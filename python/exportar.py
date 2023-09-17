from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.lists.list import List
from requests_ntlm import HttpNtlmAuth
from shareplum import Site

from requests_ntlm import HttpNtlmAuth
from shareplum.site import Version
from requests.auth import HTTPBasicAuth 
import csv
import requests

# Configurar la información de autenticación
site_url = "https://netorgft3388582.sharepoint.com/sites/HoraxHora"
username = "fvillalba@jkkpack.com"
password = "Jkkpack.22"
sp_list = "HXH IMPRESION"
api_url = f"{site_url}/_api/web/lists/getbytitle('HXH IMPRESION')/items"
response = requests.get(api_url, auth=HTTPBasicAuth(username, password))



# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    items = data['d']['results']
    # Procesa los elementos como desees
    for item in items:
        print(item)
else:
    print(f"Error: {response.status_code}")