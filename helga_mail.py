import smokesignal

from helga.db import db
from helga.plugins import command


@command('mail', help='send message to offline user, usage: mail <nick> <message>', aliases=['email'])
def mail(client, channel, nick, message, cmd, args):

    if len(args) < 2:
        return u'usage: mail <nick> <message>'

    recipient = args[0]
    msg = ' '.join(args[1:])

    db.mail.insert({
        'sender': nick,
        'recipient': recipient,
        'message': msg,
        'received': False,
        'channel': channel,
    })

    client.msg(channel, 'message sent!')

def check_messages(client, nick):
    """
    Check for messages, output if any.
    """

    unread_messages = db.mail.find({
        'recipient': nick,
        'received': False,
    })

    for message in unread_messages:
        client.msg(
            message['channel'],
            '{}, message from {}: {}'.format(
                message['recipient'],
                message['sender'],
                message['message'],
            )
        )

        db.mail.update_one({
            '_id': message['_id'],
        }, {
            '$set': {'received': True},
        })

@smokesignal.on('user_joined')
def user_joined(client, user, channel):

    check_messages(client, user)

@smokesignal.on('user_rename')
def user_rename(client, oldname, newname):

    check_messages(client, newname)
