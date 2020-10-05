# Part 1 - Creating EC2 Instance and Installing MariaDB Server

# Launch EC2 Instance.

# AMI: Amazon Linux 2
# Instance Type: t2.micro
# Security Group
#   - SSH           -----> 22    -----> Anywhere
#   - MYSQL/Aurora  -----> 3306  -----> Anywhere

# Connect to EC2 instance with SSH.

# Update yum package management and install MariaDB server.
sudo yum update -y
sudo yum install mariadb-server -y

# Start MariaDB service.
sudo systemctl start mariadb

# Check status of MariaDB service.
sudo systemctl status mariadb

# Enable MariaDB service, so that MariaDB service will be activated on restarts.
sudo systemctl enable mariadb

###################################################################################

# Part 2 - Connecting and Configuring MariaDB Database

# Connect to the MariaDB Server and open MySQL CLI with root user, no password set as default.
mysql -u root


# Show default databases in the MariaDB Server.
SHOW DATABASES;

# Choose a database (mysql db) to work with. ⚠️ Caution: We have chosen mysql db as demo purposes, normally database mysql is used by server itself, it shouldn't be changed or altered by the user.
USE mysql;

# Show tables within the mysql db.
SHOW TABLES;

# Show users defined in the db server currently.
SELECT Host, User, Password FROM user;

#Close the mysql terminal.
EXIT;

# Setup secure installation of MariaDB.
# No root password for root so 'Enter' for first question,
# Then set root password: 'root1234' and yes 'y' to all remaining ones.
sudo mysql_secure_installation

# Show that you can not log into mysql terminal without password anymore.
mysql -u root

#Connect to the MariaDB Server and open MySQL CLI with root user and password (pw:root1234).
mysql -u root -p

# Show that test db is gone.
SHOW DATABASES;

# List the users defined in the server and show that it has now password and its encrypted.
USE mysql;
SELECT Host, User, Password FROM user;


# Create new database named 'clarusdb'.
CREATE DATABASE clarusdb;

# Show newly created database.
SHOW DATABASES;

# Create a user named 'clarususer'. Password: clarus1234
CREATE USER calarususer IDENTIFIED BY 'clarus1234';

# Grant permissions to the user clarususer for database clarusdb.
GRANT ALL ON clarusdb.* TO clarususer IDENTIFIED BY 'clarus1234' WITH GRANT OPTION;

# Update privileges.
FLUSH PRIVILEGES;

# Close the mysql terminal.
EXIT;

###################################################################

# Part 3 - Manipulating MariaDB Database

# Login back as clarususer using the password defined.
mysql -u clarususer -p

# Show databases for clarususer.
SHOW DATABASES;

# Select the database clarusdb.
USE clarusdb;

