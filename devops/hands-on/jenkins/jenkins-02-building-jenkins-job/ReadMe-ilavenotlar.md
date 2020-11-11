

İlave not:

Connect to the Jenkins Server

Install Java
````
sudo yum update -y
sudo amazon-linux-extras install java-openjdk11 -y
sudo yum install java-devel
```` 

Install Maven
````
cd /opt
wget https://ftp.itu.edu.tr/Mirror/Apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
tar -zxvf $(ls | grep apache-maven-*-bin.tar.gz)
rm -rf $(ls | grep apache-maven-*-bin.tar.gz)
sudo ln -s $(ls | grep apache-maven*) maven
sudo su
echo 'export M2_HOME=/opt/maven' >> /etc/profile.d/maven.sh
echo 'export PATH=${M2_HOME}/bin:${PATH}' >> /etc/profile.d/maven.sh
exit
source /etc/profile.d/maven.sh
````

Install Git
````
sudo yum install git -y