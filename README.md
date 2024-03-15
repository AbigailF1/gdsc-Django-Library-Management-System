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
submit_review.html [ libraryCatalogue/templates -> borrowing/templates ] <br>
ReviewForm class [ libraryCatalogue/forms.py -> borrowing/templates ] <br>
submit_review function [ librarycatalogue/views.py -> borrowing/views.py ] <br>
submit_review path [ librarycatalogue/urls.py  -> borrowing/urls.py   ] <br>

import them where needed and delete unused imports while you make the changes <br>

or you could just pull it again if doesn't affect your work since I fixed it. <br>
</p>
