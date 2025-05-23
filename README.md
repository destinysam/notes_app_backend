### Matrix Sols – Developer Task


### Setup Instructions

1. Clone the repository.
   ```
   git clone https://github.com/destinysam/notes_app_backend
   ```
2.  Setup Environment on local(only if venv is installed)
   ```
  python3 -m venv env
  ```
3. Install the requirements
   ```
   pip install -r requirements.txt
   ```
4. Finally Run the project
   ```
   python3 manage.py runserver
   ```

### Create a superuser to login or test things
  ```
  python3 manage.py createsuperuser
  ```


### API SUMMARY (Adjust localhost address according to your server)

1. API to get token OR refresh token
   #### Get Token
   ```
   POST http://127.0.0.1:8000/api/token/
   ```
   #### Refresh Token
   ```
   POST http://127.0.0.1:8000/api/token/refresh/
   ```

1. API to create note or list notes or search note
   #### LIST
   ```
   GET http://127.0.0.1:8000/notes/
   ```
   #### CREATE
   ```
   POST http://127.0.0.1:8000/notes/
   ```
   #### SEARCH
   ```
   GET http://127.0.0.1:8000/notes/search=sameer
   ```

2. API to get particular Note
   ```
   GET http://127.0.0.1:8000/notes/post_id/
   ```


Note: Postman collection has been shared over the email(same email on which i recieved the assignment).


#### Thanks for the assignment :)

