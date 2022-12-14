![commit](https://img.shields.io/github/last-commit/annayang26/CS321-Milestone4)
![contributer](https://img.shields.io/github/contributors/annayang26/CS321-Milestone4)
![open issues](https://img.shields.io/github/issues-raw/annayang26/CS321-Milestone4)
![stars](https://img.shields.io/github/stars/annayang26/CS321-Milestone4?style=social)

<p align="center">
    <img src="https://img.shields.io/badge/CS321-Group1Milestone4-blue">
    <img src="https://img.shields.io/badge/CS321-Group1Milestone5-blue">
    <img src="https://img.shields.io/badge/CS321-Group1Milestone6-blue">
    <img src="https://img.shields.io/badge/CS321-Group1Milestone8-blue">
</p>

# 📈 Colby College Athletic Management System (Flask Web App)

## Abstract (Milestone 8)
The objective of this milestone is to finish our project by implementing remaining items in our product backlog and refactoring our code to enhance readability and maintainability. Specifically, we redeployed the app on Heroku, raised the test coverage from 74% to 90%, calculated the code metrics using Radon and reduced the complexity of the code.

## Sprint Backlog (Milestone 8)
- Super Admin User Stories - ESTIMATE: High Priority Drafts (1 week), Medium Priority (5 days), Low Priority (2 days) 
    - As a super admin, I want to control the permissions (for both coaches and athletes) so that I can monitor who has access to the data and protect           student athletes’ personal data (High Priority) - COMPLETED
    - As a super admin, I want to see all student-athletes data to track trends to inform the relevant people about injuries, wellbeing, etc. (High Priority) - COMPLETED
    - As a super admin, I want to be able to generate and send reports to coaches so that they can be well informed about the trends in their team. (Medium Priority) - COMPLETE
    - As a super admin, I want to view all athletes’ stats and coaches’ profiles so I can have an idea of who they are. (Medium Priority) - COMPLETE
    - As a super admin, I want machine learning functionality so that I can make predictions based on trends in the data. (Low Priority)
    - As a super admin, I want to see the nutrition logs of athletes so that I can ensure that they are fueling their bodies with the right nutrition. (Low Priority) - COMPLETE
    - As a super admin, I want to be able to run analysis on available data so that I can provide coaches and athletes with useful information. (Low Priority)
    - As a super admin, I want to be able to look at my schedule and upcoming events so that I know where I need to be at all times. (Low Priority) - COMPLETE
- Coach User Stories - ESTIMATE: High Priority Drafts (1 week), Medium Priority (5 days)
    - As a coach, I want to be able to view data and visualizations for all my athletes, honing in on individuals, including sleep data, readiness (based on Hawkin Dynamics, firstbeat - heart rate), and injury status so I can better manage my players, and adjust training plan, and ensure athletes get the relevant care they need. (High Priority) - COMPLETE 
    - As a coach, I want these stats to be presented in a way that is easy to understand so that I can quickly access the information that I need. (Medium Priority) - COMPLETE
- Athlete - ESTIMATE: High Priority (1 week), Medium Priority (5 days)
    - As an athlete, I want to be able to see my own data so that I have information about my performance. (High Priority) - COMPLETE
    - As an athlete, I want to have access to my own injury status, mental health information, and notes from the support staff so that I understand what is going on with my body. (Medium Priority) - COMPLETE
    - As an athlete, I can see historical trends in my stats so that I can know how to optimize my performance. (Medium Priority) - COMPLETE

## Results (Milestone 8)
Deployed Colby Athletic Management System: https://colbyams1.herokuapp.com/ 

** please select login button and then enter the credentials **
- Super admin account: superadmin@colby.edu - password: 1111111
- Coach account: coach@colby.edu - password: 1111111
- Athlete account: athlete@colby.edu - password: 1111111

GitHub repository: https://github.com/annayang26/CS321-Milestone4 

### Metrics
Before:

!["Before" Metrics](/README-img/beforemetrics1.png)
!["Before" Metrics](/README-img/beforemetrics2.png)

!["Before" Metrics](/README-img/beforemetrics3.png)

After:

!["After" Metrics](/README-img/aftermetrics1.png)
!["After" Metrics](/README-img/aftermetrics2.png)

!["After" Metrics](/README-img/aftermetrics3.png)


The Radon test before modification was fairly good, given that we have an average of 2.36 complexity. After cleaning up the code, we achieved a Radon score of 2.18, which is lower than the initial one. We were able to decrease code complexity of the function edit() from B to A by changing the elif statement to else because we only need to differentiate between admin and coach/athlete. Other elif statements in login and add_user functions were also changed to else if appropriate. However, since information security is important, and we use access level to ensure that, it is necessary to set strict levels using if and elif statements. Therefore, we can’t reduce the code complexity anymore in those two functions. On the other hand, since sign-up needs to make sure that the user doesn’t exist in the database, that the user creates a strong password, or that the user is filling a valid name, if and elif statements are also needed. In addition, we hard coded the super admin email in the login so that when running the app, we have an account to create more users of different levels and for testing. 

### Test Coverage
Before:

!["Before" Test Coverage](/README-img/beforetestcoverage.png)

After:

!["After" Test Coverage](/README-img/aftertestcoverage.png)

The test coverage was raised from 74% to 90%. We left out a lot of code in views.py because they were API codes.

### Burndown Chart

![Burndown Chart](/README-img/burndownchart8.png)

## Contribution List (Milestone 8)
| Linn | Anna | Hayden | Adaobi | Sam | Dylan| Bryan |
| ---                   | ---  | ---    | ---  | --- | ---  | ---   |
| Raised test coverage from 74% to 90% | Redeployed the app on Heroku | Burndown Chart |  |  |  |  |
| Wrote report | Calculated code metrics and reduce code complexity  | Put report on README.md |  |  |  |  |
| | Use Heroku Config Var to store credentials |  |  |  |

## Extensions (Milestone 8)
Wrote our report in Markdown as a readme file in our repository, including table images and appropriate tags and content.

## References/Acknowledgements (Milestone 8)
https://www.offerzen.com/blog/how-i-used-pytest-to-write-qa-tests-that-securely-bypass-2fa
https://stackoverflow.com/questions/18827985/mocking-oauth-providers-while-testing


## Abstract (Milestone 6)
The goal of this milestone was to implement and practice with CI/CD testing. Our team developed a CI/CD pipeline to lint, test, and deploy our dynamic Athletic Management System to the cloud. Another goal was to get practice with Pytest and we added tests with the goal of improving code quality and discovering problems earlier. In the end we were able to achieve 80% test coverage.

## Sprint Backlog (Milestone 6)
- Super Admin User Stories - ESTIMATE: High Priority Drafts (1 week), Medium Priority (5 days), Low Priority (2 days)
    - As a super admin, I want to control the permissions (for both coaches and athletes) so that I can monitor who has access to the data and protect student athletes’ personal data (High Priority) - COMPLETED
    - As a super admin, I want to see all student-athletes data to track trends to inform the relevant people about injuries, wellbeing, etc. (High Priority) - COMPLETED
    - As a super admin, I want to be able to generate and send reports to coaches so that they can be well informed about the trends in their team. (Medium Priority) - COMPLETE
    - As a super admin, I want to view all athletes’ stats and coaches’ profiles so I can have an idea of who they are. (Medium Priority) - COMPLETE
    - As a super admin, I want machine learning functionality so that I can make predictions based on trends in the data. (Low Priority)
    - As a super admin, I want to see the nutrition logs of athletes so that I can ensure that they are fueling their bodies with the right nutrition. (Low Priority) - COMPLETE
    - As a super admin, I want to be able to run analysis on available data so that I can provide coaches and athletes with useful information. (Low Priority)
- Coach User Stories - ESTIMATE: High Priority Drafts (1 week), Medium Priority (5 days)
    - As a coach, I want to be able to view data and visualizations for all my athletes, honing in on individuals, including sleep data, readiness (based on Hawkin Dynamics, firstbeat - heart rate), and injury status so I can better manage my players, and adjust training plan, and ensure athletes get the relevant care they need. (High Priority) - COMPLETE 
    - As a coach, I want these stats to be presented in a way that is easy to understand so that I can quickly access the information that I need. (Medium Priority) - COMPLETE
- Athlete - ESTIMATE: High Priority (1 week), Medium Priority (5 days)
    - As an athlete, I want to be able to see my own data so that I have information about my performance. (High Priority) - COMPLETE
    - As an athlete, I want to have access to my own injury status, mental health information, and notes from the support staff so that I understand what is going on with my body. (Medium Priority) - COMPLETE
    - As an athlete, I can see historical trends in my stats so that I can know how to optimize my performance. (Medium Priority) - COMPLETE

## Results (Milestone 6)

### Github Workflow
![Github workflow on repository](/README-img/githubworkflow.png)

### Pytest in Github workflow
![Pytest in Github workflow](/README-img/pytestingithubworkfloww.png)

### Pytest Coverage
![Pytest Coverage](/README-img/pytestcoverage.png)

### Burndown Chart
![Burndown Chart](/README-img/newburndownchart.png)

## Contribution List (Milestone 6)
| Linn (Scrum Master) | Anna | Hayden | Adaobi | Sam | Dylan| Bryan |
| ---                   | ---  | ---    | ---  | --- | ---  | ---   |
| Worked on testing for views.py | Worked on testing for views.py | Worked on testing for __init__.py | Worked on testing for models.py | Worked on testing for views.py | Worked on testing for views.py | Worked on testing for auth.py |
| write in issues e.g. testing view.py, almost each function should be an issue| Test admin related functions, e.g. add_user, edit | Getting Graphs onto HTML pages | Connected component breakdown in coach’s team breakdown | Cleanup–Identified html files that were not in use and could be deleted | Getting Graphs onto HTML pages | Getting Graphs onto HTML pages |
| | | Fixed off-center link in Admin Dashboard | Allowed the CSV button to download sample CSV | |


## Reference/Acknowledgements (Milestone 6)
We appreciate Professor Al Madi for helping us answer questions about testing and linting in our project.

## Abstract (Milestone 5)
The goal of this milestone was to deploy the dynamic version of the Athletic Management System to the cloud. We deployed our website using Heroku and postgresql database. We also fixed some bugs found in our Flask website from the last milestone. These bugs include issues with the list not repopulating after a search was deleted in the search bar, and CSS issues that caused the list of athletes to appear as a green square. We added new functionality such as delete user and edit user for admin, populating athlete lists from the database instead of hard coding, and added a view and link to Peak Instagram posts on the nutrition page. In addition, for this milestone, we completed the component breakdowns(sleep, calories, and nutrition). We also updated our CSS for the admin dashboard and team breakdown to make our website cleaner. We then gave a short presentation to the class on our deployed Athletic Management System.

## Sprint Backlog (Milestone 5)
- Super Admin User Stories - ESTIMATE: High Priority Drafts (1 week), Medium Priority (5 days), Low Priority (2 days)
    - As a super admin, I want to control the permissions (for both coaches and athletes) so that I can monitor who has access to the data and protect student athletes’ personal data (High Priority) - COMPLETED
    - As a super admin, I want to see all student-athletes data to track trends to inform the relevant people about injuries, wellbeing, etc. (High Priority) - COMPLETED
    - As a super admin, I want to be able to generate and send reports to coaches so that they can be well informed about the trends in their team. (Medium Priority) - COMPLETE
    - As a super admin, I want to view all athletes’ stats and coaches’ profiles so I can have an idea of who they are. (Medium Priority) - COMPLETE
    - As a super admin, I want machine learning functionality so that I can make predictions based on trends in the data. (Low Priority)
    - As a super admin, I want to see the nutrition logs of athletes so that I can ensure that they are fueling their bodies with the right nutrition. (Low Priority) - COMPLETE
    - As a super admin, I want to be able to run analysis on available data so that I can provide coaches and athletes with useful information. (Low Priority)
- Coach User Stories - ESTIMATE: High Priority Drafts (1 week), Medium Priority (5 days)
    - As a coach, I want to be able to view data and visualizations for all my athletes, honing in on individuals, including sleep data, readiness (based on Hawkin Dynamics, firstbeat - heart rate), and injury status so I can better manage my players, and adjust training plan, and ensure athletes get the relevant care they need. (High Priority) - COMPLETE 
    - As a coach, I want these stats to be presented in a way that is easy to understand so that I can quickly access the information that I need. (Medium Priority) - COMPLETE
- Athlete - ESTIMATE: High Priority (1 week), Medium Priority (5 days)
    - As an athlete, I want to be able to see my own data so that I have information about my performance. (High Priority) - COMPLETE
    - As an athlete, I want to have access to my own injury status, mental health information, and notes from the support staff so that I understand what is going on with my body. (Medium Priority) - COMPLETE
    - As an athlete, I can see historical trends in my stats so that I can know how to optimize my performance. (Medium Priority)

## Results (Milestone 5)

### Super Admin's View
![Super Admin add admin user page image](/README-img/adminaddpage.png)
![Super Admin add athlete/coach user page image](/README-img/adminaddpage2.png)
![Super Admin generate reports page image](/README-img/adminreports.png)

### Coach's View
![Coach's Dashboard image](/README-img/coachdash.png)
![Coach's Dashboard image](/README-img/coachathletebreakdown.png)

### Athlete's View
![Athlete's Dashboard image](/README-img/athletedashboard.png)
![Athlete's Sleep Data image](/README-img/athletesleepdashboard.png)
![Athlete's Recovery Data image](/README-img/athleterecoverydashboard.png)
![Athlete's Calorie Intake Data image](/README-img/athletecaloriedahsboard.png)

### Original Sprints 
![Sprint Report](/README-img/sprintvelocity.png)

### Burndown Chart
![Burndown Chart](/README-img/burndownchart.png)

## Contribution List (Milestone 5)
| Adaobi (Scrum Master) | Anna | Hayden | Linn | Sam | Dylan| Bryan |
| ---                   | ---  | ---    | ---  | --- | ---  | ---   |
| Created athlete breakdown pages | Add team/branch to the User Model | Fixed CSS link issues | Fix coach dashboard’s HTML & CSS | Linked report pages | Helped group members with graph questions | Created Upload Page |
| Added Instagram widget on athlete breakdown| Add “team/branch” to add user and edit users function with updated CSS and js to allow choosing between tabs | Helped fix search bar so it resets | Helped fix athlete dashboard’s HTML & CSS | Helped fix search bar so it resets || Created Button to upload csv |
|Helped update CSS and HTML, using base.html so it was consistent for coach and athlete| Fixed bugs from the last milestone, including edit page not able to stay with current_user authentication | |Merged & resolved conflicts (develop -> main) | Helped upload csv|

## Extensions (Milestone 5)
Calculated team velocity for our team (an Agile metric).


![Sprint Report](/README-img/sprintvelocity.png)

As you can see in the agile velocity report creating the database for users and graphs was our highest priority and most complicated sprint. A lot of progress was made on that but we didn't quite complete everything. We were able to pretty much complete all the work we had set out to do and we pretty accurately predicted how much we would be able to do.

Sprint 1- Create database for users and graphs - put into tables 
Sprint 2 - Style/CSS
Sprint 3 - Athlete breakdown pages
Sprint 4 - Edit permission: choose team for coaches and athletes 
Sprint 5 - Add user: bulk-add users with email
Sprint 6 - Add forget password button
Sprint 7 - Add delete user button for admin
Sprint 8 - Report page linked to reportpage.html and not Index.html

Wrote our report in Markdown as a readme file in our repository, including table images and appropriate tags and content.


## Reference/Acknowledgements (Milestone 5)
We appreciate Giuseppe Stelluto for helping us with deploying our website using Heroku. 

## Abstract (Milestone 4)
The goal of this milestone was to develop a dynamic version of the Athletic Management System we have been working on. We used Flask to make a website that implemented the pages we had made for milestone 3 in html and css. Some of the dynamic features we added were a functional search bar, downloadable pdfs, permission controls, user login and user profiles. In addition, we implemented Flask modules to utilize functional features, such as authentication, and a database. We then put our files on the Github repository that our scrum master (Anna) had created and gave a short presentation to the class on what we had created.

## Sprint Backlog (Milestone 4)
- Super Admin User Stories - ESTIMATE: High Priority Drafts (1 week), Medium Priority (5 days), Low Priority (2 days)
  - As a super admin, I want to control the permissions (for both coaches and athletes) so that I can monitor who has access to the data and protect student athletes’ personal data (High Priority) - COMPLETED
  - As a super admin, I want to see all student-athletes data to track trends to inform the relevant people about injuries, wellbeing, etc. (High Priority) - COMPLETED
  - As a super admin, I want to be able to generate and send reports to coaches so that they can be well informed about the trends in their team. (Medium Priority) - COMPLETE
  - As a super admin, I want to view all athletes’ stats and coaches’ profiles so I can have an idea of who they are. (Medium Priority)
  - As a super admin, I want machine learning functionality so that I can make predictions based on trends in the data. (Low Priority)
  - As a super admin, I want to see the nutrition logs of athletes so that I can ensure that they are fueling their bodies with the right nutrition. (Low Priority) - COMPLETE
  - As a super admin, I want to be able to run analysis on available data so that I can provide coaches and athletes with useful information. (Low Priority)
- Coach User Stories - ESTIMATE: High Priority Drafts (1 week), Medium Priority (5 days)
  - As a coach, I want to be able to view data and visualizations for all my athletes, honing in on individuals, including sleep data, readiness (based on Hawkin Dynamics, firstbeat - heart rate), and injury status so I can better manage my players, and adjust training plan, and ensure athletes get the relevant care they need. (High Priority) - COMPLETE 
  - As a coach, I want these stats to be presented in a way that is easy to understand so that I can quickly access the information that I need. (Medium Priority) - COMPLETE
- Athlete - ESTIMATE: High Priority (1 week), Medium Priority (5 days)
  - As an athlete, I want to be able to see my own data so that I have information about my performance. (High Priority) - COMPLETE
  - As an athlete, I want to have access to my own injury status, mental health information, and notes from the support staff so that I understand what is going on with my body. (Medium Priority) - COMPLETE
  - As an athlete, I can see historical trends in my stats so that I can know how to optimize my performance. (Medium Priority)

## Results (Milestone 4)
### Coach's Dashboard 
![Coach's Dashboard image](/README-img/coach1.png)
![Coach's Dashboard image](/README-img/coach2.png)
![Coach's Dashboard image](/README-img/coach3.png)

### Super Admin Dashboard
![Super Admin Dashboard image](/README-img/admin.png)
![Team Breakdown image](/README-img/teambreakdown.png)

### Super Admin Permissions
![Permissions image](/README-img/permissions.png)

### Edit User Information
![Edit User image](/README-img/edit1.png)
![Edit User image](/README-img/coach2.png)

### Athlete Dashboard
![Athlete Dashboard image](/README-img/athlete.png)

### Original Sprint (Milestone 4)
🔴Friday 21st - Have a solid attempt and meet to discuss specifics and uniformity

🔵Tuesday 25th - Have everything done but small minute details and vuew eachotehrs stuff give feedback

🟢Wednesday 26th – Everyone done with their part meet to merge everything together and put on Github


- Login page (Adaobi & Anna)
- Athlete Pages
    - Information View/Dashboard (Adaobi)
    - Main data breakdown - Sleep, Readiness (Adaobi)
- Coach Pages 
    - Dashboard (Linn)
    - Athlete data breakdown (Adaobi)
        - Main data breakdown (Adaobi)
- Admin Pages
    - Dashboard (Hayden)
    - Team data breakdown (Linn)
    - Athlete data breakdown (Adaobi)
        - Main data breakdown (Adaobi)
    - Permissions (Anna)
        - Edit User Information (Anna)
        - User permissions (Anna)
        - New user (Anna)
    - Reports (Sam)
    - Interactive Team Search (Sam)

In addition to constant communication through text, we met three times throughout the time allotted for milestone 4. We met on Friday the 21st and our goal for this meeting was to have a solid attempt of the parts we had previously agreed to each do and discuss specifics and how we wanted the pages to look so we could have uniformity across the website. We then met on Tuesday 25th and the goal for this meeting was to have the bulk of your page done not including little fixes and details. We also used this time to go over what everyone had done and give feedback. Our final meeting was on Wednesday the 26th and in this meeting it was expected that everyone had all their stuff done because we were going to merge all of our pages together and publish them onto the Github,

### Burndown Chart (Milestone 4)
![Burndown Chart image](/README-img/burndown.png)

The burndown chart shows our work throughout the 2 week period we had to do this milestone.
As you can see progress started off very slow but we all felt there were significant jumps when we met together.
Unfortunately due to very hectic conflicting schedules much of the progress we made was in the two nights before the due date so I think going forward we are going to try to meet earlier in the week.

## Contribution List (Milestone 4)
| Adaobi | Anna (Scrum Master) | Hayden | Linn | Sam |
| --- | --- | --- | --- | --- |
| Login Page | Permissions (Flask + HTML) (Edit, Add user) | Admin Dashboard | Interactive Graph | Interactive Team Search |
| Athlete Dashboard | Login Page | Helped group members with HTML and CSS questions | Coach Dashboard | Super Admin Reports - download PDFs |
| | Signup Page | README.md | | |

## Extensions (Milestone 4)
Write your report in Markdown as a readme file in your repository, including table images and appropriate tags and content.

## Helpful links (references) (Milestone 4)
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
