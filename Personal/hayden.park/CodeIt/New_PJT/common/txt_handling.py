import os
import argentX as arg
import metamask as meta

data = []
wallet_pw = '12341234'
path = os.path.dirname(__file__)+"\\"+"result_wallet.txt"

# def create_metamask(wallet_pw):
#     meta.pin_to_extensions()
#     meta.create_wallet(wallet_pw)

# def create_argentX(wallet_pw):
#     arg.pin_to_extensions()
#     arg.create_wallet(wallet_pw)

# def get_info_metamask(wallet_pw):
#     data.append(meta.get_recovery_phrase(wallet_pw))
#     data.append(meta.get_wallet_address())

# def get_info_argentX(wallet_pw):
#     data.append(arg.init_recovery_phrase())
#     data.append(arg.get_wallet_address())



f = open(path, "a+")

# create_metamask(wallet_pw)
create_argentX(wallet_pw)
get_info_metamask(wallet_pw)
get_info_argentX(wallet_pw)

f.write('100')
f.write('\n')
for text in data:
    f.write(text)
    f.write("\n")

f.close()