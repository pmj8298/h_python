import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import DML, Keyword, Wildcard

def format_sql_with_leading_commas(query: str) -> str:
    formatted = sqlparse.format(query, keyword_case="upper", strip_whitespace=True)
    parsed = sqlparse.parse(formatted)[0]

    result_lines = []
    inside_select = False

    for token in parsed.tokens:
        # SELECT 처리
        if token.ttype is DML and token.value.upper() == "SELECT":
            inside_select = True
            result_lines.append("SELECT")
        # 여러 컬럼 (IdentifierList)
        elif inside_select and isinstance(token, IdentifierList):
            identifiers = [str(i).strip() for i in token.get_identifiers()]
            result_lines[-1] += f" {identifiers[0]}"
            for col in identifiers[1:]:
                result_lines.append(f"     , {col}")
            inside_select = False
        elif inside_select and (isinstance(token, Identifier) or token.ttype is Wildcard):
            result_lines[-1] += f" {str(token).strip()}"
            inside_select = False
        
        elif token.ttype is Keyword and token.value.upper() == "FROM":
            result_lines.append(f"  {token.value.upper()}")
        else:
            if str(token).strip():
                # FROM 다음 테이블명 붙이기
                if result_lines and result_lines[-1].strip() == "FROM":
                    result_lines[-1] += f" {str(token).strip()}"
                else:
                    result_lines.append(str(token).strip())

    return "\n".join(result_lines)


if __name__ == "__main__":
    query = input("SQL 쿼리를 입력하세요: ")
    print("\n=== 정렬된 쿼리 ===")
    print(format_sql_with_leading_commas(query))
