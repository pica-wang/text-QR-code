import qrcode

def generate_qr_code_from_file(file_path, output_filename):
    """
    从txt文件读取内容并生成二维码

    :param file_path: txt文件的路径
    :param output_filename: 保存的二维码图片文件名
    """
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().strip()  # 去除首尾空白字符
        
        # 创建QRCode对象
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # 添加数据
        qr.add_data(data)
        qr.make(fit=True)
        
        # 创建图像
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 保存图像
        img.save(output_filename)
        print(f"二维码已成功保存为 {output_filename}")
    
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到")
    except Exception as e:
        print(f"发生错误：{e}")

# 示例用法
if __name__ == "__main__":
    file_path = input("请输入txt文件的路径: ")
    output_filename = "qr_code.png"
    generate_qr_code_from_file(file_path, output_filename)