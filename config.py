"""
Configuration file for Telegram Bot
Modify these settings as needed
"""

# Bot Settings
BOT_NAME = "Ipload Bot"
BOT_VERSION = "1.0.0"

# Database Settings
DATABASE_NAME = "bot_database.db"
MAX_FILE_SIZE_MB = 50  # Maximum file size in MB

# Messages (Arabic)
WELCOME_MESSAGE_TEMPLATE = """
🎉 مرحباً {name}! 

أهلاً بك في {bot_name} المتطور! 

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

FILE_SAVED_MESSAGE = "✅ تم حفظ {type} بنجاح!\n\n💾 الحجم: {size:.2f} MB"
NO_FILES_MESSAGE = "📭 لم تقم برفع أي ملفات بعد.\n\nأرسل ملفاً الآن لحفظه!"
GALLERY_EMPTY_MESSAGE = "🎨 المعرض فارغ حالياً.\n\nكن أول من يشارك ملفاً!"

# Logging Settings
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO'

# Feature Flags
ENABLE_CONSOLE_INFO = True  # Show info in console
ENABLE_FILE_UPLOAD = True
ENABLE_GALLERY = True
ENABLE_USER_STATS = True
