private_key = variable.get('private_key')
with open('./file', 'w+') as f:
    f.writelines(private_key.replace('\r',''))
