import streamlit as st
import pandas as pd

st.set_page_config(page_title="Swagelok Inspection", layout="wide")
st.title("🛠 Swagelok Inspection System")

@st.cache_data
def load_data():
    try:
        # อ่านไฟล์ Excel โดยระบุว่าไม่ต้องสนใจชื่อคอลัมน์ในตอนแรกเพื่อเช็คข้อมูล
        df = pd.read_excel("master_parts.xlsx")
        
        # ลบแถวที่เป็นค่าว่าง (ถ้ามี)
        df = df.dropna(how='all')
        
        # ลบช่องว่างส่วนเกินที่หัวตาราง
        df.columns = [str(c).strip() for c in df.columns]
        
        return df
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
        return None

df_master = load_data()

if df_master is not None:
    st.header("1. Technical Selection")
    
    # ดึงรายชื่อคอลัมน์ทั้งหมดที่มีในไฟล์ออกมาดู
    all_columns = df_master.columns.tolist()
    
    # สร้าง Dropdown จากคอลัมน์แรก (ซึ่งควรจะเป็น Cylinder P/N)
    first_col = all_columns[0]
    
    # กรองเอาเฉพาะแถวที่มีข้อมูล (ไม่เอาแถวที่เป็นค่าว่าง)
    dropdown_list = df_master[first_col].dropna().unique()
    
    selected_item = st.selectbox(f"เลือก {first_col}", dropdown_list)
    
    # แสดงข้อมูลของแถวที่เลือก
    if selected_item:
        item_data = df_master[df_master[first_col] == selected_item].iloc[0]
        
        st.subheader("📋 ข้อมูลทางเทคนิคจากลิสต์")
        # โชว์ข้อมูลทุกอย่างที่มีในแถวนั้นแบบอัตโนมัติ
        cols = st.columns(3)
        for i, col_name in enumerate(all_columns[1:10]): # โชว์ 9 คอลัมน์แรก
            with cols[i % 3]:
                st.write(f"**{col_name}:** {item_data[col_name]}")

    st.divider()
    st.header("2. ข้อมูลอื่นๆ")
    doc_no = st.text_input("Document No.")
    customer = st.text_input("Customer Name")

else:
    st.warning("⚠️ ไม่พบไฟล์ 'master_parts.xlsx' ในระบบ GitHub ของคุณ")
    st.info("กรุณาตรวจสอบว่าคุณได้ Upload ไฟล์ชื่อนี้ขึ้นไปแล้ว และสะกดตัวเล็กตัวใหญ่ถูกต้องนะคะ")
