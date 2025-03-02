import mysql.connector

config = {
    "host": "svc.sel4.cloudtype.app",       # MySQL 서버 주소 (원격이면 IP 입력)
    "port": "30468",
    "user": "root",            # MySQL 사용자명
    "password": "Awdzsc010!@dbr",  # MySQL 비밀번호
    "database": "wbDB"   # 사용할 데이터베이스
}

try:
    # MySQL 연결 시도
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print("✅ MySQL 연결 성공!")
    
    cursor = conn.cursor()

    cursor.execute("""
    SHOW DATABASES;
    """)
    # 연결 종료
    conn.close()

except mysql.connector.Error as e:
    print(f"❌ MySQL 연결 실패: {e}")