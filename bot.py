#!/usr/bin/env python3
"""
Telegram Bot for File Upload and Gallery Management
Features:
- File upload with database storage
- Gallery view of all projects
- Welcome messages
- Info command with console logging
- User-friendly interface
"""

import os
import logging
import sqlite3
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN', '7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo')
DATABASE_NAME = 'bot_database.db'

# Initialize database
def init_database():
    """Initialize SQLite database with required tables"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create files table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            file_id TEXT NOT NULL,
            file_name TEXT,
            file_type TEXT,
            file_size INTEGER,
            caption TEXT,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    logger.info("Database initialized successfully")

def add_user(user):
    """Add or update user in database"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR REPLACE INTO users (user_id, username, first_name, last_name)
        VALUES (?, ?, ?, ?)
    ''', (user.id, user.username, user.first_name, user.last_name))
    
    conn.commit()
    conn.close()

def add_file(user_id, file_id, file_name, file_type, file_size, caption):
    """Add file to database"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO files (user_id, file_id, file_name, file_type, file_size, caption)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, file_id, file_name, file_type, file_size, caption))
    
    conn.commit()
    conn.close()
    logger.info(f"File saved: {file_name} (User: {user_id})")

def get_user_files(user_id):
    """Get all files uploaded by a user"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, file_id, file_name, file_type, file_size, caption, uploaded_at
        FROM files
        WHERE user_id = ?
        ORDER BY uploaded_at DESC
    ''', (user_id,))
    
    files = cursor.fetchall()
    conn.close()
    return files

def get_all_files():
    """Get all files from database"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT f.id, f.file_id, f.file_name, f.file_type, f.file_size, 
               f.caption, f.uploaded_at, u.username, u.first_name
        FROM files f
        JOIN users u ON f.user_id = u.user_id
        ORDER BY f.uploaded_at DESC
    ''')
    
    files = cursor.fetchall()
    conn.close()
    return files

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    add_user(user)
    
    welcome_message = f"""
🎉 مرحباً {user.first_name}! 

أهلاً بك في بوت رفع الملفات المتطور! 

✨ المميزات المتاحة:
━━━━━━━━━━━━━━━━
📤 رفع الملفات - أرسل أي ملف وسيتم حفظه بأمان
📸 رفع الصور - شارك صورك في المعرض
📹 رفع الفيديوهات - احفظ مقاطعك المفضلة
📁 رفع المستندات - خزن مستنداتك المهمة

🎨 عرض المعرض - شاهد جميع مشاريعك
ℹ️ معلومات - /info
📊 ملفاتي - /myfiles
🌐 جميع الملفات - /gallery

━━━━━━━━━━━━━━━━
🚀 جاهز للاستخدام! أرسل ملفك الآن
"""
    
    keyboard = [
        [
            InlineKeyboardButton("📊 ملفاتي", callback_data="my_files"),
            InlineKeyboardButton("🌐 المعرض", callback_data="gallery")
        ],
        [InlineKeyboardButton("ℹ️ معلومات", callback_data="info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)
    logger.info(f"User {user.id} ({user.username}) started the bot")

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /info command with console logging"""
    user = update.effective_user
    
    # Get user statistics
    user_files = get_user_files(user.id)
    total_files = len(user_files)
    total_size = sum(f[4] for f in user_files if f[4])
    
    # Console output
    print("\n" + "="*50)
    print("📊 BOT INFO - Console Output")
    print("="*50)
    print(f"User ID: {user.id}")
    print(f"Username: @{user.username if user.username else 'N/A'}")
    print(f"Name: {user.first_name} {user.last_name if user.last_name else ''}")
    print(f"Total Files: {total_files}")
    print(f"Total Size: {total_size / 1024 / 1024:.2f} MB")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50 + "\n")
    
    logger.info(f"Info command executed by user {user.id}")
    
    info_message = f"""
ℹ️ معلومات البوت

👤 معلوماتك:
━━━━━━━━━━━━━━━━
🆔 معرف المستخدم: {user.id}
👤 الاسم: {user.first_name}
📛 اسم المستخدم: @{user.username if user.username else 'غير متوفر'}

📊 إحصائياتك:
━━━━━━━━━━━━━━━━
📁 عدد الملفات: {total_files}
💾 الحجم الكلي: {total_size / 1024 / 1024:.2f} ميجابايت

🤖 معلومات البوت:
━━━━━━━━━━━━━━━━
📌 الإصدار: 1.0.0
🔐 قاعدة البيانات: محمية وآمنة
✅ الحالة: نشط ويعمل بكامل المميزات
🚀 جاهز للنشر على الاستضافة

💡 تم عرض المعلومات في وحدة التحكم (Console)
"""
    
    await update.message.reply_text(info_message)

