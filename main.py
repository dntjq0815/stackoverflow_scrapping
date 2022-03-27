from scrapper import get_jobs
from save_to_csv import save_to_csv

so_jobs = get_jobs()
save_to_csv(so_jobs)
print(so_jobs)