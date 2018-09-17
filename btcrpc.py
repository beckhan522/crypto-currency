# python-bitcoinlibライブラリを使用しています
import bitcoin
import bitcoin.rpc

bitcoin.SelectParams('testnet')
proxy_connection = bitcoin.rpc.Proxy()
# ブロックチェーン情報を取得
print('ブロックチェーン情報')
print(proxy_connection.getinfo())
# ウォレット残高を取得
print('ウォレット残高')
print(proxy_connection.getbalance(account='beckhan522'))
# UTXOのリストを取得
print('UTXO')
print(proxy_connection.listunspent())
