from telegram import Update , ReplyKeyboardMarkup 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
from databaseconfig import dbconnect

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv 
import os 

load_dotenv()

# Conversation States 
CLASS,STUDENTID,ATTCODE = range(3) 

# Ask for CLASS 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["Nodejs B1","Python B2","Reactjs B3","WDF 15"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(f'Please choose your class : ',reply_markup=markup)
    return CLASS

# Temp Save CLASS and Ask for STUDENTID 
async def getclass(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["class"] = update.message.text
    await update.message.reply_text(f'Enter your Student ID (eg., WDF1001) : ')
    return STUDENTID

# Temp Save STUDENTID and Ask for ATTCODE 
async def getstudentid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["studentid"] = update.message.text
    await update.message.reply_text(f'Enter your Attendance Code (eg., 12CB) : ')
    return ATTCODE

# Temp Save ATTCODE and insert to DB 
async def getattcode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["attcode"] = update.message.text
    user = update.effective_user

    user_class = context.user_data["class"]
    user_studentid = context.user_data["studentid"]
    user_attcode = context.user_data["attcode"]

    insert_sql = "INSERT INTO attendances(user_id,class,studentid,attcode) VALUE (%s,%s,%s,%s)"
    value_sql = (user.id,user_class,user_studentid,user_attcode)

    # Insert into Mysql 
    conn = dbconnect()

    if conn.is_connected():
        cursor = conn.cursor() # Get a cursor 

        try: 
            cursor.execute(insert_sql,value_sql)
            conn.commit()
            await update.message.reply_text(f'Thank you! You submitted ATT form.')
            print(f"Data Inserted, ID by is {cursor.lastrowid}")
        except Error as e:
            await update.message.reply_text(f"An unexpected error : {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        await update.message.reply_text("Database connection error!")
    
    return ConversationHandler.END

# Fetch own Data 
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    select_sql = 'SELECT class,studentid,attcode,created_at FROM attendances WHERE user_id = %s ORDER BY created_at DESC'

    # Insert into Mysql 
    conn = dbconnect()

    if conn.is_connected():
        cursor = conn.cursor(dictionary=True) # Get a cursor 

        try: 
            cursor.execute(select_sql,(user.id,))
            rows = cursor.fetchall()

            if rows: 
                reportmessage = "Your Attendance Records\n\n"
                for row in rows:

                    # => conn.cursor() or cursor = conn.cursor(dictionary=False)

                    # reportmessage += (
                    #     f"Class : {row[0]} \n"
                    #     f"Student ID : {row[1]} \n"
                    #     f"Attendance Code : {row[2]} \n"
                    #     f"Date : {row[3]} \n\n"
                    # )

                    # => conn.cursor() or cursor = conn.cursor(dictionary=True)

                    reportmessage += (
                        f"Class : {row['class']} \n"
                        f"Student ID : {row['studentid']} \n"
                        f"Attendance Code : {row['attcode']} \n"
                        f"Date : {row['created_at']} \n\n"
                    )
            else: 
                reportmessage = "No attendance records found!"

            await update.message.reply_text(reportmessage)

        finally:
            cursor.close()
            conn.close()
    else:
        await update.message.reply_text("Database connection error!")
    
    return ConversationHandler.END

# Cancel command "/cancel"
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Registeration cancelled!")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CLASS:[MessageHandler(filters.TEXT & ~filters.COMMAND, getclass)],
            STUDENTID:[MessageHandler(filters.TEXT & ~filters.COMMAND, getstudentid)],
            ATTCODE:[MessageHandler(filters.TEXT & ~filters.COMMAND, getattcode)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler('report',report))
    print("Bot is running....")
    app.run_polling()

if __name__ == "__main__":
    main()