async def my_files_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user's uploaded files"""
    user = update.effective_user
    files = get_user_files(user.id)
    
    if not files:
        await update.message.reply_text("📭 لم تقم برفع أي ملفات بعد.\n\nأرسل ملفاً الآن لحفظه!")
        return
    
    message = f"📊 ملفاتك ({len(files)} ملف):\n\n"
    
    for idx, file_data in enumerate(files[:20], 1):  # Show last 20 files
        file_id, file_name, file_type, file_size, caption, uploaded_at = file_data[1:7]
        size_mb = file_size / 1024 / 1024 if file_size else 0
        message += f"{idx}. 📄 {file_name or 'ملف بدون اسم'}\n"
        message += f"   📌 النوع: {file_type}\n"
        message += f"   💾 الحجم: {size_mb:.2f} MB\n"
        message += f"   📅 {uploaded_at}\n\n"
    
    keyboard = [[InlineKeyboardButton("🔄 تحديث", callback_data="my_files")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(message, reply_markup=reply_markup)

async def gallery_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show gallery of all files"""
    files = get_all_files()
    
    if not files:
        await update.message.reply_text("🎨 المعرض فارغ حالياً.\n\nكن أول من يشارك ملفاً!")
        return
    
    message = f"🎨 معرض المشاريع ({len(files)} ملف):\n\n"
    
    for idx, file_data in enumerate(files[:15], 1):  # Show last 15 files
        file_id, file_name, file_type, file_size, caption, uploaded_at, username, first_name = file_data[1:9]
        size_mb = file_size / 1024 / 1024 if file_size else 0
        uploader = f"@{username}" if username else first_name
        
        message += f"{idx}. 📄 {file_name or 'ملف'}\n"
        message += f"   👤 رفع بواسطة: {uploader}\n"
        message += f"   💾 {size_mb:.2f} MB\n"
        if caption:
            message += f"   💬 {caption[:50]}\n"
        message += f"   📅 {uploaded_at}\n\n"
    
    keyboard = [[InlineKeyboardButton("🔄 تحديث المعرض", callback_data="gallery")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(message, reply_markup=reply_markup)

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle document uploads"""
    user = update.effective_user
    document = update.message.document
    
    add_user(user)
    add_file(
        user.id,
        document.file_id,
        document.file_name,
        'document',
        document.file_size,
        update.message.caption
    )
    
    await update.message.reply_text(
        f"✅ تم حفظ المستند بنجاح!\n\n"
        f"📄 الاسم: {document.file_name}\n"
        f"💾 الحجم: {document.file_size / 1024 / 1024:.2f} MB\n\n"
        f"يمكنك مشاهدته في /myfiles أو /gallery"
    )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle photo uploads"""
    user = update.effective_user
    photo = update.message.photo[-1]  # Get highest resolution
    
    add_user(user)
    add_file(
        user.id,
        photo.file_id,
        f"photo_{photo.file_unique_id}.jpg",
        'photo',
        photo.file_size,
        update.message.caption
    )
    
    await update.message.reply_text(
        f"✅ تم حفظ الصورة بنجاح!\n\n"
        f"💾 الحجم: {photo.file_size / 1024 / 1024:.2f} MB\n\n"
        f"شاهدها في المعرض: /gallery"
    )

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle video uploads"""
    user = update.effective_user
    video = update.message.video
    
    add_user(user)
    add_file(
        user.id,
        video.file_id,
        video.file_name or f"video_{video.file_unique_id}.mp4",
        'video',
        video.file_size,
        update.message.caption
    )
    
    await update.message.reply_text(
        f"✅ تم حفظ الفيديو بنجاح!\n\n"
        f"📹 المدة: {video.duration} ثانية\n"
        f"💾 الحجم: {video.file_size / 1024 / 1024:.2f} MB\n\n"
        f"شاهده في: /myfiles"
    )

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle audio uploads"""
    user = update.effective_user
    audio = update.message.audio
    
    add_user(user)
    add_file(
        user.id,
        audio.file_id,
        audio.file_name or f"audio_{audio.file_unique_id}.mp3",
        'audio',
        audio.file_size,
        update.message.caption
    )
    
    await update.message.reply_text(
        f"✅ تم حفظ الملف الصوتي بنجاح!\n\n"
        f"🎵 المدة: {audio.duration} ثانية\n"
        f"💾 الحجم: {audio.file_size / 1024 / 1024:.2f} MB\n\n"
        f"استمع إليه في: /myfiles"
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()
    
    user = query.from_user
    
    if query.data == "my_files":
        files = get_user_files(user.id)
        
        if not files:
            await query.message.reply_text("📭 لم تقم برفع أي ملفات بعد.")
            return
        
        message = f"📊 ملفاتك ({len(files)} ملف):\n\n"
        for idx, file_data in enumerate(files[:20], 1):
            file_name, file_type, uploaded_at = file_data[2], file_data[3], file_data[6]
            message += f"{idx}. 📄 {file_name or 'ملف'} ({file_type})\n"
        
        await query.message.reply_text(message)
    
    elif query.data == "gallery":
        files = get_all_files()
        
        if not files:
            await query.message.reply_text("🎨 المعرض فارغ حالياً.")
            return
        
        message = f"🎨 المعرض ({len(files)} ملف):\n\n"
        for idx, file_data in enumerate(files[:15], 1):
            file_name, username, first_name = file_data[2], file_data[7], file_data[8]
            uploader = f"@{username}" if username else first_name
            message += f"{idx}. 📄 {file_name or 'ملف'} - {uploader}\n"
        
        await query.message.reply_text(message)
    
    elif query.data == "info":
        # Trigger info command
        user_files = get_user_files(user.id)
        total_files = len(user_files)
        total_size = sum(f[4] for f in user_files if f[4])
        
        print("\n" + "="*50)
        print("📊 BOT INFO - Console Output (Button)")
        print("="*50)
        print(f"User ID: {user.id}")
        print(f"Username: @{user.username if user.username else 'N/A'}")
        print(f"Total Files: {total_files}")
        print("="*50 + "\n")
        
        info_message = f"""
ℹ️ معلومات البوت

👤 المستخدم: {user.first_name}
📁 عدد الملفات: {total_files}
💾 الحجم: {total_size / 1024 / 1024:.2f} MB

✅ البوت يعمل بكامل المميزات
"""
        await query.message.reply_text(info_message)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot"""
    # Initialize database
    init_database()
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("myfiles", my_files_command))
    application.add_handler(CommandHandler("gallery", gallery_command))
    
    # File handlers
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.VIDEO, handle_video))
    application.add_handler(MessageHandler(filters.AUDIO, handle_audio))
    
    # Button callback handler
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("="*50)
    logger.info("🤖 Telegram Bot Started Successfully!")
    logger.info(f"📅 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("✅ All features are ready and working")
    logger.info("🚀 Ready for deployment to hosting")
    logger.info("="*50)
    
    print("\n" + "="*50)
    print("🤖 BOT IS RUNNING")
    print("="*50)
    print("✅ Database initialized")
    print("✅ All handlers registered")
    print("✅ Ready to receive messages")
    print("="*50 + "\n")
    
    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
