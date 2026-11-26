import os
import oracledb
from dotenv import load_dotenv

# 1. 불러오기
load_dotenv()
ora_conn = os.getenv('ora_conn')

# 2. db연결
conn = oracledb.connect(ora_conn)  # 접속 테이블창
cursor = conn.cursor()             # 입력 창

# 3. 쿼리작성실행
sql ='select * from event'      #작성
cursor.execute(sql)

# 4. 데이터정보전달
rows = cursor.fetchall()    

# 5. 데이터 출력
for row in rows:
    print(row[0],row[1],row[2],row[3])


# 5-2. insert,update,delete 할 경우
# insert - board
# insert - file1
# insert - file2
# insert - file3

# conn.commit()
# conn.rollback()     #변경 내용을 취소하고 마지막 COMMIT 상태로 복구

# 6. db정보 닫기 
cursor.close()
conn.close()

