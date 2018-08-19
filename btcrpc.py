import bitcoin
import bitcoin.rpc

bitcoin.SelectParams('testnet')
proxy_connection = bitcoin.rpc.Proxy()
print(proxy_connection.getinfo())
