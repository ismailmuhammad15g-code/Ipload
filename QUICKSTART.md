# 🚀 Quick Start Guide - دليل البدء السريع

## للبدء فوراً (في 3 خطوات)

### الطريقة 1: التشغيل المباشر

```bash
# 1. استنساخ المشروع
git clone https://github.com/ismailmuhammad15g-code/Ipload.git
cd Ipload

# 2. تثبيت المكتبات
pip install -r requirements.txt

# 3. تشغيل البوت
python bot.py
```

✅ **البوت يعمل الآن!**

---

### الطريقة 2: باستخدام السكريبت (الأسهل)

```bash
git clone https://github.com/ismailmuhammad15g-code/Ipload.git
cd Ipload
./start.sh
```

✅ **تم! البوت يعمل**

---

### الطريقة 3: باستخدام Docker (موصى به للإنتاج)

```bash
git clone https://github.com/ismailmuhammad15g-code/Ipload.git
cd Ipload
docker-compose up -d
```

✅ **البوت يعمل في حاوية Docker**

---

## 📱 اختبار البوت

1. افتح تطبيق Telegram
2. ابحث عن البوت الخاص بك
3. أرسل `/start`
4. ستظهر رسالة الترحيب مع القائمة

## 🎯 الأوامر المتاحة

| الأمر | الوصف |
|------|---------|
| `/start` | بدء البوت والترحيب |
| `/info` | عرض المعلومات |
| `/myfiles` | عرض ملفاتك |
| `/gallery` | عرض جميع الملفات |

## 📤 رفع الملفات

ببساطة أرسل:
- 📄 **مستند**: أي ملف
- 📸 **صورة**: صورة مباشرة
- 📹 **فيديو**: مقطع فيديو
- 🎵 **صوت**: ملف صوتي

سيتم حفظه تلقائياً!

## 🔧 تخصيص التوكن

### الطريقة 1: تعديل ملف .env
```bash
echo "BOT_TOKEN=your_token_here" > .env
```

### الطريقة 2: متغير بيئة
```bash
export BOT_TOKEN=your_token_here
python bot.py
```

### الطريقة 3: في الكود مباشرة
عدل `bot.py` السطر 25:
```python
BOT_TOKEN = 'your_token_here'
```

---

## ⚡ نشر سريع

### Heroku (دقيقة واحدة):
```bash
heroku create
heroku config:set BOT_TOKEN=7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo
git push heroku main
heroku ps:scale worker=1
```

### Railway.app (30 ثانية):
1. اذهب إلى https://railway.app
2. اضغط "New Project"
3. اختر "Deploy from GitHub"
4. أضف BOT_TOKEN في المتغيرات
5. انقر Deploy

### Render.com (دقيقة واحدة):
1. اذهب إلى https://render.com
2. أنشئ "Background Worker"
3. اربط GitHub
4. أضف BOT_TOKEN
5. انقر Create

---

## 🆘 حل سريع للمشاكل

### البوت لا يرد؟
```bash
# تحقق من السجلات
python bot.py  # شاهد الأخطاء
```

### خطأ في التوكن؟
- تأكد من التوكن صحيح
- تأكد من BotFather

### خطأ في المكتبات؟
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

---

## ✅ التحقق من عمل البوت

يجب أن ترى في الكونسول:
```
🤖 Telegram Bot Started Successfully!
✅ All features are ready and working
🚀 Ready for deployment to hosting
```

---

## 📞 للمساعدة

- 📖 اقرأ README.md للتفاصيل
- 🚀 راجع DEPLOYMENT.md للنشر
- 🐛 افتح issue على GitHub

---

✨ **البوت جاهز 100% للاستخدام والنشر!**

🎉 **استمتع باستخدام البوت!**
