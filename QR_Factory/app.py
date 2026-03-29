import streamlit as st
import qrcode
from PIL import Image
import io
import os

# --- 1. إعدادات التبويبة (بناءً على تعديلاتك) ---
logo_path = "logo3.png" # تأكد من وجود الملفlogo3.png في نفس المجلد
if os.path.exists(logo_path):
    page_icon = Image.open(logo_path)
else:
    page_icon = "💎"

st.set_page_config(
    page_title="QCS - QR Code Service", 
    page_icon=page_icon,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. كود إخفاء البار العلوي وتنسيق لوحة الألوان ---
st.markdown("""
<style>
    /* إخفاء الشريط العلوي بالكامل (الأسود، النقاط، والـ Deploy) */
    header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0px;
    }
    
    /* موازنة المسافة العلوية لتبدأ الصفحة من اللوقو فوراً */
    .stApp {
        background-color: #f9f8f3;
        margin-top: -60px;
    }

    /* باقي التنسيقات الأصلية كما هي تماماً */
    h1 {
        text-align: center;
        color: #1a1a1a;
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    h1 span {
        color: #8b7355;
    }
    .stMarkdown p {
        text-align: center;
        color: #4a4a4a;
        font-family: 'Lora', serif;
        font-size: 1.1rem;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 12px;
        color: #1a1a1a;
    }
    .stTextInput label {
        color: #8b7355;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* تنسيق لوحة اختيار الألوان لتكون أنيقة */
    .stColorPicker label {
        color: #8b7355;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px;
        display: block;
        text-align: center;
    }
    .stColorPicker div[data-testid="stColorPickerColor"] {
        border-radius: 8px !important;
        border: 1px solid #e0e0e0 !important;
    }

    .stButton > button {
        background-color: #8b7355;
        color: #ffffff;
        border: None;
        border-radius: 8px;
        padding: 15px 30px;
        font-weight: 700;
        font-size: 1.1rem;
        width: 100%;
        margin-top: 1rem;
    }
    .stButton > button:hover {
        background-color: #a18a6f;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. محتوى الموقع (كما هو في نسختك) ---

# عرض اللوقو
import os
from PIL import Image

# تأكد إنك حاطط اسم الملف صح (logo3.png)
# هاد السطر بيحكي للبايثون يدور بنفس المجلد اللي فيه ملف الـ app.py حالياً
current_dir = os.path.dirname(__file__)
logo_path = os.path.join(current_dir, "logo3.png")

if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    cols_logo = st.columns([1, 1, 1])
    with cols_logo[1]:
        st.image(logo_img, use_container_width=True)
else:
    # هاي الحركة بس عشان تعرف شو المسار اللي الكود عم يدور فيه حالياً (للتصحيح)
    st.error(f"اللوجو مش موجود بالمسار: {logo_path}")

# العناوين
st.markdown("<h1>Crafting codes into <br><span>digital jewelry.</span></h1>", unsafe_allow_html=True)
st.write("Elevate your connectivity with precision-engineered QR codes designed for the modern aesthetic.")

# الجملة الإضافية التي وضعتها أنت
st.write("Powered by AHMAD ALSARDI")

st.markdown("<br>", unsafe_allow_html=True)

# خانة الرابط
url_input = st.text_input("DESTINATION URL", placeholder="https://yourlink.com")

# --- الإضافة الجديدة: ميزة اختيار الألوان ---
st.markdown("### PERSONALIZE YOUR PIECE")
col_color1, col_color2 = st.columns(2)
with col_color1:
    qr_fill_color = st.color_picker("Code Color", "#000000")
with col_color2:
    qr_back_color = st.color_picker("Background Color", "#FFFFFF")

# زر الإنشاء
if st.button("Generate Signature Code →"):
    if url_input:
        with st.spinner('Engineering...'):
            # توليد الـ QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url_input)
            qr.make(fit=True)
            
            # --- تعديل الـ Python لاستخدام الألوان المختارة ---
            img = qr.make_image(
                fill_color=qr_fill_color, 
                back_color=qr_back_color
            )
            
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.markdown("---")
            st.markdown("<h3 style='text-align: center;'>PREVIEW READY</h3>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                # عرض الصورة الملونة في الموقع
                st.image(byte_im, use_container_width=True)
                st.download_button(
                    label="Download the FUKING PNG",
                    data=byte_im,
                    file_name="Sugar_Lab_QR.png", # اسم الصورة كما اخترته أنت
                    mime="image/png",
                    use_container_width=True
                )
            
            # كود السكرول التلقائي (الذي يستهدف الـ main container)
            st.write('<script>window.parent.document.querySelector(".main").scrollTo(0, 10000);</script>', unsafe_allow_html=True)
    else:
        st.error("Please enter a URL first!")