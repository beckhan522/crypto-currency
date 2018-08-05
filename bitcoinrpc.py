from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332" % (rpc_user, rpc_password))
best_block_hash = rpc_connection.getbestblockhash()
print(rpc_connection.getblock(best_block_hash))
