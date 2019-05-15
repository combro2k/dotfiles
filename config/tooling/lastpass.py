#! /usr/bin/env python3

from __future__ import print_function

import json
import sys
from datetime import datetime
from subprocess import PIPE, run

try:
    import pyperclip
except ImportError:
    pass


class LastPass(object):

    @staticmethod
    def check_login():
        try:
            q = ['/usr/bin/lpass', 'status']
            r = run(q, stdout=PIPE)

            if r.returncode != 0:
                print('Please login first!')

                e = input('Please enter email adress: ')
                q = ['/usr/bin/lpass', 'login', e]
                r = run(q, stdout=PIPE)

                print('', file=sys.stdout)

        except Exception as e:
            print(e, file=sys.stdout)

            sys.exit(255)

    @staticmethod
    def run():
        try:
            LastPass.check_login()

            clipboard = False

            if len(sys.argv) < 2:
                print('No query given!')

                sys.exit(1)

            item = sys.argv[1]

            q = ['/usr/bin/lpass', 'show', '-j', item]
            r = run(q, stdout=PIPE)
            result = json.loads(r.stdout.decode())
            r = result[0]

            if 'note' in r and r['note'].strip() == '':
                del r['note']

            if 'username' in r and r['username'].strip() == '':
                del r['username']

            if 'last_modified_gmt' in r and r['last_modified_gmt'].strip() != '':
                r['last_modified_gmt'] = datetime. \
                    fromtimestamp(int(r['last_modified_gmt'])). \
                    strftime('%d-%m-%Y %T')

            if 'password' in r and not r['password'].strip() == '':
                try:
                    if 'pyperclip' in sys.modules:
                        print('test')
                        pyperclip.copy(r['password'])
                        r['password'] = 'Copied to clipboard'
                        clipboard = True
                except Exception as e:
                    print('Could not copy password to clipboard: %s' % e)

            if 'url' in r and r['url'] == 'http://sn':
                t = """
\033[95m==== %s ====\033[0m
\033[93mName:\033[0m
 %s
\033[93mModified:\033[0m
 %s
\033[93mShared:\033[0m
 %s
\033[93mFolder:\033[0m
 %s
\033[93mNotes:\033[0m
 %s

===============
                    """ % (
                    r['fullname'] if 'fullname' in r else 'N/A',
                    r['name'] if 'name' in r else 'N/A',
                    r['last_modified_gmt'] if 'last_modified_gmt' in r else 'N/A',
                    r['share'] if 'share' in r else 'NO',
                    r['group'] if 'group' in r else 'N/A',
                    r['note'] if 'note' in r else 'N/A',
                )
            else:
                t = """
\x1b[3m\033[95m==== %s ====\033[0m\x1b[0m
\033[93mName:\033[0m
 %s
\033[93mModified:\033[0m
 %s
\033[93mShared:\033[0m
 %s
\033[93mFolder:\033[0m
 %s
\033[93mURL:\033[0m
 %s
\033[93mUsername:\033[0m
 %s
\033[93mPassword:\033[0m
 %s
\033[93mNotes:\033[0m
 %s

===============
                    """ % (
                    r['fullname'] if 'fullname' in r else 'N/A',
                    r['name'] if 'name' in r else 'N/A',
                    r['last_modified_gmt'] if 'last_modified_gmt' in r else 'N/A',
                    r['share'] if 'share' in r else 'NO',
                    r['group'] if 'group' in r else 'N/A',
                    r['url'] if 'url' in r else 'None',
                    r['username'] if 'username' in r else 'N/A',
                    r['password'] if 'password' in r else 'N/A',
                    r['note'] if 'note' in r else 'N/A',
                )

            print(t.strip(), file=sys.stdout)

            if 'password' in r and not clipboard:
                print('\033[91mWarning: automatic clipboard is not loaded', file=sys.stderr)

        except Exception as e:
            print(e, file=sys.stderr)

        return True


if __name__ == '__main__':
    LastPass.run()
