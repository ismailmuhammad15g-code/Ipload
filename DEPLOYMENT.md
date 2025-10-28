# دليل النشر | Deployment Guide

## نشر على خدمات مختلفة | Deploy to Different Services

### 1. Heroku

#### الخطوات | Steps:

1. أنشئ حساباً على [Heroku](https://heroku.com)
2. ثبت Heroku CLI:
```bash
npm install -g heroku
```

3. تسجيل الدخول:
```bash
heroku login
```

4. إنشاء تطبيق جديد:
```bash
heroku create your-app-name
```

5. إضافة Procfile:
```bash
echo "web: node src/index.js" > Procfile
```

6. النشر:
```bash
git push heroku main
```

7. فتح التطبيق:
```bash
heroku open
```

---

### 2. Vercel

#### الخطوات | Steps:

1. ثبت Vercel CLI:
```bash
npm install -g vercel
```

2. النشر:
```bash
vercel
```

3. اتبع التعليمات التفاعلية

**ملاحظة:** قد تحتاج إلى تعديلات إضافية للعمل مع Serverless

---

### 3. Railway

#### الخطوات | Steps:

1. أنشئ حساباً على [Railway](https://railway.app)
2. اربط مستودع GitHub الخاص بك
3. اختر المشروع
4. سيتم النشر تلقائياً

**المتغيرات البيئية | Environment Variables:**
```
PORT=3000
NODE_ENV=production
```

---

### 4. Render

#### الخطوات | Steps:

1. أنشئ حساباً على [Render](https://render.com)
2. اختر "New Web Service"
3. اربط مستودع GitHub
4. اختر الإعدادات:
   - **Build Command:** `npm install`
   - **Start Command:** `npm start`
   - **Environment:** Node

---

### 5. DigitalOcean App Platform

#### الخطوات | Steps:

1. أنشئ حساباً على [DigitalOcean](https://digitalocean.com)
2. اذهب إلى App Platform
3. اربط مستودع GitHub
4. اختر الإعدادات واضغط "Deploy"

---

### 6. خادم خاص (VPS) | Private Server (VPS)

#### متطلبات | Requirements:
- Ubuntu 20.04+ أو نظام مشابه
- Node.js 14+
- PM2 لإدارة العمليات

#### الخطوات | Steps:

1. تحديث النظام:
```bash
sudo apt update && sudo apt upgrade -y
```

2. تثبيت Node.js:
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

3. تثبيت PM2:
```bash
sudo npm install -g pm2
```

4. استنساخ المشروع:
```bash
git clone https://github.com/ismailmuhammad15g-code/Ipload.git
cd Ipload
```

5. تثبيت المكتبات:
```bash
npm install --production
```

6. تشغيل باستخدام PM2:
```bash
pm2 start src/index.js --name ipload
pm2 save
pm2 startup
```

7. إعداد Nginx (اختياري):
```bash
sudo apt install nginx
```

إنشاء ملف التكوين:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

8. تفعيل الموقع:
```bash
sudo ln -s /etc/nginx/sites-available/ipload /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

9. إعداد SSL مع Let's Encrypt:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## إعدادات الإنتاج | Production Settings

### متغيرات البيئة | Environment Variables

قم بإعداد هذه المتغيرات في بيئة الإنتاج:

```bash
NODE_ENV=production
PORT=3000
MAX_FILE_SIZE=10485760
```

### الأمان | Security

1. استخدم HTTPS دائماً في الإنتاج
2. قم بتحديث المكتبات بانتظام
3. استخدم متغيرات البيئة للمعلومات الحساسة
4. فعّل rate limiting
5. استخدم WAF (Web Application Firewall)

### المراقبة | Monitoring

استخدم خدمات مثل:
- PM2 Monitoring
- New Relic
- Datadog
- CloudWatch (AWS)

### النسخ الاحتياطي | Backup

قم بعمل نسخ احتياطية منتظمة لـ:
- مجلد `uploads/`
- قاعدة البيانات (إن وجدت)
- ملفات التكوين

---

## استكشاف الأخطاء | Troubleshooting

### المشكلة: Application crashes
**الحل:**
- تحقق من السجلات (logs)
- تأكد من توفر الذاكرة
- تحقق من اتصال قاعدة البيانات

### المشكلة: Slow performance
**الحل:**
- استخدم CDN للملفات الثابتة
- فعّل caching
- قم بتحسين قاعدة البيانات
- استخدم load balancing

---

## الصيانة | Maintenance

### التحديثات | Updates

```bash
# سحب آخر التحديثات | Pull latest updates
git pull origin main

# تثبيت التحديثات | Install updates
npm install

# إعادة تشغيل التطبيق | Restart application
pm2 restart ipload
```

### المراقبة | Monitoring

```bash
# عرض الحالة | View status
pm2 status

# عرض السجلات | View logs
pm2 logs ipload

# عرض استخدام الموارد | View resource usage
pm2 monit
```
