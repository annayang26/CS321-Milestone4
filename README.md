![commit](https://img.shields.io/github/last-commit/annayang26/CS321-Milestone4)
![contributer](https://img.shields.io/github/contributors/annayang26/CS321-Milestone4)
![open issues](https://img.shields.io/github/issues-raw/annayang26/CS321-Milestone4)
![stars](https://img.shields.io/github/stars/annayang26/CS321-Milestone4?style=social)

<p align="center">
    <img src="https://img.shields.io/badge/CS321-Group1Milestone4-blue">
</p>

# 📈 Colby College Athletic Management System (Flask Web App)

## Abstract
The goal of this milestone was to develop a dynamic version of the Athletic Management System we have been working on. We used Flask to make a website that implemented the pages we had made for milestone 3 in html and css. Some of the dynamic features we added were a functional search bar, downloadable pdfs, permission controls, user login and user profiles. In addition, we implemented Flask modules to utilize functional features, such as authentication, and a database. We then put our files on the Github repository that our scrum master (Anna) had created and gave a short presentation to the class on what we had created.

## Sprint Backlog
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

## Results
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

### Original Sprint
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

### Burndown Chart
![Burndown Chart image](/README-img/burndown.png)

The burndown chart shows our work throughout the 2 week period we had to do this milestone.
As you can see progress started off very slow but we all felt there were significant jumps when we met together.
Unfortunately due to very hectic conflicting schedules much of the progress we made was in the two nights before the due date so I think going forward we are going to try to meet earlier in the week.

## Contribution List
| Adaobi | Anna (Scrum Master) | Hayden | Linn | Sam |
| --- | --- | --- | --- | --- |
| Login Page | Permissions (Flask + HTML) (Edit, Add user) | Admin Dashboard | Interactive Graph | Interactive Team Search |
| Athlete Dashboard | Login Page | Helped group members with HTML and CSS questions | Coach Dashboard | Super Admin Reports - download PDFs |
| | Signup Page | README.md | | |

## Extensions
Write your report in Markdown as a readme file in your repository, including table images and appropriate tags and content.

## Helpful links (references)
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
