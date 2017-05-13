from sqlalchemy import create_engine, MetaData, Column, Table, ForeignKey, Integer, String

class chan(object):
    def __init__(self):
        return

    def initialize_tables():
        try:
            self.engine = create_engine('mysql://root@localhost:3306/chan')#'mysql://{}:{}@{}'.format(os.environ["DB_USERNAME"], os.environ["DB_PASSWORD"], os.environ["DB_CONNECTION_STRING"]), echo=False)
            metadata = MetaData(bind=engine)
            try:
                engine.connect()
            except Exception:
                print 'CHAN:LOG:Creating the database'
                self.engine = create_engine('mysql://root@localhost:3306')
                self.engine.execute("CREATE DATABASE chan")
                self.engine.execute("USE chan")
                self.engine.execute("CREATE TABLE channels(slack_id VARCHAR(9), name VARCHAR (50), is_productive TINYINT, is_active TINYINT, PRIMARY KEY (slack_id))")
                self.engine.execute("CREATE TABLE users(slack_id VARCHAR(9), first_name VARCHAR(40), last_name VARCHAR(40), join_date DATETIME, is_admin TINYINT, is_pb_admin TINYINT, PRIMARY KEY (slack_id))")
                self.engine.execute("CREATE TABLE emojis(name VARCHAR(60), is_custom TINYINT, PRIMARY KEY (name))")
                self.engine.execute("CREATE TABLE commentActivity(from_user_id VARCHAR(9), to_channel_id VARCHAR(9), comment_count INTEGER, PRIMARY KEY (from_user_id, to_channel_id), FOREIGN KEY (from_user_id) REFERENCES users (slack_id), FOREIGN KEY (to_channel_id) REFERENCES channels (slack_id))")
                self.engine.execute("CREATE TABLE emojiActivity(from_user_id VARCHAR(9), to_user_id VARCHAR(9), in_channel_id VARCHAR(9), emoji_name VARCHAR(60), given_count INTEGER, PRIMARY KEY (from_user_id, to_user_id, in_channel_id, emoji_name),  FOREIGN KEY (from_user_id) REFERENCES users (slack_id), FOREIGN KEY (to_user_id) REFERENCES users (slack_id), FOREIGN KEY (in_channel_id) REFERENCES channels (slack_id))")    
                self.engine.execute("CREATE TABLE channelActivity(channel_id VARCHAR(9), hour TINYINT, week_day VARCHAR(2), day_of_month TINYINT, month TINYINT, year SMALLINT, FOREIGN KEY (channel_id) REFERENCES channels (slack_id))")
        except Exception as e:
            print e