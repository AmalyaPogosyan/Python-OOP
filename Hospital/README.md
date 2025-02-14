# Job Application Management System

This is a Python-based job application management system that allows companies to post job openings and job seekers to apply for them. The system includes validation mechanisms, logging, and custom error handling.

## Features
- Object-Oriented Programming (OOP) principles
- Abstract base classes with `ABC`
- Custom exception handling
- Logging of job applications
- Validation with descriptors
- Email validation

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/AmalyaPogosyan/job-application-system.git
   cd job-application-system
   ```
2. Make sure you have Python installed (version 3.7 or later). You can check your Python version using:
   ```sh
   python --version
   ```
3. Install dependencies (if needed):
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Example Code:

```python
from job_application_system import Company, FullTimeJob, PartTimeJob, JobSeeker

# Create a company
c1 = Company('AMD', 'amd@mail.com')

# Create job postings
ftj1 = FullTimeJob('Developer', 'Python Developer', 1000000, c1)
ptj1 = PartTimeJob('Tester', 'Software Tester', 500000, c1)

# Add jobs to the company
c1.add_job(ftj1)
c1.add_job(ptj1)

# List available jobs
c1.list_jobs()

# Create a job seeker
js1 = JobSeeker('John Doe', 'john.doe@mail.com', 'Experienced Python Developer')

# Search for jobs and apply
js1.search_jobs('Developer', c1)
ftj1.apply(js1)

# View applied jobs
js1.view_applied_jobs()

# Company reviews applications
c1.review_applications()
```

## Logging
All actions such as job applications are logged in `log.txt`. Each entry includes a timestamp and the function called.

## Error Handling
- `InvalidJobError`: Raised when an invalid job type is used.
- `ApplicationError`: Raised when a job seeker applies without a resume.
- `SearchError`: Raised when no matching jobs are found.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Author
Created by [AmalyaPogosyan](https://github.com/AmalyaPogosyan).

