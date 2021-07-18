email = input('Enter your email Id: ').strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
final = 'Your user name is {}, and your domain is {}'.format(username, domain)
print(final)