# Create a table named offices.
CREATE TABLE `offices` (
  `office_id` int(11) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  PRIMARY KEY (`office_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

# Insert some data into the table named offices.
INSERT INTO `offices` VALUES (1,'03 Reinke Trail','Cincinnati','OH');
INSERT INTO `offices` VALUES (2,'5507 Becker Terrace','New York City','NY');
INSERT INTO `offices` VALUES (3,'54 Northland Court','Richmond','VA');
INSERT INTO `offices` VALUES (4,'08 South Crossing','Cincinnati','OH');
INSERT INTO `offices` VALUES (5,'553 Maple Drive','Minneapolis','MN');
INSERT INTO `offices` VALUES (6,'23 North Plaza','Aurora','CO');
INSERT INTO `offices` VALUES (7,'9658 Wayridge Court','Boise','ID');
INSERT INTO `offices` VALUES (8,'9 Grayhawk Trail','New York City','NY');
INSERT INTO `offices` VALUES (9,'16862 Westend Hill','Knoxville','TN');
INSERT INTO `offices` VALUES (10,'4 Bluestem Parkway','Savannah','GA');

# Create a table named employees.
CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `job_title` varchar(50) NOT NULL,
  `salary` int(11) NOT NULL,
  `reports_to` int(11) DEFAULT NULL,
  `office_id` int(11) NOT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `fk_employees_offices_idx` (`office_id`),
  CONSTRAINT `fk_employees_offices` FOREIGN KEY (`office_id`) REFERENCES `offices` (`office_id`) ON UPDATE CASCADE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

# Insert some data into the table named employees.
INSERT INTO `employees` VALUES (37270,'Yovonnda','Magrannell','Executive Secretary',63996,NULL,10);
INSERT INTO `employees` VALUES (33391,'Darcy','Nortunen','Account Executive',62871,37270,1);
INSERT INTO `employees` VALUES (37851,'Sayer','Matterson','Statistician III',98926,37270,1);
INSERT INTO `employees` VALUES (40448,'Mindy','Crissil','Staff Scientist',94860,37270,1);
INSERT INTO `employees` VALUES (56274,'Keriann','Alloisi','VP Marketing',110150,37270,1);
INSERT INTO `employees` VALUES (63196,'Alaster','Scutchin','Assistant Professor',32179,37270,2);
INSERT INTO `employees` VALUES (67009,'North','de Clerc','VP Product Management',114257,37270,2);
INSERT INTO `employees` VALUES (67370,'Elladine','Rising','Social Worker',96767,37270,2);
INSERT INTO `employees` VALUES (68249,'Nisse','Voysey','Financial Advisor',52832,37270,2);
INSERT INTO `employees` VALUES (72540,'Guthrey','Iacopetti','Office Assistant I',117690,37270,3);
INSERT INTO `employees` VALUES (72913,'Kass','Hefferan','Computer Systems Analyst IV',96401,37270,3);
INSERT INTO `employees` VALUES (75900,'Virge','Goodrum','Information Systems Manager',54578,37270,3);
INSERT INTO `employees` VALUES (76196,'Mirilla','Janowski','Cost Accountant',119241,37270,3);
INSERT INTO `employees` VALUES (80529,'Lynde','Aronson','Junior Executive',77182,37270,4);
INSERT INTO `employees` VALUES (80679,'Mildrid','Sokale','Geologist II',67987,37270,4);
INSERT INTO `employees` VALUES (84791,'Hazel','Tarbert','General Manager',93760,37270,4);
INSERT INTO `employees` VALUES (95213,'Cole','Kesterton','Pharmacist',86119,37270,4);
INSERT INTO `employees` VALUES (96513,'Theresa','Binney','Food Chemist',47354,37270,5);
INSERT INTO `employees` VALUES (98374,'Estrellita','Daleman','Staff Accountant IV',70187,37270,5);
INSERT INTO `employees` VALUES (115357,'Ivy','Fearey','Structural Engineer',92710,37270,5);

# Show newly created tables.
SHOW TABLES;

# List all records within employees table.
SELECT * FROM employees;

# List all records within offices table.
SELECT * FROM offices;

# Filter the first_name, last_name, salary, city, state information of employees having salary more than $100000.
SELECT first_name, last_name, salary, city, state FROM employees INNER JOIN offices ON employees.office_id=offices.office_id WHERE employees.salary > 100000;

# Close the mysql terminal.
EXIT;

##########################################################################

# Part 4 - Creating a Client Instance and Connecting to MariaDB Server Instance Remotely

# Launch EC2 Instance (Ubuntu 20.04) and name it as MariaDB-Client on Ubuntu.

# AMI: Ubuntu 20.04
# Instance Type: t2.micro
# Security Group
#   - SSH           -----> 22    -----> Anywhere
#   - MYSQL/Aurora  -----> 3306  -----> Anywhere

# Connect to EC2 instance with SSH.

# Update instance.
sudo apt update && sudo apt upgrade -y

# Install the mariadb-client.
sudo apt-get install mariadb-client -y

# Connect the clarusdb on MariaDB Server on the other EC2 instance (pw:clarus1234).
mysql -h ec2-54-242-32-254.compute-1.amazonaws.com -u clarususer -p

# Show that clarususer can do same db operations on MariaDB Server instance.
SHOW DATABASES;
USE clarusdb;
SHOW TABLES;
SELECT first_name, last_name, salary, city, state FROM employees INNER JOIN offices ON employees.office_id=offices.office_id WHERE employees.salary > 100000;

# Close the mysql terminal.
EXIT

# DO NOT FORGET TO TERMINATE THE INSTANCES YOU CREATED!!!!!!!!!!

