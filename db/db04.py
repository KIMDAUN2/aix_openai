# 접속
import oracledb
import os
from dotenv import load_dotenv

load_dotenv()
ora_conn = os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)
cursor = conn.cursor()

# 검색
# kor_loan_status테이블에서
# 지역별로 그룹핑 후, 주택담보대출을 출력하시오.

#------------------------------
# 실행문 --- select
sql = f'''
select region,sum(loan_jan_amt) as amt
from kor_loan_status
where gubun='주택담보대출'
group by region
'''

# 실행하고 결과 받기
cursor.execute(sql)   # sql 실행

rows = cursor.fetchall()   # 결과받기 
print(f'지역\t담보대출')
print('-'*40)
for row in rows:
    print('{}\t{}'.format(*row))

#------------------------------
# 닫기
conn.close()