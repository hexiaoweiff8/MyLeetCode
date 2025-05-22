from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from nonebot.params import CommandArg
import requests
import os

# 初始化插件信息
__zx_plugin_name__ = "deepseek"
__plugin_usage__ = """
usage：
    deepseek
    指令：
        dp: 内容
""".strip()
__plugin_des__ = "与DeepSeek对话"
__plugin_cmd__ = ["dp:[内容]"]
__plugin_version__ = 0.1
__plugin_author__ = "YourName"

# 定义命令处理器
deepseek_handler = on_command("dp:", aliases={"dp:"}, priority=5, block=True)

# 设置 DeepSeek API 密钥（请替换成你自己的密钥）
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-5fd67f83aa7b4def890c00f8b126d650")

# 调用 DeepSeek API
def call_deepseek(prompt: str) -> str:
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "抱歉，无法获取响应。请稍后再试。"

# 处理用户输入
@deepseek_handler.handle()
async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    
    if not msg:
        await deepseek_handler.finish("请输入你想问的问题！", at_sender=True)
    
    # 调用 DeepSeek 获取回复
    response = call_deepseek(msg)
    
    # 返回 DeepSeek 的回答
    await deepseek_handler.send(response, at_sender=True)

