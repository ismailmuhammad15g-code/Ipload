// Get and display IP address
async function getIP() {
    try {
        const response = await fetch('/api/ip');
        const data = await response.json();
        document.getElementById('ip-display').textContent = data.ip;
    } catch (error) {
        document.getElementById('ip-display').textContent = 'خطأ في جلب عنوان IP';
        console.error('Error fetching IP:', error);
    }
}

function refreshIP() {
    document.getElementById('ip-display').textContent = 'جاري التحميل...';
    getIP();
}

// Handle file selection
document.getElementById('file-input').addEventListener('change', function(e) {
    const fileName = e.target.files[0]?.name || 'لم يتم اختيار ملف';
    document.getElementById('file-name').textContent = fileName;
});

// Handle file upload
document.getElementById('upload-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const fileInput = document.getElementById('file-input');
    const statusDiv = document.getElementById('upload-status');
    
    if (!fileInput.files[0]) {
        showStatus('الرجاء اختيار ملف', 'error');
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        statusDiv.textContent = 'جاري رفع الملف...';
        statusDiv.className = '';
        statusDiv.style.display = 'block';

        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            showStatus(`تم رفع الملف بنجاح: ${data.file.originalname}`, 'success');
            fileInput.value = '';
            document.getElementById('file-name').textContent = 'لم يتم اختيار ملف';
            loadFiles();
        } else {
            showStatus(`خطأ: ${data.error}`, 'error');
        }
    } catch (error) {
        showStatus('خطأ في رفع الملف', 'error');
        console.error('Upload error:', error);
    }
});

function showStatus(message, type) {
    const statusDiv = document.getElementById('upload-status');
    statusDiv.textContent = message;
    statusDiv.className = type;
    statusDiv.style.display = 'block';
}

// Load and display files
async function loadFiles() {
    try {
        const response = await fetch('/api/files');
        const data = await response.json();
        
        const filesList = document.getElementById('files-list');
        
        if (data.files.length === 0) {
            filesList.innerHTML = '<p style="text-align: center; color: #666;">لا توجد ملفات مرفوعة</p>';
            return;
        }

        filesList.innerHTML = data.files.map(file => `
            <div class="file-item">
                <div class="filename">📄 ${file.filename}</div>
                <div class="fileinfo">
                    الحجم: ${formatFileSize(file.size)} | 
                    التاريخ: ${new Date(file.created).toLocaleString('ar-SA')}
                </div>
            </div>
        `).join('');
    } catch (error) {
        document.getElementById('files-list').innerHTML = '<p style="text-align: center; color: #dc3545;">خطأ في جلب الملفات</p>';
        console.error('Error loading files:', error);
    }
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 بايت';
    const k = 1024;
    const sizes = ['بايت', 'كيلوبايت', 'ميجابايت', 'جيجابايت'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    getIP();
    loadFiles();
});
