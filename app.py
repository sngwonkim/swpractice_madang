import streamlit as st
from sqlalchemy import text

st.set_page_config(page_title="Madang Viewer", layout="centered")

conn = st.connection("neon", type="sql")

col_input, col_btn = st.columns([3, 1])
with col_input:
    name = st.text_input("고객 이름", label_visibility="collapsed", placeholder="고객 이름")
with col_btn:
    clicked = st.button("Search", width="stretch")

if clicked:
    sql = text("""
        SELECT o.orderid, c.name, b.bookname, o.saleprice, o.orderdate
        FROM Customer c, Orders o, Book b
        WHERE c.name = :name
          AND c.custid = o.custid
          AND b.bookid = o.bookid
    """)
    df = conn.query(sql.text, params={"name": name}, ttl=0)
    st.dataframe(df, width="stretch", hide_index=True)
