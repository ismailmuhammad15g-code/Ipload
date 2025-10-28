# دليل النشر الشامل - Deployment Guide

## 🚀 طرق النشر المتاحة

هذا البوت جاهز للنشر على عدة منصات. اختر الطريقة المناسبة لك:

---

## 1️⃣ النشر على Heroku (مجاني)

### الخطوات:

1. **إنشاء حساب على Heroku**
   - اذهب إلى: https://heroku.com
   - سجل حساب جديد مجاناً

2. **تثبيت Heroku CLI**
```bash
# Windows
# قم بتحميل المثبت من: https://devcenter.heroku.com/articles/heroku-cli

# Mac
brew tap heroku/brew && brew install heroku

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

3. **تسجيل الدخول**
```bash
heroku login
```

4. **إنشاء التطبيق**
```bash
cd Ipload
heroku create ipload-bot-unique-name
```

5. **إضافة المتغيرات**
```bash
heroku config:set BOT_TOKEN=7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo
```

6. **نشر الكود**
```bash
git push heroku main
```

7. **تشغيل البوت**
```bash
heroku ps:scale worker=1
```

8. **مراقبة السجلات**
```bash
heroku logs --tail
```

✅ **البوت الآن يعمل على Heroku!**

---

## 2️⃣ النشر على Railway.app (سهل ومجاني)

1. **اذهب إلى**: https://railway.app
2. **سجل دخول** باستخدام GitHub
3. **اضغط "New Project"**
4. **اختر "Deploy from GitHub repo"**
5. **اختر مستودع Ipload**
6. **أضف المتغيرات البيئية**:
   - `BOT_TOKEN`: `7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo`
7. **انقر Deploy**

✅ **البوت سيعمل تلقائياً!**

---

## 3️⃣ النشر على VPS (خادم خاص)

### المتطلبات:
- خادم Ubuntu/Debian
- Python 3.11+
- صلاحيات sudo

### الخطوات:

1. **الاتصال بالخادم**
```bash
ssh root@your-server-ip
```

2. **تحديث النظام**
```bash
apt update && apt upgrade -y
apt install python3 python3-pip git -y
```

3. **استنساخ المشروع**
```bash
cd /opt
git clone https://github.com/ismailmuhammad15g-code/Ipload.git
cd Ipload
```

4. **تثبيت المتطلبات**
```bash
pip3 install -r requirements.txt
```

5. **إنشاء خدمة systemd**
```bash
cp telegram-bot.service /etc/systemd/system/
```

6. **تعديل ملف الخدمة** (إذا لزم الأمر)
```bash
nano /etc/systemd/system/telegram-bot.service
```

7. **تفعيل وتشغيل الخدمة**
```bash
systemctl daemon-reload
systemctl enable telegram-bot
systemctl start telegram-bot
```

8. **التحقق من الحالة**
```bash
systemctl status telegram-bot
```

9. **مراقبة السجلات**
```bash
journalctl -u telegram-bot -f
```

✅ **البوت يعمل الآن كخدمة دائمة!**

---

## 4️⃣ النشر باستخدام Docker

### الطريقة الأولى: Docker فقط

1. **بناء الصورة**
```bash
cd Ipload
docker build -t ipload-bot .
```

2. **تشغيل الحاوية**
```bash
docker run -d \
  --name ipload-bot \
  --restart unless-stopped \
  -e BOT_TOKEN=7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo \
  -v $(pwd)/data:/app/data \
  ipload-bot
```

3. **مشاهدة السجلات**
```bash
docker logs -f ipload-bot
```

### الطريقة الثانية: Docker Compose

1. **تشغيل باستخدام docker-compose**
```bash
docker-compose up -d
```

2. **مشاهدة السجلات**
```bash
docker-compose logs -f
```

3. **إيقاف البوت**
```bash
docker-compose down
```

✅ **البوت يعمل في حاوية Docker!**

---

## 5️⃣ النشر على Render.com (مجاني)

1. **اذهب إلى**: https://render.com
2. **سجل دخول** وأنشئ حساب
3. **اضغط "New +"** واختر **"Background Worker"**
4. **اربط مستودع GitHub**
5. **املأ البيانات**:
   - **Name**: ipload-bot
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
6. **أضف المتغيرات البيئية**:
   - `BOT_TOKEN`: `7933653463:AAEQ7wrD-XH4p6SOSLpXfHo36PmW77AOKAo`
7. **انقر "Create Web Service"**

✅ **البوت سيبدأ العمل تلقائياً!**

---

## 6️⃣ التشغيل المحلي (للتطوير)

### الطريقة الأولى: مباشرة

```bash
cd Ipload
pip install -r requirements.txt
python bot.py
```

### الطريقة الثانية: باستخدام السكريبت

```bash
cd Ipload
./start.sh
```

---

## 🔧 نصائح مهمة

### الأمان:
- ⚠️ **لا تشارك توكن البوت مع أحد**
- 🔒 استخدم `.env` للتوكن في البيئة المحلية
- 🛡️ فعّل المصادقة الثنائية على حساب Telegram

### الأداء:
- 📊 راقب استخدام الذاكرة
- 💾 احتفظ بنسخة احتياطية من قاعدة البيانات
- 🔄 أعد تشغيل البوت بشكل دوري

### الصيانة:
- 📝 راجع السجلات بانتظام
- 🔄 حدّث المكتبات عند توفر تحديثات أمنية
- 🧪 اختبر المميزات الجديدة قبل النشر

---

## 🆘 حل المشاكل

### البوت لا يستجيب:
```bash
# تحقق من السجلات
heroku logs --tail  # Heroku
journalctl -u telegram-bot -f  # systemd
docker logs -f ipload-bot  # Docker
```

### خطأ في قاعدة البيانات:
```bash
# احذف قاعدة البيانات وأعد تشغيل البوت
rm bot_database.db
systemctl restart telegram-bot
```

### خطأ في التوكن:
- تأكد من صحة التوكن
- تأكد من أن البوت لم يتم حذفه من BotFather
- تحقق من المتغيرات البيئية

---

## 📞 الدعم

إذا واجهت أي مشكلة:
1. راجع السجلات أولاً
2. تأكد من تثبيت جميع المتطلبات
3. تحقق من اتصال الإنترنت
4. افتح issue على GitHub

---

✅ **البوت جاهز 100% للنشر على أي منصة!**
