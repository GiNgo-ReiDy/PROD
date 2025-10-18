from rq_scheduler import Scheduler
from redis import Redis


scheduler = Scheduler(connection=Redis())