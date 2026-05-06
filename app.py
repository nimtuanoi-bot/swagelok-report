import streamlit as st
import pandas as pd

st.set_page_config(page_title="Swagelok Inspection", layout="wide")
st.title("🛠 Swagelok Inspection System")

@st.cache_data
def load_data():
    try:
        # อ่านไฟล์ Master List ของคุณ
        df = pd.read_excel("master_parts.xlsx")
        # ลบช่องว่างที่อาจปนมาในชื่อหัวตารางออกให้หมด
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        return None

df_master = load_data()

if df_master is not None:
    st.header("1. Technical Selection")
    
    # ตรวจสอบชื่อคอลัมน์ (ใช้คอลัมน์แรกสุดของไฟล์เป็นตัวเลือกหลัก)
    main_col = df_master.columns[0] 
    
    selected_pn = st.selectbox(f"เลือกรายการจาก {main_col}", df_master[main_col])
    
    # ดึงข้อมูลแถวที่เลือก
    part_info = df_master[df_master[main_col] == selected_pn].iloc[0]
    
    # แสดงข้อมูลอื่น ๆ ที่มีในลิสต์ (เช่น Needle Valve, Visual, Status)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info(f"**Cylinder P/N:** {selected_pn}")
    with c2:
        # ดึงข้อมูลจากคอลัมน์ Needle Valve... ถ้ามี
        val = part_info.get('Needle Valve w/t Rupture Disc P/N', 'N/A')
        st.success(f"**Needle Valve:** {val}")
    with c3:
        status = part_info.get('Status', 'N/A')
        st.warning(f"**Status:** {status}")

    st.divider()
    st.header("2. Inspection Data Entry")
    # เพิ่มช่อง Dropdown อื่น ๆ โดยดึงข้อมูลจากลิสต์ใน Excel
    visual_option = st.selectbox("Visual Check", df_master['Visual'].dropna().unique())
    level_option = st.selectbox("Level", df_master['Level'].dropna().unique())
    
else:
    st.error("❌ ไม่พบไฟล์ 'master_parts.xlsx' หรือหัวตารางไม่ถูกต้อง")
    st.info("กรุณาตรวจสอบว่าชื่อไฟล์ใน GitHub สะกดตรงกับในโค้ดนะคะ")
