# Bencompare sollicitatie opdracht
Willem Datema

1. Install docker and docker-compose

2. Clone this repository

3. Get Twitter API credentials and fill them in on the dots in create_credentials.py

4. Run 
```
python3 create_credentials.py
```
You should now have a twitter_credentials.json file in the main directory.

4. Run 
```
docker-compose up -d
```

5. Run
```
docker exec -it bencomopdracht_web_1 python3 manage.py migrate

```
6. Create a superuser by running 
```
docker exec -it bencomopdracht_web_1 python3 manage.py createsuperuser
``` 
Afterwards, complete the necessary steps to create the superuser.

7. Navigate to 0.0.0.0:8000

The homepage contains a button. If the credentials are filled in correctly in create_credentials.py, and saved correctly in twitter_credentials.json, this button will retrieve the latest three tweets from Gaslicht_com. 

Afterwards, the user is redirected to a list view with the latest three tweets and a link to the admin page. The list view contains links of the tweets. Clicking on these links redirects the user to the more detailed view of the tweet, with the most frequent letter in italics and the word(s) with the most frequent letters in bold. The full urls, if available, are listed underneath the tweet. 

On the admin page, a user navigate to the Tweets model, he can click on a tweet and tick the 'Important' box to highlight the tweet in both the list view and the detail view.
