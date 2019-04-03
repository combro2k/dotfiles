#! /usr/bin/env python3

from subprocess import run, Popen, PIPE

import json, pyperclip, sys

class LastPass():

    def __init__(self):
        try:
            q = ['/usr/bin/lpass', 'status']
            r = run(q, stdout=PIPE)

            if r.returncode != 0:
                print('Please login first!')

                e = input('Please enter email adress: ')
                q = ['/usr/bin/lpass', 'login', e]
                r = run(q, stdout=PIPE)

                print('')

        except Exception as e:
            print(e)

            sys.exit(255)

    def run(self):
        try:
            if len(sys.argv) < 2:
                print('No query given!')

                sys.exit(1)

            item = sys.argv[1]

            q = ['/usr/bin/lpass', 'show', '-j', item]
            result = json.loads(Popen(q, stdout=PIPE).communicate()[0])
            r = result[0]

            if 'password' in r:
                try:
                    pyperclip.copy(r['password'])
                    r['password'] = 'Copied to clipboard'
                except NotImplementedError as e:
                    pass
            t = """==== %s ====
ID:
 %s
URL:
 %s
Username:
 %s
Password:
 %s
Notes:
 %s

===============""" % (
                r['fullname']   if 'fullname' in r              else 'N/A',
                r['id']         if 'id' in r                    else 'N/A',
                r['url']        if 'url' in r                   else 'None',
                r['username']   if 'username' in r              else 'N/A',
                r['password']   if 'password' in r              else 'N/A',
                r['note']       if 'note' in r                  else 'N/A',
            )

            print(t)

        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = LastPass()
    app.run()
