import task
import sys
import os

last_ip = [1, 0, 0, 0]
ip_file = 'ip_c.txt'

if os.path.isfile(ip_file):

    with open(ip_file, 'r') as fp:
        ip_c = fp.read()
    tmp_ip = list(map(int, ip_c.split('.')))

    if isinstance(tmp_ip, list) and len(tmp_ip) == 4:
        last_ip = tmp_ip
        print("\nStart crawling from "+ ('.'.join(list(map(str, last_ip)))))
    else:
        print("\nread "+ ip_file + ' failed...')
        print('Start crawling from 0.0.0.0\n')


for a in range(1, 256):
    if a < last_ip[0]: continue

    for b in range(0, 256):
        if b < last_ip[1]:
            continue
        last_ip[1] = 0

        for c in range(0, 256):
            if c < last_ip[2]:
                continue
            last_ip[2] = 0

            for d in range(0, 256):
                if d < last_ip[3]:
                    continue
                last_ip[3] = 0

                ip = '.'.join([str(a), str(b), str(c), str(d)])
                try:
                    if os.path.isfile(ip_file):
                        os.remove(ip_file)
                    result = task.ip.delay(ip)
                    print(ip+ '....'+result.get())
                except KeyboardInterrupt as e:
                    with open('ip_c.txt', 'wt') as fp:
                        fp.write(ip)
                        print("\n\nsystem exit...")
                        print('last ip '+ ip +' write in ip_c.txt\n')
                        sys.exit()
