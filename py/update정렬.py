import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Parenthesis
from sqlparse.tokens import DML, Keyword, Wildcard



    
def format_sql_update_set(query: str) -> str:
    query = query.strip().rstrip(';')
    query_upper = query.upper()
    
    # UPDATE, SET, WHERE 위치 찾기
    update_idx = query_upper.find("UPDATE")
    set_idx = query_upper.find("SET")
    where_idx = query_upper.find("WHERE")
    
    # UPDATE 라인
    update_line = query[:set_idx].strip() if set_idx != -1 else query.strip()
    
    # UPDATE 키워드 끝 위치
    update_keyword_end = update_line.upper().find("UPDATE") + len("UPDATE")
    
    # SET 라인 (UPDATE 키워드 끝과 SET 키워드 끝 맞추기)
    set_line = query[set_idx:where_idx].strip() if set_idx != -1 and where_idx != -1 else query[set_idx:].strip()
    spaces_for_set = " " * (update_keyword_end - len("SET"))
    set_line = f"{spaces_for_set}{set_line}"
    
    # WHERE 라인
    where_line = query[where_idx:].strip() if where_idx != -1 else ""
    spaces_for_set = " " * (update_keyword_end - len("WHERE"))
    where_line = f"{spaces_for_set}{where_line}"
    
    
    # 합치기
    formatted = f"{update_line}\n{set_line}"
    if where_line:
        formatted += f"\n{where_line}"
    
    return formatted



if __name__ == "__main__":
    query = input("SQL 쿼리를 입력하세요: ")
    print("\n=== 정렬된 쿼리 ===")
    print(format_sql_update_set(query))
