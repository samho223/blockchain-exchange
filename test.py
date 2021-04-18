from backend.wallet import Wallet
import binascii


wallet = Wallet()

private_key = wallet.private_key()
print(binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'))