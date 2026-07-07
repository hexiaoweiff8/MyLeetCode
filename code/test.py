import requests
import json

def extract_first_json(text):
    """
    从文本中提取第一个完整的 JSON 对象（支持多个 JSON 拼接）。
    返回 dict / list / str / number 等解析后的对象，失败返回 None。
    """
    start = text.find('{')
    if start == -1:
        return None

    brace_count = 0
    in_string = False
    escape = False

    for i in range(start, len(text)):
        ch = text[i]
        if not in_string:
            if ch == '{':
                brace_count += 1
            elif ch == '}':
                brace_count -= 1
                if brace_count == 0:
                    json_str = text[start:i+1]
                    try:
                        return json.loads(json_str)
                    except json.JSONDecodeError:
                        return None
            elif ch == '"':
                in_string = True
        else:
            if escape:
                escape = False
            elif ch == '\\':
                escape = True
            elif ch == '"':
                in_string = False
    return None


def get_first_json_from_api(entId, debug=False):
    """
    根据 entId 查询企业信息，从可能拼接的响应中提取第一个 JSON 对象。
    返回该 JSON 对象（dict），失败返回 None。
    """
    url = "http://192.168.101.61:15001/platform/entInfo/details/queryEntKnowBase"
    params = {"entId": entId}

    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            print(f"HTTP 请求失败，状态码: {response.status_code}")
            return None

        text = response.text
        if debug:
            print(f"原始响应（前500字符）: {text[:500]}")

        first_json = extract_first_json(text)
        if first_json is None:
            print("无法从响应中提取第一个 JSON 对象")
            return None

        if debug:
            print(f"提取到的第一个 JSON: {json.dumps(first_json, ensure_ascii=False, indent=2)[:500]}")

        return first_json

    except requests.exceptions.RequestException as e:
        print(f"网络请求异常: {e}")
        return None
    except Exception as e:
        print(f"未预期的异常: {e}")
        return None


# 使用示例
if __name__ == "__main__":
    result = get_first_json_from_api(1, debug=True)
    if result:
        print("\n第一个 JSON 对象:")
        print(json.dumps(result, ensure_ascii=False, indent=2))

        # 如果需要进一步处理，由调用者自行完成
        if result.get("code") == "00000":
            data = result.get("data")
            # 再根据实际需求提取...