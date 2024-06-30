

loglevel = 'info'
workers = 4
worker_class = 'sync'
worker_tmp_dir = '/tmp'
bind = '0.0.0.0:8000'
pidfile = '/tmp/gunicorn.pid'
umask = 0
user = 'www-data'
group = 'www-data'

errorlog = '-'
accesslog = '-'

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'



