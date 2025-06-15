import sqlite3
from decimal import Decimal
from datetime import datetime, timedelta, date

class BotDBClass:

    def __init__(self, db_file):
        print('DBFILE', db_file)
        self.file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_bot_id):

        result = self.cursor.execute('select user_bot_id from users_baseuser where user_bot_id=?',(user_bot_id,)).fetchall()
        print(bool(len(result)))
        return bool(len(result))
    # def user_profile_exists(self,user_id):
    #     result=self.cursor.execute('select id from users_profile where user_id=?',(user_id,)).fetchall()
    #     return bool(len(result))
    #
    def get_username_user(self, user_bot_id):
        return self.cursor.execute('select username from users_baseuser where user_bot_id=?', (user_bot_id,)).fetchone()[0]
    def get_types(self):
        return self.cursor.execute('select name from property_propertytype').fetchall()
    def get_user_id(self, user_bot_id):
        return self.cursor.execute('select id from users_baseuser where user_bot_id=?', (user_bot_id,)).fetchone()[0]
    #
    # def get_user_id_by_username(self,username):
    #     return self.cursor.execute('select id from auth_user where username=?', (username,)).fetchone()[0]
    #
    # def get_user(self,user_id):
    #     return self.cursor.execute('select * from auth_user where id=?',(user_id,)).fetchone()
    #
    # def get_delivery_point(self,delivery_id):
    #     return self.cursor.execute('select * from order_delivery_id where id=?',(delivery_id,)).fetchone()
    def get_user_profile(self, user_id):
        return self.cursor.execute('select * from users_baseuser where id=?',(user_id,)).fetchone()
    #
    # def check_user(self,username,password):
    #     result = self.cursor.execute('select id from auth_user where username=?',
    #                                  (username,)).fetchone()[0]
    #     return result
    #
    # def add_user(self,username,password,is_superuser,last_name,email,is_staff,is_active,date_joined,first_name):
    #     self.cursor.execute("insert into auth_user (username,password,is_superuser,last_name,email,is_staff,is_active,date_joined,first_name) values (?,?,?,?,?,?,?,?,?)",
    #                         (username, password,is_superuser,last_name,email,is_staff,is_active,date_joined,first_name))
    #     return self.conn.commit()
    # def add_user_profile(self,name,user_id,status,user_bot_id,user_bot_pass):
    #     self.cursor.execute("insert into users_profile (name,sirname,about_user,image,user_id,balance,status,user_bot_id,user_bot_pass) values (?,'','','default.jpg',?,0,?,?,?)",
    #                         (name,user_id,status,user_bot_id,user_bot_pass))
    #     return self.conn.commit()
    #
    # def reg_bot(self,user_bot_id,user_bot_pass,user_id):
    #     with self.conn:
    #         return self.cursor.execute("update  users_profile set user_bot_id=?, user_bot_pass=? where user_id =?", (user_bot_id,user_bot_pass,user_id,))
    #
    # def get_deliveres_on_work(self,user_id):
    #     return self.cursor.execute('select * from order_order where deliver_id=? and delivery_status="on_work"',(user_id,)).fetchall()
    #
    # def check_deliveres_on_waitnig(self,user_id):
    #     dat=datetime.now()
    #     # return  self.cursor.execute('select * from order_order where deliver_id=? and date_created NOT BETWEEN datetime("now", "-30 minutes") AND datetime("now", "localtime") ',(user_id,)).fetchall()
    #     with self.conn:
    #         return self.cursor.execute('update order_order set delivery_status="on_work", date_on_work=? where deliver_id=? and delivery_status="waiting" and date_created NOT BETWEEN datetime("now", "-30 minutes") AND datetime("now", "localtime") ',(dat,user_id,)).fetchall()
    # def get_deliveres_on_status(self,user_id,status):
    #     return self.cursor.execute('select * from order_order where deliver_id=? and delivery_status=?',(user_id,status)).fetchall()
    # def get_delivery(self,number):
    #     return self.cursor.execute('select * from order_order where order_number=?',(number,)).fetchone()
    #
    # def change_balance(self,user_id,balance):
    #     print(user_id,balance)
    #     with self.conn:
    #         return self.cursor.execute("update  users_profile set balance=balance + ? where user_id =?", (balance,user_id))
    # def get_delivery_point(self,delivery_point_id):
    #     return self.cursor.execute('select name,city,street,building,office from order_delivery_point where id=?',(delivery_point_id,)).fetchone()
    #
    # def change_delivery_status(self,number,status):
    #     with self.conn:
    #         dat=datetime.now()
    #         return self.cursor.execute('update order_order set delivery_status=?, date_finished=?  where order_number=?',(status,dat,number))
    #
    # def get_user_balance(self,user_id):
    #     return Decimal(self.cursor.execute('select balance from users_profile where user_bot_id=?',(user_id,)).fetchone()[0])
    #
    # def get_report_info(self,user_id,category_info):
    #     print(user_id,category_info)
    #     if  category_info=="Заказчики":
    #         result = self.cursor.execute(
    #             "SELECT orderer_id FROM order_order WHERE deliver_id = ?",
    #             (user_id,))
    #     elif category_info=="Адреса":
    #         result = self.cursor.execute(
    #             "SELECT delivery_point_id FROM order_order WHERE deliver_id = ?",
    #             (user_id,))
    #
    #     return result.fetchall()
    #
    # def get_period_reports(self,user_id,delivery_status,period):
    #     periods={'День':'start of day','Месяц':'start of month','Неделя':'-6 days','Всего':'-500 days'}
    #     result = self.cursor.execute(
    #             "SELECT * FROM order_order WHERE deliver_id =? AND delivery_status=? AND date_finished BETWEEN datetime('now', ?) AND datetime('now', 'localtime') ORDER BY date_finished",
    #             (user_id, delivery_status,periods[period]))
    #     return result.fetchall()
    # # def get_search(self,user_id,search,operation):
    # #     if search:
    # #         if operation == 's':
    # #             result = self.cursor.execute("SELECT * FROM spents WHERE user_id =? AND spent like ?",
    # #                                      (self.get_user_id(user_id),search.capitalize()+'%')).fetchall()
    # #             return result
    # #         elif operation == 'e':
    # #             result = self.cursor.execute("SELECT * FROM earned WHERE user_id =? AND earn like ?",
    # #                                      (self.get_user_id(user_id),search.capitalize()+'%')).fetchall()
    # #             return result
    # #
    # #     else:
    # #         return None
    # #
    # #

    def close(self):
        self.conn.close()
