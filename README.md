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

⋅The Most Popular Three Articles of all time:
1. "Candidate is jerk, alleges rival" - 677294 views
2. "Bears love berries, alleges bear" - 507602 views
3. "Bad things gone, say good people" - 340196 views

Top Three Popular Authors:
1. "Ursula La Multa" - 2030376 views
2. "Rudolf von Treppenwitz" - 1693828 views
3. "Anonymous Contributor" - 680392 views

Days With More Than 1% Errors:
July 17, 2016 - 226.3% Errors!```
