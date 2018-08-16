# Log-Analysis

For this project, a log analysis of a newspaper site database was conducted.  The sql datbase can be downloaded from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). 


# Analysis
The reporting tool needed to answer the following questions:

1.  What are the most popular three articles of all time?
2.  Who are the most popular article authors of all time?
3.  On which days did more than 1% of requests lead to errors?



# Dependencies
*  [Vagrant](https://www.vagrantup.com/)
*  [VirtualBox](https://www.virtualbox.org/)
*  [Udacity's Github Vagrant Setup](https://github.com/udacity/fullstack-nanodegree-vm)


# Running the Program
1.  Open terminal and navigate to project folders.
2.  cd into `vagrant` directory.
3.  Run `vagrant up` to build the Virtual Machine (VM) for the first time.
4.  Once VM is built, run `vagrant ssh` to connect.
5.  cd into project directory:  `cd /vagrant/ Log-Analysis-Project`
6.  Run `python logAnalysis.py`


# Expected Output:
```Gathering Analysis...


Top Three Articles:
1. "Candidate is jerk, alleges rival" with 338647 views
2. "Bears love berries, alleges bear" with 253801 views
3. "Bad things gone, say good people" with 170098 views

Top Three Authors:
1. Ursula La Multa with 507594 views
2. Rudolf von Treppenwitz with 423457 views
3. Anonymous Contributor with 170098 views

Days With More Than 1% Errors:
July 17, 2016 - 2.3% Errors!```
