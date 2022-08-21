
# URL Shortener API

Directory **api** contains the project, **URL Shortener API**

  To run server after clonning repo, from *api* run : **uvicorn app.main:app --reload**
  
  **Authentication** is handled with *oauth2* 
  
  There are two types of users: *normal* and *premium*, *premium* user is boolean, if **True** user can create custom shortened url if not **True**
  system does not allows to create custom url
  
  **Helper Functions** are in *app/util.py* which also includes the **Click Counter** function, which is defined as *update_clicks*
  
 
# Endpoints

You can navigate to : *localhost:8000/docs* to see the available endpoints and payloads via *swagger* UI
