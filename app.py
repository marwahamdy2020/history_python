from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mysql.connector import connect


app = Flask(__name__)

app.config.from_object('config.default')  # include config file default
# db = SQLAlchemy(app)


@app.route("/")
def home_page():
    return "hello app history log"


#############----------------------connect with old data base----------------------##########################

configDB = connect(
    host='localhost',
    user='root',
    passwd='',
    database='fastnet_fastplay_v2'
)

cursor = configDB.cursor()
##################----------- method for insert log data in db table action_log---------------#############


def logAllActions(logData={'UserId': 0, 'GmID': 0, 'SubscriptionId': 0, 'OrgId': 0, 'PayType': "", 'Cost': 0, 'CouponCode': '', 'Note': "", 'PolicyId': 0, 'IsMedical': 0, 'SrcType': '', 'LogType': 0, 'ContactId': 0}):

    sql = "INSERT INTO actions_log (actions_log_user_id , actions_log_class_id , actions_log_subscription_id ,actions_log_org_id , actions_log_payment_type , actions_log_cost ,actions_log_coupon_code ,actions_log_note, actions_log_policy_id, actions_log_is_medical, actions_log_src_type ,actions_log_action_type_id , actions_log_contact_id) VALUES (%s ,%s, %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s)"

    val = (logData['UserId'], logData['GmID'], logData['SubscriptionId'], logData['OrgId'], logData['PayType'], logData['Cost'], logData['CouponCode'],
           logData['Note'], logData['PolicyId'], logData['IsMedical'], logData['SrcType'], logData['LogType'], logData['ContactId'])

    cursor.execute(sql, val)
    configDB.commit()


# call method for execution
logAllActions()

# close connect db
cursor.close()
configDB.close()

#######################################################################################################

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
