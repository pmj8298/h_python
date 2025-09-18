import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Parenthesis
from sqlparse.tokens import DML, Keyword, Wildcard



    
def format_sql_delete_set(query: str) -> str:
    query = query.strip().rstrip(';')
    query_upper = query.upper()
    
    # delete, SET, WHERE 위치 찾기
    delete_idx = query_upper.find("DELETE")
    from_idx = query_upper.find("FROM")
    where_idx = query_upper.find("WHERE")
    
    # UPDATE 라인
    delete_line = query[:from_idx].strip() if from_idx != -1 else query.strip()
    
    # UPDATE 키워드 끝 위치
    delete_keyword_end = delete_line.upper().find("DELETE") + len("DELETE")
    
    # SET 라인 (UPDATE 키워드 끝과 SET 키워드 끝 맞추기)
    from_line = query[from_idx:where_idx].strip() if from_idx != -1 and where_idx != -1 else query[from_idx:].strip()
    spaces_for_from= " " * (delete_keyword_end - len("FROM"))
    from_line = f"{spaces_for_from}{from_line}"
    
    # WHERE 라인
    where_line = query[where_idx:].strip() if where_idx != -1 else ""
    spaces_for_set = " " * (delete_keyword_end - len("WHERE"))
    where_line = f"{spaces_for_set}{where_line}"
    
    
    # 합치기
    formatted = f"{delete_line}\n{from_line}"
    if where_line:
        formatted += f"\n{where_line}"
    
    return formatted



if __name__ == "__main__":
    query = input("SQL 쿼리를 입력하세요: ")
    print("\n=== 정렬된 쿼리 ===")
    print(format_sql_delete_set(query))
