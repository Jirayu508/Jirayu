print("������ͺ�����÷�Һѵ��ôԵ")
cred = int(input("��͡�����ͧ�س:"))
if cred <= 30000:
    print("�س�����ö�Ӻѵ���")
elif cred >= 40000 and cred <= 89999:
    print("�س���Է�ԷӺѵ��Թ")
    if cred >= 70000 and cred <= 99999:
        print("�س���Է�ԷӺѵ÷ͧ")
elif cred >= 70000 and cred <= 99999:
    print("�س���Է�ԷӺѵ÷ͧ")
else:
    print("�س���Է�ԷӺѵ� Platinum")
