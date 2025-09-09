Package Sorting System

----------------------------------------------------------------------------------------------------------------

Overview -
The Package Sorting System is a Python-based tool designed for internal office staff to manage incoming tenant
packages effectively. It assigns storage locations to packages, allows quick retrieval, and keeps the database 
up to date. This tool is intended for use by trusted front office personnel.

-----------------------------------------------------------------------------------------------------------------

Features - 
Add Packages: Enter owner names and package widths: The system automatically calculates storage positions.

Find Packages: Locate a package using the owner's name, showing row and column placement.

Remove Packages: Once a package has been picked up, the user can remove the packages by owner, by location, or they can clear all entries.

Data Persistence: Stores package and location information in a text file (Data.txt) to mantain continuity between sessions and retain valueable package information.

Input Validation: Ensures users provide valid information and allows for operations to be canceled during the process.

-----------------------------------------------------------------------------------------------------------------
Requirements - 
- Python 3.x
- Standard libraries: time, ast (no external dependencies)
-----------------------------------------------------------------------------------------------------------------
Setup - 
1. Clone or download this repository.
2. Verify that a Data.txt file exists with the following structure:
   
     [] # List of package owners

     [] # List of package locations

     [] # List of sections and section sizes

   
4. Run the program:

   python Main.py

-----------------------------------------------------------------------------------------------------------------

Usage - 
When running the program, users can choose from the following commands: 

-----------------------------------------------------------------------------------------------------------------
Command     /      Description

update -             Add new packages and assign storage locations

find -               Locate a package using the owner's name

remove -             Remove packages by name or location, or remove all packages at once

stop -               Save all data and exit the program
    
details -            Display detailed instructions for all commands

-----------------------------------------------------------------------------------------------------------------

The program will display package locations in a clear formate for easy verification and retreival.

-----------------------------------------------------------------------------------------------------------------
Design Notes - 
- Internal Use: This tool is intended for office staff only -- it is not public-facing
  
- Data Handling: Uses lists of lists to store and change package and location information effectively

- Modular Functions: Organized into clear functions for readability and maintainability.

- Storage Optimization: Automatically calculates positions based on row and column constraints, preventing overlaps
------------------------------------------------------------------------------------------------------------------
