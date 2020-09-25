import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzAB'\
    'CDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code=''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    
    return code

if __name__ == '__main__':
    code1=generate_code()
    print(code1)
    code2=generate_code()
    print(code2)
    code3=generate_code(6)
    print(code3)