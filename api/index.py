#  请求示例：
#  POST 请求数据格式：
#  data：base64 编码图像数据（可选）
#  file：上传的图像文件（可选）
#  url：图像 URL（可选）
#  headers：自定义请求头（可选），格式为 "Key1:Value1;Key2:Value2"
#  params：自定义表单参数（可选），格式为 "param1=value1&param2=value2"

# import base64
# import binascii
# import aiohttp
# import ddddocr
from fastapi import FastAPI, UploadFile, Form, File, HTTPException
# from typing import Union, Dict, Optional

# 初始化 FastAPI 应用
app = FastAPI()

# # 允许的文件扩展名
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'jfif'}

# # 初始化 OCR
# ocr = ddddocr.DdddOcr()

# # 检查文件扩展名是否允许
# def allowed_file(filename: str) -> bool:
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # 解码图像数据
# def decode_image(image: Union[UploadFile, str, None]) -> bytes:
#     if image is None:
#         raise HTTPException(status_code=400, detail="未提供图像")

#     if isinstance(image, UploadFile):
#         return image.file.read()
#     elif isinstance(image, str):
#         if image.startswith(('data:image/', 'data:application/')):
#             try:
#                 return base64.b64decode(image.split(',')[1])
#             except (binascii.Error, ValueError):
#                 raise HTTPException(status_code=400, detail="无效的 base64 字符串")
#         raise HTTPException(status_code=400, detail="无效的 base64 数据")
#     else:
#         raise HTTPException(status_code=400, detail="无效的图像输入")

# # 从 URL 获取图像数据及 Cookie（异步）
# async def fetch_image_from_url(url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, str]] = None) -> Dict[str, Union[bytes, str]]:
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url, headers=headers, params=params, timeout=10) as response:
#                 response.raise_for_status()
#                 cookies = '; '.join(f'{key}={value}' for key, value in response.cookies.items())
#                 return {'image': await response.read(), 'cookies': cookies}
#     except aiohttp.ClientError as e:
#         raise HTTPException(status_code=400, detail=f"从 URL 获取图像时出错: {str(e)}")

# @app.post('/ocr')
# async def ocr_endpoint(
#     data: Optional[str] = Form(None),        # Base64 编码的图像数据
#     file: Optional[UploadFile] = File(None), # 上传的图像文件
#     url: Optional[str] = Form(None),         # 图像 URL
#     headers: Optional[str] = Form(None),     # 图像请求的自定义头部
#     params: Optional[str] = Form(None)       # 图像请求的自定义参数
# ):
#     headers_dict = dict(item.split(':', 1) for item in headers.split(';')) if headers else None
#     params_dict = dict(item.split('=', 1) for item in params.split('&')) if params else None

#     if data:
#         try:
#             image_data = decode_image(data)
#             res = ocr.classification(image_data)
#             if not res:
#                 raise HTTPException(status_code=404, detail="OCR 识别失败")
#             return {'code': 200, 'data': str(res), 'msg': '识别成功'}
#         except HTTPException as e:
#             return {'code': e.status_code, 'msg': e.detail}
#         except Exception:
#             raise HTTPException(status_code=500, detail="OCR 处理错误")

#     if file:
#         if not allowed_file(file.filename):
#             return {'code': -202, 'msg': '文件格式不支持'}
#         try:
#             image_data = await file.read()  # 使用异步读取
#             res = ocr.classification(image_data)
#             if not res:
#                 raise HTTPException(status_code=404, detail="OCR 识别失败")
#             return {'code': 200, 'data': str(res), 'msg': '识别成功'}
#         except HTTPException as e:
#             return {'code': e.status_code, 'msg': e.detail}
#         except Exception:
#             raise HTTPException(status_code=500, detail="OCR 处理错误")

#     if url:
#         try:
#             result = await fetch_image_from_url(url, headers=headers_dict, params=params_dict)
#             image_data = result['image']
#             cookies = result['cookies']
#             res = ocr.classification(image_data)
#             if not res:
#                 raise HTTPException(status_code=404, detail="OCR 识别失败")
#             return {'code': 200, 'data': str(res), 'cookies': cookies, 'msg': '识别成功'}
#         except HTTPException as e:
#             return {'code': e.status_code, 'msg': e.detail}
#         except Exception:
#             raise HTTPException(status_code=500, detail="OCR 处理错误")

#     return {'code': -200, 'msg': '图片处理失败'}

@app.route('/', methods=["GET"])
def return_OneText():
    return "<h1>欢迎使用本接口</h1>"
