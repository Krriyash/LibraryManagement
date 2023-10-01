
						/// Designed and Programmed by Ria and Team ///

*Open folder*

**READMe . md** *is not entirely complete. Its complete functionality will be updated once the documentation is done.*

**LICENSE File** *is a file that patents your sourcecode allowing only you and the users of your team to have full ownership and rights of the source code.* 
	- *License used:* **Eclipse Public License - v 2.0**
	*EPLv.20* - **Reproduction or Distribution of the program/source code requires permission from the owner of the license.**

*Open folder LM*

**LM.code-workspace:**
*Used to open the entire folder as a workspace in visual studio. Basically a setup feature to be able to open your code faster.*
	- How to use: *Left click and open with Visual Studio*

Open folder Sourcecode:

**I.** **Main . py**

	Main py is your main python script that acts as a parent script
		- Acts as the parent window for your program.

**II. Add_books . py**

*Launches a window for the user to add books into the database.*

*Parameters/Fields to enter: Title, Author, Genre, Rating, ISBN*
 
	(This script is connected to library.csv)

**III. List_books . py**

*Launches a window displaying all books to the user.
	Is in a list format on the left hand panel displaying titles
	Once user clicks on a book, on the right hand panel it displays data related to the book.
	(This script is connected to library.csv)*

**IV. My_books . py**
	
 *When user launches Main . py, on the bottom of the window a field is present to log in by entering a username.
	Once a username is Input, the program will create a new csv database document file in the "Users" folder with the file name corresponding to the user's username.*
 
*If there already exists a csv file with the same username, the program will not create another one.*

*In this window the user can borrow or return or view the books borrowed by them currently.
In order to borrow or return a book, they must enter the ISBN of the book. (It's window is launched when the borrow or return button is engaged.)*

	(This script is connected to library.csv)
 
	(This script is connected to the corresponding csv file of the username in the "Users" folder.)

**V. Remove_book . py**
	
 *Launches a window allowing the user to remove a book from the main database by entering the title of the book along with its ISBN
	(This script is connected to library.csv)*

**VI. Search_book.py**
	
 *Launches a window allowing the user to search for any desired book based on the parameters of: Title, Author, Genre or Rating.
	Any one of the fields can be entered, either the Title, or Author, or Genre, or rating and the respective results will be displayed.*
 
*If a user engages the search button without entering any parameter, the program will execute with it displaying all possible books.
The clear button is used to clear results.*

	(This script is connected to library.csv)

**LIBRARY.CSV**

	This is a csv file that acts as a database for the LibraryManagementSystemProgram (LMSP).
	Here data is organised in the format: Title - Author - Genre - Rating - ISBN
	The header of the file indicates the columns. 
	The header must not be changed or else it will break the program.
	The sourcecode is written in such a way that the program skips -
	- the first row of code in Library.csv to avoid reading the header.

**How do I run the program?**
				
	Navigate to sourcecode\main.py
	Left click on main.py and open with visual studio. Or any other editor. 
	
	However it is preffered you use VScode.

**I entered my name in the log in bar and clicked on submit but it did nothing?**
				
	Click on submit once more. And then check the "Users" folder.
	If a new csv file corresponding to your name is created, 
	then the database is active and a new window will open.

**What is pycache?**

	
	They are bytecode complied files that are saved in the directory,
	to make the program run faster the next time you open it. 
	
	Do not delete them, it is an unnecessary action.

**My books say they dont have a cover page, but I want to add a cover page, what do I do?**

	Simply download your image in png format, 
	and save it in the "Covers" folder with the corresponding ISBN number as the image file's title.
	
	For example: Book XYZ with ISBN: 1234
	Download image and name it 1234.png and save it in the "Covers" folder.
	
	Launch the program and navigate to list books and click your book. You should now see the cover page displayed.


*(Cover pages were not displayed in the original sourcecode since it took too much time and reduced efficiency of program during testing)*

*This READMe document can/will be further updated as needed.*

						/// Designed and Programmed by Ria and Team ///
