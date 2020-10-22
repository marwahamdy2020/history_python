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

##------------------------------------[log actin :admin add or edit or delete class]-------------------------------------------#

# actionType = (1) Add , (2)Edit , (3)Delete
# sourceType = web ,ios ,android


def logGame(gmData={'GmID': 0, 'sourceType': "", 'actionType': 0}):
    result1 = " "
    sqlGm = "SELECT * FROM  game WHERE gm_id  = 126620"
    # cursor = configDB.cursor(dictionary=True)
    cursor.execute(sqlGm)
    result1 = cursor.fetchone()

    addGm = "INSERT INTO log_game (log_gm_id,log_gm_title,log_gm_org_id,log_gm_display_org,log_gm_sub_type_id,log_gm_court_id,log_gm_level_id,log_gm_img,log_gm_gender,	log_gm_age,log_gm_age_min,log_gm_age_max,log_gm_min_players,log_gm_max_players,	log_gm_max_players_orig,log_gm_date,log_gm_start_time,log_gm_end_time,log_gm_utc_datetime,log_gm_zip_code,log_gm_city_id,log_gm_country_id,log_gm_loc_lat,log_gm_loc_long,log_gm_loc_desc,log_gm_scope,log_gm_has_gallery,log_gm_desc,log_gm_requirements,log_gm_notes,log_gm_rules,log_gm_kits,log_gm_is_free,log_gm_payment_type,log_attend_type,log_zoom_url,log_zoom_meeting_id,log_gm_fees,log_gm_currency_symbol,log_gm_policy_id,log_gm_is_stop_recurred,log_gm_recurr_id,log_gm_recurr_times,log_gm_recurr_type,log_gm_copy_id,log_gm_copy_ques_from,log_gm_renew_id,log_gm_showMem,log_gm_reqQues, log_gm_end_pause,log_gm_status,log_gm_recurr_cancel_type,log_gm_pid,log_gm_recurr_days_times,log_gm_time_zone,log_gm_created,log_gm_src_type,log_gm_action_type) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )"

    valGm = (result1[0], result1[1], result1[2], result1[3], result1[4], result1[5], result1[6], result1[7], result1[8], result1[9], result1[10], result1[11], result1[12], result1[13], result1[14], result1[15], result1[16], result1[17], result1[18], result1[19], result1[20], result1[21], result1[22], result1[23], result1[24], result1[25], result1[26], result1[27], result1[28], result1[29], result1[30],
             result1[31], result1[32], result1[33], result1[34], result1[35], result1[36], result1[37], result1[38], result1[39], result1[40], result1[41], result1[42], result1[43], result1[44], result1[45], result1[46], result1[47], result1[48], result1[49], result1[50], result1[51], result1[52], result1[53], result1[54], result1[55], gmData['sourceType'], gmData['actionType'])

    cursor.execute(addGm, valGm)
    configDB.commit()


logGame(gmData={'GmID': 126620, 'sourceType': 'web', 'actionType': 1})
# -----close connect db---#
cursor.close()
configDB.close()

#######################################################################################################

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
