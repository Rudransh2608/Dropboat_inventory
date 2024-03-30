<div align="center">
  <img src="https://github.com/Rudransh2608/Dropboat_inventory/assets/160394256/5b6318f3-0a9e-4367-83d9-022af9490fbc" alt="InvenTree logo" width="400" height="auto" />
  <br><br>
  <h1></h1>
  <p>Inventory Management System</p>
  <br>
  
# 💻 Tech Stack:
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![GithubPages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300000f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
</div>
<br>
<br>

# 🌟 About the project:
<p>
Dropboat is a robust Inventory Control Management System designed for efficient stock control and personnel management. At its core lies a Python/Django database backend that facilitates an admin interface accessible via the web. It employs protocols like SMTP and HTTP for seamless interaction with external interfaces and applications. Additionally, its versatile plugin system accommodates custom applications and extensions with ease.
</p>
<br>

# 🛠️ Integration:
<h3>
We've incorporated external tools and packages to enhance user experience and streamline operations.</h3>
<ul>
<li>Third party tools</li>
<li>Charts.js</li>
<li>Tinymce</li>
<li>Django crispy forms and bootstrap</li>
</ul>
<br>

-- install <a href="https://django-crispy-forms.readthedocs.io/en/latest/">django crispy forms</a><br>
-- for integrating graphs and figures <a href="https://www.chartjs.org/">Charts.js</a><br>
-- python -m pip install Django
<br><br>

# 💎 Features:
<h3>Key highlights of our system comprise:</h3>
<ul>
  <li><h4>CRUD operations 💹</h4></li>
  <p>These form the fundamental functionalities of our website, encompassing product and order management. Administrators can monitor records, oversee management tasks, and conduct comparative analyses between different categories to comprehend and uphold the organization's profit/loss ratios effectively.
  The administrator could introduce new products, modify existing ones(feature yet to come), and assess their status for potential deletion as necessary.
</p>
  <br>
  <li><h4>User Authentication and Permissions 🔐</h4></li>
  <p>Secure login for users with different roles (admin, manager, employee) and permissions to access specific features or data.
Our website features strong and vigorous authorization and authentication measures for both administrators and staff members. The staff page is distinct, providing a form for submitting order requests to the administrator and a profile section where staff can update their employee profiles according to organizational requirements.<br> Conversely, administrators access a distinct section of the website, featuring the main dashboard encompassing all essential system functionalities. From here, administrators can manage order requests submitted by staff and analyze products based on various categorical and numerical metrics.</p>
  <br>
  <li><h4>Smtp integration and App passwords 🔑🔗</h4></li>
<p>Integrated smtp protocol and external third party tools for managing app passwords .
This functionality becomes prominent when a user forgets their password, as they can generate a new one simply by providing their registered email address and then logging in using the newly created password.<br>
-- External third-party tools provide solutions that offer features for securely managing app passwords. These tools typically provide functionalities such as password storage, encryption, access control, and auditing to ensure the security of sensitive credentials.</p>
    <br>
<div align="center"><h2># The flow of server requests and the architectural setup for resetting passwords through third-party applications.</h2></div><br>

![USERS (3)](https://github.com/Rudransh2608/Dropboat_inventory/assets/160394256/b4896c3a-93e0-45d7-bec2-4443c12cd1b7)

 
  <li><h4>Reporting and Analytics 📈📊</h4></li>
<p>Generation of reports(feature yet to come) and analytics to provide insights into inventory levels, movement, trends, and casting.
We've incorporated a variety of graphical representations, encompassing line graphs, bar graphs, and pie charts, to elevate our analytics and reporting capabilities.
Dynamically rendered graphs with real-time stock reporting and product management scanning represent a cutting-edge feature of our system. This capability allows for the creation and display of graphical representations of pertinent data, such as inventory levels and product management activities, that are continually updated to reflect the most current information available.<br> <br>
Real-time data visualization enhances decision-making by providing users with immediate insights into inventory performance and product management activities. Users can quickly identify trends, anomalies, or issues within the inventory system and take proactive measures to address them.
</p>
<br>
<li><h4>User Profile and django signals 👤</h4></li>
<p>We've implemented Django signals to automatically generate a user profile upon registration, allowing users to subsequently customize their profiles and add additional details as required by the organization. Django signals enable decoupled and modular communication between different components of a Django application, allowing for the execution of custom logic in response to predefined events. </p>
<br>
Upon user registration, a signal is triggered to automatically generate a user profile instance in the database. This eliminates the need for users to manually create profiles after registering, simplifying the onboarding process and reducing friction for new users.<br>
Once the user profile is generated, users have the flexibility to customize their profiles and add additional details as needed. Users can access their profile page within the application and update information such as residential address, bio, interests, Phone and any other fields provided by the organization.
</ul>
<br>

<h3> ✨ Here's a glimpse of the Administrator dashboard and the Staff page :</h3>
<h1></h1>
<br>

![Screenshot (89)](https://github.com/Rudransh2608/Dropboat_inventory/assets/160394256/441adbdd-5d3d-492b-8f4a-e724280a0a32)
<br>

![Screenshot (90)](https://github.com/Rudransh2608/Dropboat_inventory/assets/160394256/6f0957c4-a2cd-498c-9336-e316e3ce9bb1)
<br>
  
# ❓FAQ

#### Question 1: Upon logging in a new user, the page cannot be located. ?

Answer 1: This occurs because the page for the logged-out user is not refreshed. Once the previous user's page is refreshed, the new user will be automatically logged in !!!

#### Question 2: The email containing app passwords is not being received. 

Answer 2: This is due to the fact that the user has not provided their registered email address for the password reset.
<br> 
<br>

# ❤️ Support

#### For support, email prathamrudransh1012@gmail.com or git us at <a href="https://github.com/Rudransh2608/Rudransh2608">github/Rudransh2608</a><br>




