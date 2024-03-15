important!
<p>
go check the Review class in libraryCatalog/models.py. <br>
student field is asssigned to a charfield <br>
you have to change that to a user instance before makemigration->migrate <br>
also remove student from libraryCatalog/forms.py meta field<br>
</p>

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
