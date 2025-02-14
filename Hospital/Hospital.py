from abc import ABC, abstractmethod
import re
import datetime

# Logging Decorator
def log_action(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            with open("log.txt", "a") as log_file:
                log_file.write(f"[{datetime.datetime.now()}] {func.__name__} called with {', '.join(repr(arg) for arg in args[1:])}\n")
            return result
        except Exception as e:
            with open("log.txt", "a") as log_file:
                log_file.write(f"[{datetime.datetime.now()}] ERROR in {func.__name__}: {str(e)}\n")
            raise e
    return wrapper

# Email validation function
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Custom Exceptions
class InvalidJobError(Exception):
    def __init__(self, msg):
        super().__init__(f"InvalidJobError: {msg}")

class ApplicationError(Exception):
    def __init__(self, msg):
        super().__init__(f"ApplicationError: {msg}")

class SearchError(Exception):
    def __init__(self, msg):
        super().__init__(f"SearchError: {msg}")

# Validator Descriptor
class Validator:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"'{self.name}' must be of type '{self.expected_type.__name__}'")

        if isinstance(value, str) and not value.strip():
            raise ValueError(f"'{self.name}' cannot be an empty string.")
        
        if isinstance(value, int) and value < 0:
            raise ValueError(f"'{self.name}' must be a positive integer.")

        if self.name == "email" and not is_valid_email(value):
            raise ValueError(f"'{self.name}' must be a valid email.")

        instance.__dict__[self.name] = value

# Abstract JobPosition Class
class JobPosition(ABC):
    title = Validator(str)
    salary = Validator(int)

    def __init__(self, title, description, salary, company):
        self.title = title
        self.description = description
        self.salary = salary
        self.company = company
        self.applicants = []  

    def __repr__(self):
        return f"JobPosition(title={self.title!r}, salary={self.salary}, company={self.company.name!r})"

    @log_action
    def apply(self, seeker):
        if not isinstance(seeker, JobSeeker):
            raise TypeError(f"'{seeker}' is not a valid JobSeeker instance.")

        if not seeker.resume.strip():
            raise ApplicationError("Resume is required to apply for a job.")

        self.applicants.append(seeker)
        seeker.applied_jobs.append(self)
        print(f"{seeker.name} successfully applied for {self.title} at {self.company.name}")

    def get_details(self):
        return f"Title: {self.title} | Description: {self.description} | Salary: {self.salary} | Company: {self.company.name}"

    @abstractmethod
    def job_type(self):
        pass

class FullTimeJob(JobPosition):
    def job_type(self):
        return "Full-Time"

class PartTimeJob(JobPosition):
    def job_type(self):
        return "Part-Time"

# Company Class
class Company:
    name = Validator(str)
    email = Validator(str)

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.job_postings = []

    def __repr__(self):
        return f"Company(name={self.name!r}, email={self.email!r})"

    @log_action
    def add_job(self, job):
        if not isinstance(job, JobPosition):
            raise TypeError(f"'job' must be a 'JobPosition' instance.")
        self.job_postings.append(job)

    @log_action
    def remove_job(self, job):
        if job not in self.job_postings:
            raise ValueError(f"'{job.title}' is not listed in {self.name}'s job postings.")
        self.job_postings.remove(job)

    def list_jobs(self):
        print(f"-------'{self.name}' Company's Job Postings-----")
        for job in self.job_postings:
            print(job.get_details())

    def review_applications(self):
        print(f"--- Reviewing Applications for {self.name} ---")
        for job in self.job_postings:
            print(f"\n{job.title} Applicants:")
            for applicant in job.applicants:
                print(f"- {applicant.name} ({applicant.email})")

# JobSeeker Class
class JobSeeker:
    name = Validator(str)
    email = Validator(str)

    def __init__(self, name, email, resume):
        self.name = name
        self.email = email
        self.resume = resume
        self.applied_jobs = []

    def __repr__(self):
        return f"JobSeeker(name={self.name!r}, email={self.email!r})"

    @log_action
    def search_jobs(self, title, company):
        matching_jobs = [job for job in company.job_postings if job.title == title]
        if not matching_jobs:
            raise SearchError(f"No jobs found for '{title}' at {company.name}")
        
        print(f"----- Matching Jobs at {company.name} -----")
        for job in matching_jobs:
            print(job.get_details())

    def view_applied_jobs(self):
        if not self.applied_jobs:
            print("You haven't applied for any jobs yet.")
        else:
            print("----- Applied Jobs -----")
            for job in self.applied_jobs:
                print(job.get_details())

# Example Usage
if __name__ == "__main__":
    c1 = Company('AMD', 'amd@mail.com')

    ftj1 = FullTimeJob('Developer', 'Python Developer', 1000000, c1)   
    ptj1 = PartTimeJob('Tester', 'Software Tester', 500000, c1)  

    c1.add_job(ftj1)
    c1.add_job(ptj1)

    c1.list_jobs()

    js1 = JobSeeker('John Doe', 'john.doe@mail.com', 'Experienced Python Developer')

    js1.search_jobs('Developer', c1)

    ftj1.apply(js1)

    js1.view_applied_jobs()

    c1.review_applications()
