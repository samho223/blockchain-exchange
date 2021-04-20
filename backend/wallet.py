
import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Wallet():
    def __init__(self):
        self.privatekey = None
        self.publickey = None

    def private_key(self):
        random_gen = Crypto.Random.new().read
        self.privatekey = RSA.generate(1024, random_gen)
        return self.privatekey

    def public_key(self):
        self.publickey =  self.privatekey.publickey()
        return self.publickey
