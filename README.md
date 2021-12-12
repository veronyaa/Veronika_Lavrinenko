Used stack:
  - selenium package
  - Chrome webdriver https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/
  - OOP patterns

Firstly you need to open this file in python development environment and compile the code
Then Automatizational software will do this task:
1. Add new job: Student or Intern (Go to Admin -> Job - Job Titles -> Click on the Add button)
           Add job title
           Add Job Description: free text up to 20 chars
           Add note
           Save changes
2. Check newly added title is visible on the grid
4. Modify your Job Title (select your field -> click on the Edit button):
            Change Job Description: free text up to 20 chars
            Save changes
5. Check that your changes are visible on the Job Title page
6. Select your field, click the Remove button and make sure your field is removed.

Class Automatization implements functions for 1,2,4,5,6 task points

Function check() tests  added job title ( 2 task point) , changes with job title and job description ( 5 task point )

Function check_deletion() tests deletion of job title
