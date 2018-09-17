# python-bitcoinlibライブラリを使用しています
import bitcoin
import bitcoin.rpc
from bitcoin.core import lx

bitcoin.SelectParams('testnet')
proxy_connection = bitcoin.rpc.Proxy()

# 最初のトランザクションID(byte)
txid = 'cbbb2facc3724605c9f2add66a8af1fb6ccaf1bfdc95df30b0fa243229ba696c'
# そのトランザクションの構造を得る
rawtx = proxy_connection.getrawtransaction(lx(txid), True)
print(rawtx['vin'].size)
