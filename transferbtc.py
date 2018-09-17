# python-bitcoinlibライブラリを使用しています
import bitcoin
import bitcoin.rpc

bitcoin.SelectParams('testnet')
proxy_connection = bitcoin.rpc.Proxy()
# 送金
password = ''
# ウォレットロック解除
proxy_connection.unlockwallet(password, timeout=20)
# 送金(単位satoshi)
txid = proxy_connection.sendtoaddress('mp8ZSsiPBptumHU8mxvY6kNtYW43kfVfmJ', 1000000)
# トランザクション内容の確認txidはbytes形
txinfo = proxy_connection.gettransaction(txid)
print(str(txinfo))


