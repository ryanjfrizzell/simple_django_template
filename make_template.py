import django.template as dt
import os

p = os.path.dirname(os.path.abspath(__file__))
search_dir=[os.path.join(p,'templates')]
cfg_val = {
    'user': 'test',
    'pass': 'testpass'
}

c = dt.Context(cfg_val)
eng = dt.Engine()
t = eng.find_template('config.template',dirs=search_dir)
print(t[0].render(context=c))
