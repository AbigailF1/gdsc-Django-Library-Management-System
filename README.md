important!
<p>
go check the Review class in libraryCatalog/models.py. <br>
student field is asssigned to a charfield <br>
you have to change that to a user instance before makemigration->migrate <br>
also remove student from libraryCatalog/forms.py meta field<br>
</p>
