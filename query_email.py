# @Author: S. Sharma <m4rtyr>
# @Date:   2020-01-20T10:25:20-06:00
# @Email:  silentcat@protonmail.com
# @Last modified by:   m4rtyr
# @Last modified time: 2020-01-20T11:19:29-06:00



from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from colored import fg, attr
import random

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

def main():

    store = file.Storage('.token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('.credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    messages = results.get('messages', [])
    print('         MAIL\n-----------------------\n')
    for i in range(0, 5):
            msg = service.users().messages().get(userId='me', id=messages[i]['id']).execute()
            print('%s %-100s %s' % (fg(random.randint(9, 15)), msg['snippet'] + '\n', attr(0)))

if __name__ == '__main__':
    main()
