from ldap3 import ALL, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, BASE, LEVEL, SUBTREE, Connection, Server
import getpass
import os

extensionAttribute = ['cn', 'mail', 'telephoneNumber']  # выводимые атрибуты 

def logging():
    """Logging to ldap-server"""
    login = os.environ['LOGIN']
    passwd = os.environ['PASS']
    ldap = os.environ['SERVER']
    return (login, passwd, ldap)


auth = logging()  # запись списка в переменную

# Connect to LDAP Server
try:
    ldap_server = Server(auth[2], get_info=ALL)
    conn = Connection(ldap_server, auth[0], auth[1], auto_bind=True)
    print(f'Auth to LDAP from user {auth[0]} to server {ldap_server} is OK!')
    print("Start searching...")

except:
    print("Error logging to ldap-server. Try Again.")
    

ldap_search_tree = "OU=Domain Users,DC=icore,DC=local"  # указание поиска по OU

conn.search(
    ldap_search_tree, 
    search_filter='(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2))(telephoneNumber=*)(mail=*)(extensionAttribute4=*)(extensionAttribute5=*))',  # фильтрация поиска 
    search_scope=LEVEL,  # жесткий поиск в определенной OU
    attributes=extensionAttribute  # выводимые атрибуты
)
print("Print the result of search...")
read_entries = conn.entries  # чтение данные из conn.search в переменную

# вывод по строкам
lines = 0
for line in read_entries:
    lines += 1
    print(str(lines) + " " + str(line.cn))  # line.cn <- вожмоность выводить определенный атрибут из допустимых

print(str(len(read_entries)) + " - sum all active users in company")  # опционально