import bitcoin
import bitcoin.rpc

bitcoin.SelectParams('testnet')
proxy_connection = bitcoin.rpc.Proxy()
# ブロックチェーン情報を取得
print(proxy_connection.getinfo())
