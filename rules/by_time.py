import time

'''
Name: by_time
Description: Basic jump rule based in time.
Autor: @codexlynx (frogd autor) 
'''

INTERVAL = 3


def rule(ctx):
    if ctx['current']:
        time.sleep(INTERVAL)
        current_id = int(ctx['current']['id'])
        next_id = (current_id + 1) % len(ctx['networks'])
        return ctx['networks'][next_id]
    else:
        return ctx['networks'][0]
