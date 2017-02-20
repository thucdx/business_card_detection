import os
path = os.path.dirname(os.path.abspath(__file__))

common_job_titles = []

with open(path + '/../data/common_job_name') as common_job_names:
    for job_name in common_job_names:
        job_name = job_name.decode('utf8').strip().lower()
        if len(job_name) > 0:
            common_job_titles.append(job_name)


def is_job_title(line):
    line = line.decode('utf8').lower()
    for title in common_job_titles:
        if line.find(title) >= 0:
            return True
    return False