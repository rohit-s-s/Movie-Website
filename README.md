# Career-website
The "Career-Website" is a web application built using Flask, a lightweight Python web framework. It serves as a platform for job openings, allowing users to view available job positions and submit job applications.
## Table of Contents
- Features
- Prerequisites
- Installation
- Usage
- Database
- File Structure
- Dependencies

## Features
- View job openings and job details on various pages.
- Submit job applications through an application form.
- Receive feedback and confirmation on successful application submission.
- Modular HTML templates for easier management and consistency.

## Prerequisites
Before running the application, make sure you have the following installed:
- Python (version 3.x recommended)
- MySQL or any compatible database (Planetscale Database is used in this project)
## Installation
1.Clone the repository:


    git clone https://github.com/rohit-s-s/Career-website
2.Install the necessary packages using pip:


    cd career-website
    pip install -r requirements.txt
3.Create the database schema and tables using database.py. Ensure you have your MySQL/Planetscale Database credentials set up in the file.


    python database.py
4.Usage
To run the application, use the following command:


    python main.py
The application will be accessible at http://localhost:5000/ in your web browser.

## Database
The project uses a Planetscale Database to store job openings in the database and collect user-filled job application details in the "application" table.

## File Structure
The main components of the project are organized as follows:
  
    career-website/
    ├── main.py            # Flask application main file
    ├── database.py        # Database setup and interactions
    ├── templates/
    │   ├── about.html
    │   ├── application_form.html
    │   ├── application_submitted.html
    │   ├── banner.html
    │   ├── footer.html
    │   ├── index.html
    │   ├── job_pages.html
    │   ├── jobs.html
    │   └── navbar.html
    ├── static/
    │   └── people.jpg, banner.jpg       # images
    └── requirements.txt   # Dependencies
## Dependencies
The required packages and their versions are listed in the requirements.txt file.

