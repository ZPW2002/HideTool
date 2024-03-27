from flask import request, render_template
from flask_cors import CORS
from json_flask import JsonFlask
from json_response import JsonResponse
from tools import SQLManager, mask_dic, os_hide, os_mask, port
import json
import threading
from tkinter import _get_temp_root
import webview
from gevent import pywsgi

# 创建视图应用
app = JsonFlask(__name__)

# 解决跨域
CORS(app, supports_credentials=True)

db = SQLManager()


@app.route("/")
def main_():
    return render_template('index.html', port=port)


@app.route("/all", methods=["GET"])
def all_():
    result = db.get_list(sql='select * from data')
    tar = []

    for item in result:
        item['path'] = item['path'].split('.{')[0]
        tar.append(item)

    return JsonResponse.success(msg='查询成功', data=tar)


@app.route("/sel", methods=["GET"])
def sel():
    master = _get_temp_root()
    master.attributes("-topmost", 1)
    path = master.call("tk_chooseDirectory")

    folder = path.split('/')[-1]
    # print(path, folder)

    return JsonResponse.success(msg='选择成功', data={'path': path, 'folder': folder})


# 添加
@app.route("/add", methods=["POST"])
def add():
    # print(request.data)
    data = json.loads(request.data)
    if db.is_exist(data['path']):
        return JsonResponse.fail(msg='目录已存在')
    path_sql = data['path'] + mask_dic(data['mask'])

    if msg_ := os_hide(data['path'], data['hide']):
        return JsonResponse.fail(msg=msg_)
    if msg_ := os_mask(data['path'], data['mask']):
        return JsonResponse.fail(msg=msg_)

    isOk = db.modify(
        sql=f"insert into data values('{path_sql}','{data['folder']}','{data['hide']}', '{data['mask']}')",
        args=[data['path'], 'add']
        # comm=False
    )
    # db.commit_()
    return JsonResponse.success(msg='添加成功') if isOk else JsonResponse.fail(msg='添加失败')


# 修改
@app.route("/update", methods=["POST"])
def update():
    data = json.loads(request.data)
    path_sql = data['path'] + mask_dic(data['mask'])

    path_real = db.path_real(data['path'])

    if msg_ := os_hide(path_real, data['hide']):
        return JsonResponse.fail(msg=msg_)

    if msg_ := os_mask(path_real, data['mask']):
        return JsonResponse.fail(msg=msg_)

    isOk = db.modify(
        sql="UPDATE data SET path='{}', hide='{}', mask='{}' WHERE path='{}'".format(
            path_sql, data['hide'], data['mask'], db.path_real(data['path'])
        ),
        args=[data['path'], 'upd']
        # comm=False
    )

    # db.commit_()
    return JsonResponse.success(msg='修改成功') if isOk else JsonResponse.fail(msg='修改失败')


# 删除
@app.route("/delete", methods=["POST"])
def delete():
    data = json.loads(request.data)
    os_mask(db.path_real(data['path']), '无')
    os_hide(data['path'], '否')
    isOk = db.modify(
        sql=f"delete from data where path='{db.path_real(data['path'])}'",
        args=[data['path'], 'del']
        # comm=False
    )
    # db.commit_()
    return JsonResponse.success(msg='删除成功') if isOk else JsonResponse.fail(msg='删除失败')


def flask_server():
    server = pywsgi.WSGIServer(('0.0.0.0', port), app)
    server.serve_forever()
    # app.run(host="0.0.0.0", port=port, debug=False)


if __name__ == '__main__':
    threading.Thread(name='flask_server', target=flask_server, daemon=True).start()

    webview.create_window(
        title='HideTool',
        url=f'http://localhost:{port}',
        width=1200,
        height=750,
        resizable=False
    )
    webview.start()
