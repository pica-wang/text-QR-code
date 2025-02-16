import qrcode
import urllib.parse
import os
import base64  # 导入 base64 模块

def txt_to_wechat_qrcode():
    # 获取并验证文件路径
    while True:
        txt_path = input("请输入txt文件路径：").strip().strip('"')
        if not os.path.exists(txt_path):
            print("文件不存在，请重新输入！")
            continue
        if not txt_path.lower().endswith('.txt'):
            print("请选择有效的txt文件！")
            continue
        break

    # 读取并预处理内容
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
        # 微信适配处理
        if len(content) > 500:
            print("[警告] 内容超过500字，建议精简内容以保证微信正常显示")
        encoded_content = urllib.parse.quote(content)  # URL编码
        
    except Exception as e:
        print(f"文件处理失败：{str(e)}")
        return

    # 生成微信兼容二维码
    try:
        qr = qrcode.QRCode(
            version=4,  # 动态调整版本
            error_correction=qrcode.constants.ERROR_CORRECT_Q,  # 提高容错率
            box_size=8,
            border=2,
        )
        
        # 使用微信兼容的文本格式
        qr_data = f"http://tmp.weixin.qq.com/msg/plaintext?content={encoded_content}"
        qr.add_data(qr_data)
        qr.make(fit=True)

        # 生成高对比度图片
        img = qr.make_image(fill_color="#1a1a1a", back_color="#ffffff")  # 微信风格配色
        
        # 保存结果
        output_path = input("请输入输出路径（默认：wechat_qrcode.png）：").strip().strip('"') or "wechat_qrcode.png"
        img.save(output_path)
        
        print(f"已生成微信兼容二维码：{os.path.abspath(output_path)}")
        print("提示：请确保文本长度<500字且不包含敏感词")

    except Exception as e:
        print(f"生成失败：{str(e)}")

if __name__ == "__main__":
    txt_to_wechat_qrcode()

# 可选的备用方案（如果仍然无法显示）
def generate_base64_qr(content):
    try:
        base64_content = base64.b64encode(content.encode()).decode()
        qr_data = f"data:text/html;base64,{base64_content}"
        qr = qrcode.QRCode(
            version=4,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=8,
            border=2,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#1a1a1a", back_color="#ffffff")
        output_path = input("请输入输出路径（默认：base64_qrcode.png）：").strip().strip('"') or "base64_qrcode.png"
        img.save(output_path)
        print(f"已生成Base64编码的二维码：{os.path.abspath(output_path)}")
    except Exception as e:
        print(f"生成Base64编码二维码失败：{str(e)}")

# 方案二：生成短链接服务（需自行部署）
# short_url = your_shorten_service(content)
# qr_data = short_url