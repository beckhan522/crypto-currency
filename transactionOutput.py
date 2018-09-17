# python-bitcoinlibライブラリを使用しています
import bitcoin
import bitcoin.rpc
from bitcoin.core import *

bitcoin.SelectParams('mainnet')


def get_total_output():
    proxy_connection = bitcoin.rpc.Proxy()
    # bitcoin rpc proxyにより、最後のブロック情報を取得します
    block_info = proxy_connection.getblock(proxy_connection.getblockhash(proxy_connection.getblockcount()))

    # ブロック情報からtransaction情報を取得します
    vtx = block_info.vtx

    # coinbase transactionを含んで，すべのトランザクションをループ
    totalvout = 0
    for x in range(0, len(vtx)):

        # CTransactionオブジェクト
        thetx = vtx[x]

        # CTransactionオブジェクトからCTxOutオブジェクトズを取得
        vout = thetx.vout

        # トランザクションの中にoutがある場合
        if len(vout) >= 1:
            vov = 0
            for o in range(0, len(vout)):
                # CTxOutオブジェクト
                vo = vout[o]
                # CTxOutオブジェクト(vo)からoutput値を取得し、累計します。
                vov = vov + vo.nValue
            totalvout = totalvout + vov
    return str_money_value(totalvout)


def get_block_height():
    proxy_connection = bitcoin.rpc.Proxy()
    # bitcoin rpc proxyにより、最後のブロック高を取得します
    return proxy_connection.getblockcount()

