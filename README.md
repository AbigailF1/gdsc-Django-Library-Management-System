<h1>LIBRARY MANAGEMENT SYSTEM using DJANGO</h1>

<<<<<<< HEAD
<h2>models</h2>
<ul>
<li>users</li>
<li>book</li>
<li>borrowedbook</li>
<li>review</li>
<li>genre</li>
</ul>

```bash

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
after creating username and password
```bash
python manage.py runserver
```
go to the url most probably http://localhost:8000/admin
=======
<p>
  if the code doesn't work download the zip file
</p>


<p>
while I was testing my code I moved review and rating functionality to the libraryCatalogues app and left it there by mistake. <br>

if you aleady pulled it just move <br>
<ol>
<li>submit_review.html <code> [ libraryCatalogue/templates -> borrowing/templates ] </code>  <br> </li>  
<li>ReviewForm class <code> [ libraryCatalogue/forms.py -> borrowing/templates ] </code> <br></li>
<li>submit_review function <code> [ librarycatalogue/views.py -> borrowing/views.py ] </code> <br></li>
<li>submit_review path <code> [ librarycatalogue/urls.py  -> borrowing/urls.py   ] </code> <br></li>
</ol>

import them where needed and delete unused imports while you make the changes <br>

or you could just pull it again if doesn't affect your work since I fixed it. <br>
</p>
>>>>>>> 88ec268f8778a4fbce73dbbd3887c30d1de319e0
