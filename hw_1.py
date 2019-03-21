import subprocess
import locale

print('______________________________Задание_1__________________________________')

string = 'разработка'
print(string)
print(isinstance(string, str))
print(string.encode('utf-8'))
bytes_str = string.encode('utf-8')
print(bytes_str)
print(bytes_str.decode('utf-8'))
print(type(bytes_str))

string_1 = 'сокет'
print(isinstance(string_1, str))
print(string_1)
print(string_1.encode('utf-8'))
bytes_str_1 = string_1.encode('utf-8')
print(bytes_str_1)
print(bytes_str_1.decode('utf-8'))
print(type(bytes_str_1))

string_2 = 'декоратор'
print(string_2)
print(isinstance(string_2, str))
print(string_2.encode('utf-8'))
bytes_str_2 = string_2.encode('utf-8')
print(bytes_str_2)
print(bytes_str_2.decode('utf-8'))
print(type(bytes_str_2))

print('______________________________Задание_2__________________________________')

test = b'class'
print(isinstance(test, bytes))
print(type(test))
print(len(test))

test_1 = b'function' 
print(isinstance(test_1, bytes))
print(type(test_1))
print(len(test_1))

test_2 = b'method'
print(isinstance(test_2, bytes))
print(type(test_2))
print(len(test_2))

print('______________________________Задание_3__________________________________')

bytes_1 = 'attribute'
bytes_1.encode('ascii')
bytes_1_str = bytes_1.encode('ascii')
print(bytes_1_str)

bytes_2 = 'класс'
print('Can not be encode')

bytes_3 = 'функция'
print('Can not be encode')

bytes_4 = 'type'
bytes_4.encode('ascii')
bytes_4_str = bytes_4.encode('ascii')
print(bytes_4_str)

print('______________________________Задание_4__________________________________')

enc_str = 'разработка'
enc_str_bytes = enc_str.encode('utf-8')
print(enc_str_bytes)
dec_str_bytes = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
dec_str = dec_str_bytes.decode('utf-8')
print(dec_str)

enc_str_1 = 'администрирование'
enc_str_bytes_1 = enc_str_1.encode('utf-8')
print(enc_str_bytes_1)
dec_str_bytes_1 = b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
dec_str_1 = dec_str_bytes_1.decode('utf-8')
print(dec_str_1)

enc_str_2 = 'protocol'
enc_str_bytes_2 = enc_str_2.encode('utf-8')
print(enc_str_bytes_2)
dec_str_bytes_2 = b'protocol'
dec_str_2 = dec_str_bytes_2.decode('utf-8')
print(dec_str_2)

enc_str_3 = 'standard'
enc_str_bytes_3 = enc_str_3.encode('utf-8')
print(enc_str_bytes_3)
dec_str_bytes_3 = b'standard'
dec_str_3 = dec_str_bytes_3.decode('utf-8')
print(dec_str_3)

print('______________________________Задание_5__________________________________')

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

args = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

print('______________________________Задание_6__________________________________')

def_coding = locale.getpreferredencoding()
print(def_coding)
t_f = open('test_file.txt')
t_f.close()
print(t_f)
with open('test_file.txt') as t_f:
    for el_str in t_f:
        print(el_str)

