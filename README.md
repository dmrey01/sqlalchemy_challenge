# sqlalchemy_challenge
Module 10 challege 
    Created a new repository called sqlalchemy-challenge
    created a new folder SurfsUp
    Added folder from Module 10
    Started with Jupyter Notebook 
     imported, numpy, padas, datetime,
     imported, sqlalchemy, automap,
     from sqlalchemy import create_engine,func.

     created the connection by engine = create_engine to the resource folder
     added the reflection to exisitng data base and added the reflecting tables
        Base=auto_base()
            Base.prepare(autoload_with=engine)
    Found the class keys
    Saved them in a reference table 
    created a session link form our Python to our database. 

    Explored Analysis of Precipitation
    Found the most recent date of 2017-08-23

    Designed a query to retrieve the last 12 months of precipiations data and plot the results. 
    calulated the date one year form th last date
    preform a query and retrieve the data and preciepitation scores. See output line 20 for graph. 

    Calculate the summary statistics for the precipitation data.  See output in line 21. 

    Exploratiory Station Analysis. 

    Found total number of stations in the dataset = 9

     Query and found the most active stations in the dataset. 
        this we used the func.count and group_by along with the order_by methods. Then put the results in descending order. 

    Using the station Id's queried the lowest, hiest and avg temperature.  see results in output line #24

    Query using most tools to of the most active station we ploted the temperature for the last 12 months. se line 81 for the output. and ploted it using a Histogram. 

    I did encounter one issue with this dataset.  The sqlite file became correpted.  after I completed this first part.  I had to re-install the file and re-run the complete data set.  

Part 2

started working on the FLASK 
had issues with the dataset had to redo my data twice.  the file was corrupt. Then I recieved a lint error which Cait our insturtor helped me solved. 

Hoepefully everything is working now as I had to reload the file again at the end. 
