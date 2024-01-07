import re

def fun(s):
    # return True if s is a valid email, else return False
    s = s.strip()
    valid_pattern = r'([\w-])+[@]{1,1}([a-zA-Z0-9])+[.]{1,1}([a-zA-Z]){1,3}$'
    if re.match(valid_pattern, s):
        return True
    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)