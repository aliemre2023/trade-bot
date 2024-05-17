from wallet import Wallet

my_wallet = Wallet("Ali Emre")

#my_wallet.add_money(1000)

my_wallet.buy("MGROS.IS", 15)
my_wallet.buy("AKBNK.IS", 10)

my_wallet.show_asset()
my_wallet.save_wallet()



