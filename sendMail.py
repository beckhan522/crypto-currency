import smtplib
from email.mime.text import MIMEText
from email.header import Header
from transactionOutput import get_block_height, get_total_output


def create_msg(from_address, to_address, subject, body, encode):
    msg = MIMEText(body, 'plain', encode)
    msg['Subject'] = Header(subject, encode)
    msg['From'] = from_address
    msg['To'] = to_address
    return msg


def send_by_local(from_address, to_address, msg):
    # SMTPの引数省略の場合、SMTPサーバーは localhost:25になる
    s = smtplib.SMTP()
    s.connect()
    s.sendmail(from_address, [to_address], msg.as_string())
    s.close()


if __name__ == '__main__':
    from_addr = 'from@example.com'
    to_addr = 'to@example.com'
    subject = u'mainnet合計出力'
    body = 'ブロック高: %s ' % get_block_height()
    body = body + '\n'
    body = body + '合計出力: %s BTC' % get_total_output()
    encode = 'ISO-2022-JP'

    # 送信用のメッセージを作る
    msg = create_msg(from_addr, to_addr, subject, body, encode)

    # メール送信
    send_by_local(from_addr, to_addr, msg)
