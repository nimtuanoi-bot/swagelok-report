import streamlit as st
import pandas as pd

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Swagelok Inspection", layout="wide")
st.title("🛠 Swagelok Inspection System")

# 2. ฟังก์ชันดึงข้อมูลจาก Excel Master List
@st.cache_data # ช่วยให้โหลดข้อมูลเร็วขึ้น
def load_data():
    try:
        # อ่านไฟล์ Excel ที่เราอัปโหลดขึ้น GitHub
        df = pd.read_excel("master_parts.xlsx")
        return df
    except:
        # ถ้ายังไม่มีไฟล์ ให้สร้างข้อมูลตัวอย่างไว้ก่อน
        return pd.DataFrame({'Cylinder P/N': ['No Data Found'], 'Material': ['-']})

df_master = load_data()

# 3. ส่วนการเลือก Part (Dropdown จะยาวตามรายการใน Excel เลยค่ะ)
st.header("1. Technical Selection")
selected_pn = st.selectbox("เลือก Part Number จาก Master List", df_master['Cylinder P/N'])

# ดึงข้อมูลที่เกี่ยวข้องของ Part นั้นมาโชว์อัตโนมัติ
part_info = df_master[df_master['Cylinder P/N'] == selected_pn].iloc[0]

col1, col2 = st.columns(2)
with col1:
    st.success(f"**Material:** {part_info.get('Material', 'N/A')}")
with col2:
    # สมมติว่ามีคอลัมน์ Working Pressure ใน Excel
    pressure = part_info.get('Working Pressure (bar)', 'N/A')
    st.info(f"**Std. Pressure:** {pressure} bar")

st.divider()

# 4. ส่วนข้อมูลทั่วไป
st.header("2. General Information")
doc_no = st.text_input("Document No.")
customer = st.text_input("Customer Name")

# 5. ปุ่มบันทึก
if st.button("บันทึกข้อมูล"):
    st.balloons() # แสดงความยินดีเมื่อกดบันทึก
    st.write(f"บันทึกข้อมูล {selected_pn} สำหรับลูกค้า {customer} เรียบร้อย!")
