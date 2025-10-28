# Ipload - Telegram File Upload Bot 🤖

بوت تليجرام متكامل لرفع الملفات وإدارة المشاريع مع معرض شامل

## المميزات ✨

- 📤 **رفع الملفات**: رفع جميع أنواع الملفات (مستندات، صور، فيديوهات، ملفات صوتية)
- 💾 **قاعدة بيانات آمنة**: حفظ جميع الملفات في قاعدة بيانات SQLite محمية
- 🎨 **معرض المشاريع**: عرض جميع الملفات المرفوعة في معرض شامل
- 👤 **إدارة المستخدمين**: تتبع المستخدمين وملفاتهم
- ℹ️ **أمر Info**: عرض المعلومات في الكونسول
- 🌐 **جاهز للنشر**: جاهز للرفع على Heroku أو أي استضافة أخرى
- 🔐 **آمن ومحمي**: جميع البيانات محمية ومشفرة

## التثبيت 🚀

### المتطلبات
- Python 3.11+
- pip

### خطوات التثبيت

1. **استنساخ المشروع**
```bash
git clone https://github.com/ismailmuhammad15g-code/Ipload.git
cd Ipload
```

2. **تثبيت المكتبات المطلوبة**
```bash
pip install -r requirements.txt
```

3. **إعداد التوكن**
```bash
# انسخ ملف البيئة
cp .env.example .env

# عدل ملف .env وضع التوكن الخاص بك
# BOT_TOKEN=your_bot_token_here
```

4. **تشغيل البوت**
```bash
python bot.py
```

## الأوامر المتاحة 📋

- `/start` - بدء البوت والحصول على رسالة الترحيب
- `/info` - عرض معلومات البوت والمستخدم (مع عرض في الكونسول)
- `/myfiles` - عرض جميع ملفاتك
- `/gallery` - عرض معرض جميع الملفات

## كيفية الاستخدام 📖

1. ابدأ البوت بإرسال `/start`
2. أرسل أي ملف (صورة، فيديو، مستند، ملف صوتي)
3. سيتم حفظ الملف تلقائياً في قاعدة البيانات
4. شاهد ملفاتك باستخدام `/myfiles`
5. شاهد جميع الملفات في المعرض باستخدام `/gallery`

## النشر على Heroku 🌐

1. **تثبيت Heroku CLI**
```bash
# اتبع التعليمات على https://devcenter.heroku.com/articles/heroku-cli
```

2. **إنشاء تطبيق Heroku**
```bash
heroku login
heroku create your-bot-name
```

3. **إضافة المتغيرات البيئية**
```bash
heroku config:set BOT_TOKEN=7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo
```

4. **نشر البوت**
```bash
git push heroku main
```

5. **تشغيل البوت**
```bash
heroku ps:scale worker=1
```

## النشر على VPS 🖥️

1. **الاتصال بالخادم**
```bash
ssh user@your-server-ip
```

2. **استنساخ المشروع**
```bash
git clone https://github.com/ismailmuhammad15g-code/Ipload.git
cd Ipload
```

3. **تثبيت المتطلبات**
```bash
pip3 install -r requirements.txt
```

4. **تشغيل البوت في الخلفية**
```bash
nohup python3 bot.py &
```

أو استخدام systemd:
```bash
sudo nano /etc/systemd/system/telegram-bot.service
```

أضف:
```ini
[Unit]
Description=Telegram Upload Bot
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/Ipload
Environment="BOT_TOKEN=7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo"
ExecStart=/usr/bin/python3 bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

ثم:
```bash
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
```

## هيكل المشروع 📁

```
Ipload/
├── bot.py              # الملف الرئيسي للبوت
├── requirements.txt    # المكتبات المطلوبة
├── Procfile           # ملف Heroku
├── runtime.txt        # إصدار Python
├── .env.example       # مثال لملف البيئة
├── .gitignore         # ملفات Git المستبعدة
└── README.md          # هذا الملف
```

## الميزات التقنية 🔧

- **قاعدة البيانات**: SQLite مع جداول منظمة للمستخدمين والملفات
- **المكتبات**: python-telegram-bot (أحدث إصدار)
- **التسجيل**: نظام تسجيل شامل مع عرض في الكونسول
- **معالجة الأخطاء**: معالجة شاملة للأخطاء
- **واجهة المستخدم**: أزرار تفاعلية وقوائم منظمة
- **الأمان**: حماية البيانات والملفات

## الدعم 💬

إذا واجهت أي مشكلة أو لديك اقتراح، يرجى فتح issue في GitHub.

## الترخيص 📄

هذا المشروع مفتوح المصدر ومتاح للجميع.

---

صُنع بـ ❤️ للمجتمع العربي