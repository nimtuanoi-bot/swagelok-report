import streamlit as st

# 1. หัวข้อเว็บ
st.title("🛠 Swagelok Inspection System")

# 2. ข้อมูลส่วนกลาง (พิมพ์ครั้งเดียว)
st.header("1. General Information")
doc_no = st.text_input("Document No.")
customer = st.text_input("Customer Name")

# 3. ส่วนการเลือก Part
st.header("2. Technical Selection")
part_list = ['304L-05SF4-150', '304L-05SF4-300', '316L-HDF4-500']
selected_part = st.selectbox("เลือก Part Number", part_list)

# 4. ส่วนอัปโหลดรูป
st.header("3. Photo Upload")
uploaded_file = st.file_uploader("เลือกรูปภาพเพื่อวางใน Report", type=['jpg', 'png'])

if st.button("Preview ข้อมูล"):
    st.success(f"กำลังเตรียมออก Report เลขที่: {doc_no}")
    st.info(f"ลูกค้า: {customer} | Part: {selected_part}")
